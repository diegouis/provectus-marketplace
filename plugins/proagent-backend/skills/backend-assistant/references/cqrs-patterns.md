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
