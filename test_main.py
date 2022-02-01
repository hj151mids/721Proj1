import requests
from fastapi.testclient import TestClient
from fastapi import FastAPI

app = FastAPI()
client=TestClient(app)
@app.get("/")
async def root():
    return {"message": "Completed Project 1"}
@app.get("/multiply/{num1}/{num2}")
async def multiply(num1: int, num2: int):
    """Multiply two numbers together"""
    total = num1 * num2
    return {"total": total}
def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Completed Project 1"}

def test_multiply():
    response = client.get("/multiply/2/4")
    assert response.status_code == 200
    assert response.json() == {"total":8}