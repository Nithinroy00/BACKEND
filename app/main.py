from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Data model for a car
class Car(BaseModel):
    id: int
    brand: str
    model: str
    year: int

# In-memory "database"
cars_db: List[Car] = []

# GET endpoint to fetch all cars
@app.get("/cars", response_model=List[Car])
def get_cars():
    return cars_db

# POST endpoint to add a new car
@app.post("/cars", response_model=Car)
def add_car(car: Car):
    cars_db.append(car)
    return car