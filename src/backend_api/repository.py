from .models import Customer

class InMemoryCustomerRepository:
    """Replace with a SQLAlchemy/PostgreSQL repository for durable storage."""
    def __init__(self):
        self._items: dict[str, Customer] = {}

    def add(self, customer: Customer) -> Customer:
        key = str(customer.id)
        self._items[key] = customer
        return customer

    def get(self, customer_id: str) -> Customer | None:
        return self._items.get(customer_id)
