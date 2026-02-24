## Authentication and Authorization

### JWT Authentication with Refresh Tokens

```python
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import re

SECRET_KEY = os.getenv('JWT_SECRET_KEY')
REFRESH_SECRET = os.getenv('JWT_REFRESH_SECRET')

def validate_password_strength(password):
    if len(password) < 12:
        raise ValueError("Password must be at least 12 characters")
    if not re.search(r'[A-Z]', password):
        raise ValueError("Password must contain uppercase letter")
    if not re.search(r'[a-z]', password):
        raise ValueError("Password must contain lowercase letter")
    if not re.search(r'[0-9]', password):
        raise ValueError("Password must contain number")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        raise ValueError("Password must contain special character")

def create_user(username, password):
    validate_password_strength(password)
    password_hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)
    user = User(username=username, password_hash=password_hash)
    db.session.add(user)
    db.session.commit()
    logger.info(f"User created: {username}")

def login(username, password):
    user = User.query.filter_by(username=username).first()
    if not user:
        time.sleep(0.5)  # Prevent user enumeration
        logger.warning(f"Login attempt for non-existent user: {username}")
        return None

    if user.locked_until and user.locked_until > datetime.utcnow():
        logger.warning(f"Login attempt on locked account: {username}")
        return None

    if check_password_hash(user.password_hash, password):
        user.failed_login_attempts = 0
        user.last_login = datetime.utcnow()
        db.session.commit()

        access_token = jwt.encode(
            {'user_id': str(user.id), 'exp': datetime.utcnow() + timedelta(minutes=15)},
            SECRET_KEY, algorithm='HS256'
        )
        refresh_token = jwt.encode(
            {'user_id': str(user.id), 'exp': datetime.utcnow() + timedelta(days=7)},
            REFRESH_SECRET, algorithm='HS256'
        )
        return {'access_token': access_token, 'refresh_token': refresh_token}
    else:
        user.failed_login_attempts += 1
        if user.failed_login_attempts >= 5:
            user.locked_until = datetime.utcnow() + timedelta(minutes=30)
            logger.warning(f"Account locked: {username}")
        db.session.commit()
        return None
```

### Role-Based Access Control (RBAC)

```python
from functools import wraps
from flask import g, jsonify, request

def require_permission(permission):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if not g.current_user:
                return jsonify({'error': 'Authentication required'}), 401
            if not g.current_user.has_permission(permission):
                logger.warning(
                    f"Unauthorized access: user={g.current_user.id} path={request.path}"
                )
                return jsonify({'error': 'Permission denied'}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator

@app.route('/api/v1/orders/<order_id>')
@login_required
def get_order(order_id):
    order = Order.query.get_or_404(order_id)
    if order.user_id != g.current_user.id and not g.current_user.is_admin:
        logger.warning(f"Unauthorized order access: user={g.current_user.id} order={order_id}")
        return jsonify({'error': 'Access denied'}), 403
    return jsonify(order.to_dict())

@app.route('/api/v1/admin/users')
@login_required
@require_permission('admin.users.read')
def get_all_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])
```

### Rate Limiting

```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["1000 per day", "100 per hour"],
    storage_uri="redis://localhost:6379"
)

@app.route('/api/v1/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    # Strict rate limiting for authentication endpoints
    pass

@app.route('/api/v1/search')
@limiter.limit("30 per minute")
def search():
    # Moderate rate limiting for search
    pass

@app.errorhandler(429)
def ratelimit_handler(e):
    logger.warning(f"Rate limit exceeded: {get_remote_address()}")
    return jsonify({
        'error': 'RateLimitExceeded',
        'message': 'Too many requests. Please try again later.'
    }), 429
```

## Security Best Practices

### Input Validation and SQL Injection Prevention

```python
from sqlalchemy import text

# VULNERABLE: String concatenation
sql = f"SELECT * FROM users WHERE username LIKE '%{query}%'"

# SAFE: Parameterized query
sql = text("SELECT id, username, email FROM users WHERE username LIKE :query")
users = db.engine.execute(sql, {'query': f'%{query}%'}).fetchall()

# SAFEST: ORM with built-in parameterization
users = User.query.filter(User.username.like(f'%{query}%')).all()
```

### Secure File Upload

```python
from werkzeug.utils import secure_filename
import magic

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

@app.route('/api/v1/upload', methods=['POST'])
@login_required
@limiter.limit("10 per hour")
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400

    if not ('.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS):
        return jsonify({'error': 'File type not allowed'}), 400

    file.seek(0, os.SEEK_END)
    if file.tell() > MAX_FILE_SIZE:
        return jsonify({'error': 'File too large'}), 400
    file.seek(0)

    mime = magic.from_buffer(file.read(1024), mime=True)
    file.seek(0)
    if mime not in ['image/png', 'image/jpeg', 'image/gif', 'application/pdf']:
        return jsonify({'error': 'Invalid file content'}), 400

    filename = f"{uuid.uuid4()}_{secure_filename(file.filename)}"
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return jsonify({'filename': filename})
```

### Secrets Management

```python
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('EXTERNAL_API_KEY')
DATABASE_URL = os.getenv('DATABASE_URL')

if not API_KEY:
    raise ValueError("EXTERNAL_API_KEY environment variable not set")

# Production: use cloud secrets manager
try:
    import boto3
    secrets_client = boto3.client('secretsmanager')
    secret = secrets_client.get_secret_value(SecretId='prod/api/keys')
    API_KEY = json.loads(secret['SecretString'])['external_api_key']
except Exception:
    pass  # Fallback to environment variable
```
