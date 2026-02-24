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
