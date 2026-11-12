from pydantic import BaseModel, Field
from uuid import UUID, uuid4

class CustomerCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: str = Field(min_length=5, max_length=254)

class Customer(BaseModel):
    id: UUID
    name: str
    email: str

def build_customer(payload: CustomerCreate) -> Customer:
    return Customer(id=uuid4(), **payload.model_dump())
