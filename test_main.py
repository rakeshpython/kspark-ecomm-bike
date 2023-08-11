from fastapi import FastAPI
from fastapi.testclient import TestClient
from bike import Bike
from main import app
from pydantic import BaseModel

client = TestClient(app=app)


def test_bikek_shop():
    with TestClient(app) as client:
        response = client.get("/")
        
        assert response.status_code == 200
        assert response.json() == {"message": "Welcome to the Bike Shop"}


# def test_add_new_bikek():
#     with TestClient(app) as client:
#         response = client.post("/new-bike/", json={"id": 1,"brand": "Hero","Engine_capacity": "200cc","price": "4000"})
        
#         assert response.status_code == 201
              
#         body = response.json()
#         assert body.get("id") == 1
#         assert body.get("brand") == "Hero"
#         assert body.get("Engine_capacity") == "200cc"
#         assert body.get("price") == 4000
        
        
