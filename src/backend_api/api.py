from fastapi import FastAPI, HTTPException
from .models import CustomerCreate, build_customer
from .repository import InMemoryCustomerRepository

app = FastAPI(title="Python Microservices Platform")
repository = InMemoryCustomerRepository()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/customers", status_code=201)
def create_customer(payload: CustomerCreate):
    return repository.add(build_customer(payload))

@app.get("/customers/{customer_id}")
def get_customer(customer_id: str):
    customer = repository.get(customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer
