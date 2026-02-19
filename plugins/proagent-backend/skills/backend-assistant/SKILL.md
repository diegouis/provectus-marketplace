---
name: backend-assistant
description: Building Scalable Backend Services - APIs (REST, GraphQL, gRPC), database schema engineering, microservices architecture, CQRS/event-sourcing, saga orchestration, authentication and authorization, message queues, caching strategies, performance optimization, and MCP server development. Use when performing any backend development, API design, database design, service architecture, or MCP server creation task.
---

# Building Scalable Backend Services

Comprehensive backend engineering skill covering the full lifecycle of API design, database schema engineering, microservices architecture, CQRS/event-sourcing, saga orchestration, authentication, caching, performance optimization, and MCP server development. Built from 83 production-tested assets across 10 Provectus engineering repositories including `agents`, `casdk-harness`, `claude-ui`, `ralph-orchestrator`, `taches-cc-resources`, and `provectus-marketplace`.

## When to Use This Skill

- Designing REST, GraphQL, or gRPC APIs for new services
- Engineering database schemas for relational (PostgreSQL, MySQL) and NoSQL (MongoDB, DynamoDB) databases
- Architecting microservices with clear boundaries and inter-service communication
- Implementing authentication (JWT, OAuth2, session-based) and authorization (RBAC, ABAC)
- Setting up message queues (RabbitMQ, SQS, Kafka) for asynchronous processing
- Implementing caching layers (Redis, Memcached, HTTP caching)
- Optimizing database queries, fixing N+1 problems, and improving response times
- Reviewing backend code for security vulnerabilities and performance issues
- Implementing CQRS with separate read/write models following `agents/plugins/backend-development/skills/cqrs-implementation/SKILL.md`
- Orchestrating distributed transactions with saga patterns from `agents/plugins/backend-development/skills/saga-orchestration/SKILL.md`
- Building MCP servers in Python and TypeScript following `taches-cc-resources/skills/create-mcp-servers/SKILL.md`
- Scaffolding Fastify+tRPC backends based on `ralph-orchestrator/backend/ralph-web-server/package.json`

## API Design

### RESTful API Design

**Resource Modeling:**
- Resources are nouns (users, orders, products), never verbs
- Use HTTP methods for actions: GET (read), POST (create), PUT/PATCH (update), DELETE (remove)
- URLs represent resource hierarchies with proper nesting
- Always version APIs from day one: `/api/v1/resources`

**Endpoint Design Pattern:**

```
GET    /api/v1/products              # List products (with pagination)
POST   /api/v1/products              # Create product
GET    /api/v1/products/{id}         # Get product details
PUT    /api/v1/products/{id}         # Replace product
PATCH  /api/v1/products/{id}         # Update product fields
DELETE /api/v1/products/{id}         # Delete product

GET    /api/v1/products/{id}/reviews # Get product reviews (nested resource)
POST   /api/v1/products/{id}/reviews # Create review for product
```

**Pagination Pattern:**

```python
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing import List, Optional

class PaginationParams(BaseModel):
    page: int = Field(1, ge=1, description="Page number")
    page_size: int = Field(20, ge=1, le=100, description="Items per page")

class PaginatedResponse(BaseModel):
    items: List[dict]
    total: int
    page: int
    page_size: int
    pages: int
    has_next: bool
    has_prev: bool

app = FastAPI()

@app.get("/api/v1/products", response_model=PaginatedResponse)
async def list_products(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    category: Optional[str] = Query(None),
    sort: Optional[str] = Query("created_at:desc")
):
    query = build_query(category=category)
    total = await count_products(query)
    offset = (page - 1) * page_size
    products = await fetch_products(query, limit=page_size, offset=offset, sort=sort)

    pages = (total + page_size - 1) // page_size
    return PaginatedResponse(
        items=products,
        total=total,
        page=page,
        page_size=page_size,
        pages=pages,
        has_next=page < pages,
        has_prev=page > 1
    )
```

**Error Response Pattern:**

```python
from fastapi import HTTPException, status

class ErrorResponse(BaseModel):
    error: str
    message: str
    details: Optional[dict] = None

def raise_not_found(resource: str, id: str):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={
            "error": "NotFound",
            "message": f"{resource} not found",
            "details": {"id": id}
        }
    )

def raise_validation_error(field: str, message: str, value=None):
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail={
            "error": "ValidationError",
            "message": "Request validation failed",
            "details": {"field": field, "message": message, "value": value}
        }
    )

@app.get("/api/v1/users/{user_id}")
async def get_user(user_id: str):
    user = await fetch_user(user_id)
    if not user:
        raise_not_found("User", user_id)
    return user
```

### GraphQL API Design

**Schema-First Design:**

```graphql
type User {
  id: ID!
  email: String!
  name: String!
  createdAt: DateTime!
  orders(first: Int = 20, after: String, status: OrderStatus): OrderConnection!
  profile: UserProfile
}

type Order {
  id: ID!
  status: OrderStatus!
  total: Money!
  items: [OrderItem!]!
  createdAt: DateTime!
  user: User!
}

# Relay-style cursor pagination
type OrderConnection {
  edges: [OrderEdge!]!
  pageInfo: PageInfo!
  totalCount: Int!
}

type OrderEdge {
  node: Order!
  cursor: String!
}

type PageInfo {
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: String
  endCursor: String
}

enum OrderStatus {
  PENDING
  CONFIRMED
  SHIPPED
  DELIVERED
  CANCELLED
}

scalar DateTime
scalar Money

type Query {
  user(id: ID!): User
  users(first: Int = 20, after: String, search: String): UserConnection!
  order(id: ID!): Order
}

type Mutation {
  createUser(input: CreateUserInput!): CreateUserPayload!
  updateUser(input: UpdateUserInput!): UpdateUserPayload!
  createOrder(input: CreateOrderInput!): CreateOrderPayload!
}

input CreateUserInput {
  email: String!
  name: String!
  password: String!
}

type CreateUserPayload {
  user: User
  errors: [Error!]
}

type Error {
  field: String
  message: String!
}
```

**DataLoader for N+1 Prevention:**

```python
from aiodataloader import DataLoader

class UserLoader(DataLoader):
    async def batch_load_fn(self, user_ids):
        users = await fetch_users_by_ids(user_ids)
        user_map = {user["id"]: user for user in users}
        return [user_map.get(uid) for uid in user_ids]

class OrdersByUserLoader(DataLoader):
    async def batch_load_fn(self, user_ids):
        orders = await fetch_orders_by_user_ids(user_ids)
        orders_by_user = {}
        for order in orders:
            orders_by_user.setdefault(order["user_id"], []).append(order)
        return [orders_by_user.get(uid, []) for uid in user_ids]
```

### gRPC Service Design

```protobuf
syntax = "proto3";

package backend.orders;

service OrderService {
  rpc CreateOrder(CreateOrderRequest) returns (CreateOrderResponse);
  rpc GetOrder(GetOrderRequest) returns (Order);
  rpc ListOrders(ListOrdersRequest) returns (ListOrdersResponse);
  rpc StreamOrderUpdates(StreamOrderRequest) returns (stream OrderUpdate);
}

message CreateOrderRequest {
  string user_id = 1;
  repeated OrderItem items = 2;
  Address shipping_address = 3;
}

message Order {
  string id = 1;
  string user_id = 2;
  OrderStatus status = 3;
  repeated OrderItem items = 4;
  Money total = 5;
  google.protobuf.Timestamp created_at = 6;
}

enum OrderStatus {
  ORDER_STATUS_UNSPECIFIED = 0;
  ORDER_STATUS_PENDING = 1;
  ORDER_STATUS_CONFIRMED = 2;
  ORDER_STATUS_SHIPPED = 3;
  ORDER_STATUS_DELIVERED = 4;
  ORDER_STATUS_CANCELLED = 5;
}

message ListOrdersRequest {
  string user_id = 1;
  int32 page_size = 2;
  string page_token = 3;
  OrderStatus status_filter = 4;
}

message ListOrdersResponse {
  repeated Order orders = 1;
  string next_page_token = 2;
  int32 total_count = 3;
}
```

## Database Schema Engineering

### Relational Database Design (PostgreSQL)

**Complete E-Commerce Schema:**

```sql
-- Users table with proper constraints and indexes
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  username VARCHAR(50) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  phone VARCHAR(20),
  email_verified BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  last_login_at TIMESTAMP
);

-- Products table with business rule constraints
CREATE TABLE products (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(255) NOT NULL,
  slug VARCHAR(255) UNIQUE NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
  compare_at_price DECIMAL(10, 2) CHECK (compare_at_price >= price),
  cost DECIMAL(10, 2) CHECK (cost >= 0),
  sku VARCHAR(100) UNIQUE,
  stock_quantity INTEGER DEFAULT 0 CHECK (stock_quantity >= 0),
  low_stock_threshold INTEGER DEFAULT 10,
  is_active BOOLEAN DEFAULT TRUE,
  is_featured BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Orders table with status workflow constraints
CREATE TABLE orders (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES users(id),
  order_number VARCHAR(50) UNIQUE NOT NULL,
  status VARCHAR(20) DEFAULT 'pending' CHECK (
    status IN ('pending', 'processing', 'shipped', 'delivered', 'cancelled', 'refunded')
  ),
  subtotal DECIMAL(10, 2) NOT NULL,
  tax DECIMAL(10, 2) NOT NULL,
  shipping DECIMAL(10, 2) NOT NULL,
  discount DECIMAL(10, 2) DEFAULT 0,
  total DECIMAL(10, 2) NOT NULL,
  currency VARCHAR(3) DEFAULT 'USD',
  payment_method VARCHAR(50),
  payment_status VARCHAR(20),
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  shipped_at TIMESTAMP,
  delivered_at TIMESTAMP
);

-- Order items with snapshot data
CREATE TABLE order_items (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  order_id UUID NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
  product_id UUID NOT NULL REFERENCES products(id),
  product_name VARCHAR(255) NOT NULL,
  sku VARCHAR(100),
  quantity INTEGER NOT NULL CHECK (quantity > 0),
  unit_price DECIMAL(10, 2) NOT NULL,
  subtotal DECIMAL(10, 2) NOT NULL,
  tax DECIMAL(10, 2) DEFAULT 0,
  total DECIMAL(10, 2) NOT NULL
);

-- Many-to-many with junction table
CREATE TABLE product_categories (
  product_id UUID REFERENCES products(id) ON DELETE CASCADE,
  category_id UUID REFERENCES categories(id) ON DELETE CASCADE,
  PRIMARY KEY (product_id, category_id)
);

-- Indexes for common query patterns
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_products_slug ON products(slug);
CREATE INDEX idx_products_active_featured ON products(is_active, is_featured);
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_orders_created_at ON orders(created_at DESC);
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
CREATE INDEX idx_order_items_product_id ON order_items(product_id);

-- Auto-update timestamps trigger
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = CURRENT_TIMESTAMP;
  RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users
  FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_products_updated_at BEFORE UPDATE ON products
  FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_orders_updated_at BEFORE UPDATE ON orders
  FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
```

### Document Database Design (MongoDB)

```javascript
// Users collection - embedding addresses for read performance
{
  "_id": ObjectId("..."),
  "email": "user@example.com",
  "username": "johndoe",
  "passwordHash": "...",
  "profile": {
    "firstName": "John",
    "lastName": "Doe",
    "phone": "+1234567890",
    "avatar": "https://cdn.example.com/avatars/user123.jpg"
  },
  "addresses": [
    {
      "type": "shipping",
      "street": "123 Main St",
      "city": "New York",
      "state": "NY",
      "postalCode": "10001",
      "country": "US",
      "isDefault": true
    }
  ],
  "emailVerified": false,
  "createdAt": ISODate("2026-01-20T10:00:00Z"),
  "updatedAt": ISODate("2026-01-20T10:00:00Z")
}

// Orders collection - embedding items for atomic reads
{
  "_id": ObjectId("..."),
  "orderNumber": "ORD-2026-001234",
  "userId": ObjectId("..."),
  "status": "processing",
  "items": [
    {
      "productId": ObjectId("..."),
      "productName": "Wireless Headphones",
      "sku": "WH-001",
      "quantity": 1,
      "unitPrice": 199.99,
      "subtotal": 199.99
    }
  ],
  "pricing": {
    "subtotal": 199.99,
    "tax": 16.00,
    "shipping": 10.00,
    "discount": 20.00,
    "total": 205.99,
    "currency": "USD"
  },
  "payment": {
    "method": "credit_card",
    "status": "paid",
    "transactionId": "txn_abc123"
  },
  "createdAt": ISODate("2026-01-20T10:30:00Z"),
  "updatedAt": ISODate("2026-01-21T09:00:00Z")
}

// Indexes
db.users.createIndex({ "email": 1 }, { unique: true });
db.users.createIndex({ "username": 1 }, { unique: true });
db.orders.createIndex({ "userId": 1 });
db.orders.createIndex({ "orderNumber": 1 }, { unique: true });
db.orders.createIndex({ "status": 1 });
db.orders.createIndex({ "createdAt": -1 });
```

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

## Caching Strategies

### Redis Caching with Invalidation

```python
import redis
import json
from functools import wraps

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def cache_response(ttl=300):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            cache_key = f"cache:{f.__name__}:{':'.join(map(str, args))}"
            cached = redis_client.get(cache_key)
            if cached:
                return json.loads(cached)
            result = f(*args, **kwargs)
            redis_client.setex(cache_key, ttl, json.dumps(result))
            return result
        return wrapper
    return decorator

@app.route('/api/v1/products/<product_id>')
@cache_response(ttl=300)
def get_product(product_id):
    product = db.session.query(Product)\
        .options(joinedload(Product.category))\
        .options(joinedload(Product.reviews))\
        .filter_by(id=product_id).first()

    if not product:
        return jsonify({'error': 'Not found'}), 404

    avg_rating = db.session.query(func.avg(Review.rating))\
        .filter_by(product_id=product_id).scalar()

    return jsonify({
        'product': product.to_dict(),
        'average_rating': float(avg_rating or 0)
    })

# Cache invalidation on update
@app.route('/api/v1/products/<product_id>', methods=['PUT'])
def update_product(product_id):
    # Update logic...
    redis_client.delete(f"cache:get_product:{product_id}")
    return jsonify({'message': 'Updated'})
```

## Performance Optimization

### Fixing N+1 Query Problems

```python
# BEFORE: 1001 queries for 1000 users (~5000ms)
@app.route('/api/v1/users')
def get_users_slow():
    users = User.query.all()
    result = []
    for user in users:
        orders = Order.query.filter_by(user_id=user.id).all()
        result.append({
            'user': user.to_dict(),
            'order_count': len(orders),
            'total_spent': sum(order.total for order in orders)
        })
    return jsonify(result)

# AFTER: 1 query with JOIN (~50ms, 100x faster)
@app.route('/api/v1/users')
def get_users_fast():
    user_stats = db.session.query(
        User,
        func.count(Order.id).label('order_count'),
        func.sum(Order.total).label('total_spent')
    ).outerjoin(Order).group_by(User.id).all()

    result = []
    for user, order_count, total_spent in user_stats:
        result.append({
            'user': user.to_dict(),
            'order_count': order_count or 0,
            'total_spent': float(total_spent or 0)
        })
    return jsonify(result)
```

### Query Optimization with Indexes

```sql
-- BEFORE: Sequential scan, 2500ms
SELECT * FROM orders
WHERE user_id = 123
  AND status = 'completed'
  AND created_at > '2026-01-01'
ORDER BY created_at DESC
LIMIT 10;

-- ADD: Composite index on the query pattern
CREATE INDEX idx_orders_user_status_created
ON orders(user_id, status, created_at DESC);

-- AFTER: Index scan, 5ms (500x faster)

-- Partial index for specific status values
CREATE INDEX idx_orders_completed
ON orders(user_id, created_at DESC)
WHERE status = 'completed';
```

### Async Parallel Requests

```python
import asyncio
import aiohttp

async def fetch_json(session, url):
    async with session.get(url, timeout=aiohttp.ClientTimeout(total=30)) as response:
        return await response.json()

async def get_user_dashboard(user_id):
    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_json(session, f'{USER_API}/users/{user_id}'),
            fetch_json(session, f'{ORDER_API}/orders?user={user_id}'),
            fetch_json(session, f'{REC_API}/recommend/{user_id}'),
            fetch_json(session, f'{REVIEW_API}/reviews?user={user_id}'),
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        user_data, orders, recommendations, reviews = results

        return {
            'user': user_data if not isinstance(user_data, Exception) else None,
            'orders': orders if not isinstance(orders, Exception) else [],
            'recommendations': recommendations if not isinstance(recommendations, Exception) else [],
            'reviews': reviews if not isinstance(reviews, Exception) else []
        }
# Sequential: ~4000ms -> Parallel: ~1000ms (4x faster)
```

### Connection Pooling

```python
from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(
    minconn=5,
    maxconn=20,
    host='localhost',
    database='myapp',
    user='postgres',
    password=os.getenv('DB_PASSWORD')
)

def get_user(user_id):
    conn = connection_pool.getconn()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT id, username, email FROM users WHERE id = %s', (user_id,))
        user = cursor.fetchone()
        cursor.close()
        return user
    finally:
        connection_pool.putconn(conn)

# Connection overhead: ~50ms per request -> ~2ms per request (25x faster)
```

## Microservices Patterns

### Service Boundaries (Domain-Driven Design)

- Define bounded contexts based on business domains (Orders, Users, Payments, Inventory)
- Each service owns its data store (database-per-service pattern)
- Services communicate via well-defined API contracts
- Use asynchronous messaging for cross-service events

### Resilience Patterns

- **Circuit Breaker**: Detect failing services and stop cascading failures
- **Retry with Backoff**: Exponential backoff with jitter for transient failures
- **Timeout Management**: Set timeouts on all external calls to prevent resource exhaustion
- **Bulkhead Pattern**: Isolate resource pools to prevent one service from consuming all resources
- **Graceful Degradation**: Return cached or partial responses when dependencies fail

### Message Queue Integration

```python
import pika
import json

# Producer: publish order events
def publish_order_event(order_id, event_type, data):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='order_events', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='order_events',
        body=json.dumps({
            'order_id': order_id,
            'event': event_type,
            'data': data,
            'timestamp': datetime.utcnow().isoformat()
        }),
        properties=pika.BasicProperties(delivery_mode=2)  # Persistent
    )
    connection.close()

# Consumer: process order events
def process_order_events():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='order_events', durable=True)
    channel.basic_qos(prefetch_count=1)

    def callback(ch, method, properties, body):
        event = json.loads(body)
        try:
            if event['event'] == 'order.created':
                send_confirmation_email(event['data'])
                update_inventory(event['data'])
            elif event['event'] == 'order.shipped':
                send_shipping_notification(event['data'])
            ch.basic_ack(delivery_tag=method.delivery_tag)
        except Exception as e:
            logger.error(f"Failed to process event: {e}")
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)

    channel.basic_consume(queue='order_events', on_message_callback=callback)
    channel.start_consuming()
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

## CQRS and Event Sourcing

Reference: `agents/plugins/backend-development/skills/cqrs-implementation/SKILL.md`

### Command Query Responsibility Segregation

Separate write (command) and read (query) models for complex domains where read and write patterns differ significantly.

**When to Apply CQRS:**
- Read and write models have different shapes or scaling requirements
- Complex business logic on writes but simple reads (or vice versa)
- Event sourcing is required for audit trails or temporal queries
- Different consistency requirements for reads vs writes

**Command Side Pattern:**

```python
from dataclasses import dataclass
from typing import Protocol

@dataclass
class CreateOrderCommand:
    user_id: str
    items: list[dict]
    shipping_address: dict

class CommandHandler(Protocol):
    async def handle(self, command) -> None: ...

class CreateOrderHandler:
    def __init__(self, event_store, order_repo):
        self.event_store = event_store
        self.order_repo = order_repo

    async def handle(self, command: CreateOrderCommand) -> str:
        order = Order.create(
            user_id=command.user_id,
            items=command.items,
            shipping_address=command.shipping_address,
        )
        await self.order_repo.save(order)
        for event in order.pending_events:
            await self.event_store.append(event)
        return order.id
```

**Query Side Pattern:**

```python
class OrderReadModel:
    """Denormalized read model optimized for query performance."""
    def __init__(self, read_db):
        self.read_db = read_db

    async def get_user_orders(self, user_id: str, page: int = 1, size: int = 20):
        return await self.read_db.query(
            "SELECT * FROM order_projections WHERE user_id = $1 ORDER BY created_at DESC LIMIT $2 OFFSET $3",
            user_id, size, (page - 1) * size
        )

class OrderProjection:
    """Builds read model from domain events."""
    async def handle_order_created(self, event):
        await self.read_db.execute(
            "INSERT INTO order_projections (id, user_id, status, total, item_count, created_at) VALUES ($1, $2, $3, $4, $5, $6)",
            event.order_id, event.user_id, "pending", event.total, len(event.items), event.timestamp
        )
```

### Saga Orchestration

Reference: `agents/plugins/backend-development/skills/saga-orchestration/SKILL.md`

Coordinate distributed transactions across microservices with compensating actions for rollback.

**Orchestration-Based Saga:**

```python
class OrderSagaOrchestrator:
    """Central coordinator that drives the saga steps."""

    async def execute(self, order_data: dict):
        saga_id = str(uuid.uuid4())
        steps_completed = []

        try:
            # Step 1: Reserve inventory
            await self.inventory_service.reserve(order_data["items"])
            steps_completed.append("inventory_reserved")

            # Step 2: Process payment
            payment = await self.payment_service.charge(order_data["user_id"], order_data["total"])
            steps_completed.append("payment_charged")

            # Step 3: Create shipment
            await self.shipping_service.create_shipment(order_data["shipping_address"])
            steps_completed.append("shipment_created")

            # Step 4: Confirm order
            await self.order_service.confirm(order_data["order_id"])

        except Exception as e:
            logger.error(f"Saga {saga_id} failed at step: {e}")
            await self._compensate(steps_completed, order_data)
            raise

    async def _compensate(self, steps_completed: list, order_data: dict):
        """Execute compensating actions in reverse order."""
        compensations = {
            "shipment_created": lambda: self.shipping_service.cancel_shipment(order_data["order_id"]),
            "payment_charged": lambda: self.payment_service.refund(order_data["user_id"], order_data["total"]),
            "inventory_reserved": lambda: self.inventory_service.release(order_data["items"]),
        }
        for step in reversed(steps_completed):
            try:
                await compensations[step]()
            except Exception as comp_error:
                logger.critical(f"Compensation failed for {step}: {comp_error}")
```

**Choreography-Based Saga:**

```python
# Each service listens for events and reacts independently
# OrderService publishes OrderCreated -> InventoryService reserves stock
# InventoryService publishes StockReserved -> PaymentService charges
# PaymentService publishes PaymentCompleted -> ShippingService ships
# If any step fails, the failing service publishes a failure event
# and upstream services react with compensating actions
```

## MCP Server Development

Reference: `taches-cc-resources/skills/create-mcp-servers/SKILL.md`

Build Model Context Protocol servers that expose tools, resources, and prompts to Claude and other LLM clients.

**Python MCP Server (using mcp SDK):**

```python
from mcp.server import Server
from mcp.types import Tool, TextContent
import mcp.server.stdio

server = Server("my-backend-tools")

@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="query-database",
            description="Execute a read-only SQL query against the application database",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "SQL SELECT query to execute"},
                },
                "required": ["query"],
            },
        ),
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "query-database":
        if not arguments["query"].strip().upper().startswith("SELECT"):
            return [TextContent(type="text", text="Error: Only SELECT queries are allowed")]
        result = await db.fetch(arguments["query"])
        return [TextContent(type="text", text=str(result))]

async def main():
    async with mcp.server.stdio.stdio_server() as (read, write):
        await server.run(read, write, server.create_initialization_options())
```

**TypeScript MCP Server:**

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server({ name: "my-backend-tools", version: "1.0.0" }, {
  capabilities: { tools: {} },
});

server.setRequestHandler("tools/list", async () => ({
  tools: [{
    name: "health-check",
    description: "Check the health of backend services",
    inputSchema: { type: "object", properties: { service: { type: "string" } }, required: ["service"] },
  }],
}));

server.setRequestHandler("tools/call", async (request) => {
  if (request.params.name === "health-check") {
    const response = await fetch(`http://${request.params.arguments.service}/health`);
    return { content: [{ type: "text", text: JSON.stringify(await response.json()) }] };
  }
});

const transport = new StdioServerTransport();
await server.connect(transport);
```

## Framework-Specific Patterns

### Fastify + tRPC + SQLite Stack

Reference: `ralph-orchestrator/backend/ralph-web-server/package.json`

Type-safe API layer combining Fastify's performance with tRPC's end-to-end type safety:

```typescript
import Fastify from "fastify";
import { fastifyTRPCPlugin } from "@trpc/server/adapters/fastify";
import { initTRPC } from "@trpc/server";
import { z } from "zod";
import Database from "better-sqlite3";

const db = new Database("app.db");
const t = initTRPC.create();

const appRouter = t.router({
  getUser: t.procedure.input(z.object({ id: z.string() })).query(({ input }) => {
    return db.prepare("SELECT * FROM users WHERE id = ?").get(input.id);
  }),
  createUser: t.procedure
    .input(z.object({ name: z.string(), email: z.string().email() }))
    .mutation(({ input }) => {
      const stmt = db.prepare("INSERT INTO users (name, email) VALUES (?, ?)");
      return stmt.run(input.name, input.email);
    }),
});

const server = Fastify();
server.register(fastifyTRPCPlugin, { prefix: "/trpc", trpcOptions: { router: appRouter } });
await server.listen({ port: 3000 });
```

### Express Reference Patterns

Reference: `claude-ui/server/index.js`, `claude-ui/server/routes/auth.js`

Production Express patterns from the claude-ui server for authentication routes and middleware composition.

### Go Backend Patterns

Reference: `casdk-harness/src/harness/agents/configs/dev-go-expert.md`

Go-specific backend patterns including Gin/Echo/Chi routing, sqlx for database access, and goroutine-based concurrency for high-throughput services.

### Rust Streaming Adapters

Reference: `ralph-orchestrator/crates/ralph-adapters/src/claude_stream.rs`

Rust-based streaming adapters for Claude API integration, demonstrating async stream processing with tokio for high-performance backend services.

## Python 3.12+ Best Practices

When building Python backends, leverage modern Python 3.12+ features:

### Language Features
- **Improved error messages**: More precise tracebacks with fine-grained error locations
- **ExceptionGroup and except***: Handle multiple concurrent exceptions from async tasks
- **TaskGroup**: Structured concurrency with `async with asyncio.TaskGroup() as tg:` for managing parallel async operations
- **Type parameter syntax**: `def foo[T](x: T) -> T:` instead of `TypeVar` boilerplate
- **f-string improvements**: Nested quotes and backslashes now allowed in f-string expressions

### FastAPI Modern Patterns
- Use `Annotated` types for dependency injection: `Annotated[User, Depends(get_current_user)]`
- Prefer `lifespan` context manager over `@app.on_event("startup")` / `@app.on_event("shutdown")`
- Use `APIRouter` with `tags` and `prefix` for modular route organization
- Return Pydantic v2 models directly (automatic serialization with `model_dump()`)

### Django 5.x Patterns
- Use `GeneratedField` for computed database columns
- Leverage `Field.db_default` for database-level defaults
- Use `aiterator()` for async ORM iteration
- Prefer `async` views with `@sync_to_async` for I/O-bound operations

## Visual Diagramming with Excalidraw

Use the Excalidraw MCP server to generate interactive diagrams directly in the conversation. Describe what you need in natural language and Excalidraw renders it as an interactive canvas with hand-drawn style.

### When to Use

- API architecture and microservice topology diagrams
- Database schema and entity relationship diagrams
- Authentication/authorization flow visualizations
- Message queue and async processing flow diagrams

### Workflow

1. Describe the diagram you need — be specific about components, relationships, and layout
2. Review the rendered interactive diagram in the chat
3. Request refinements by describing what to change (add/remove/rearrange elements)
4. Use fullscreen mode for detailed editing when needed

### Tips for Effective Diagrams

- Name specific components and their connections (e.g., "API Gateway connects to Auth Service and User Service")
- Specify layout direction when it matters (e.g., "left-to-right flow" or "top-down hierarchy")
- Request specific diagram types (architecture diagram, flowchart, sequence diagram, ER diagram)
- Iterate — start with the overall structure, then refine details
