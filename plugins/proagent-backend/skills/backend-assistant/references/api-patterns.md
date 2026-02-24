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
