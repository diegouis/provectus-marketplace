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
