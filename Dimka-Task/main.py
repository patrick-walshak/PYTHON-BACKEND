# Task: Build a Jos Market Produce API Project Overview
# Create a simple API for managing a produce market in Jos, Nigeria. Vendors can list their farm produce, and buyers can browse and place orders.
# Data Models (Pydantic)
# 1. Vendor
# 2. Produce
# 3. Order

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI(title="Jos market produce!")

vendors_db = {}
produce_db = {}
orders_db = {}

class Vendor(BaseModel):
    id: int
    name: str
    market_location: str #(Terminus, Katako, Bukuru, Farin Gada, Building Materials)
    phone: str
    created_at: datetime = datetime.now()

class Produce(BaseModel):
    id: int
    vendor_id: int
    name: str #(e.g., "Irish Potato", "Tomatoes", "Carrots", "Cabbage")
    quantity_kg: float #(in kilograms)
    price_per_kg: float #(in Naira)
    category: str #(Vegetables, Fruits, Grains, Tubers)
    is_available: bool =True

class Order(BaseModel):
    id: int
    produce_id: int
    buyer_name: str
    buyer_phone: str
    produce_name: str
    quantity_kg: float
    total_price: float
    delivery_area: str #(Rayfield, Bukuru, Terminus, Jos South, etc.)
    status: str #(pending, confirmed, delivered)
    created_at: datetime = datetime.now()


#VENDORS ENDPOINT

@app.post("/vendors")
def create_vendor(vendor: Vendor):
    if vendor.id in vendors_db:
        raise HTTPException(status_code=400, detail="Vendor already exists")
    vendors_db[vendor.id] = vendor
    return {"message": "Vendor registered successfully!", "vendor": vendor}

@app.get("/vendors")
def get_all_vendors():
    return list(vendors_db.values())

@app.put("/vendors/{id}")
def update_vendor(id: int, updated_vendor: Vendor):
    if id not in vendors_db:
        raise HTTPException(status_code=404, detail="Vendor not found")
    vendors_db[id] = updated_vendor
    return {"message": "Vendor updated successfully", "vendor": updated_vendor}


@app.delete("/vendors/{id}")
def delete_vendor(id: int):
    if id not in vendors_db:
        raise HTTPException(status_code=404, detail="Vendor not found")
    del vendors_db[id]
    return {"message": "Vendor removed successfully"}
                                                                
# PRODUCE EMDPOINT

@app.get("/produce")
def creat_produce(produce: Produce):
    if produce.id in produce_db:
        raise HTTPException(status_code=400, detail="Produce already exist!")
    if produce.vendor_id not in vendors_db:
        raise HTTPException(status_code=404, detail="Vendor not found")
    produce_db[produce.id] = produce
    return {"message": "Produce added successfully", "produce": produce}

@app.get("/produce/{id}")
def get_produce(id: int):
    produce = produce_db.get(id)
    if not produce:
        raise HTTPException(status_code=404, detail="Produce not found")
    return produce

@app.patch("/produce/{id}/stock")
def update_produce_stock(id: int, quantity_kg: float):
    if id not in produce_db:
        raise HTTPException(status_code=404, detail="Produce not found")
    produce_db[id].quantity_kg = quantity_kg
    produce_db[id].is_available = quantity_kg > 0
    return {"message": "Produce stock updated", "produce": produce_db[id]}


@app.delete("/produce/{id}")
def delete_produce(id: int):
    if id not in produce_db:
        raise HTTPException(status_code=404, detail="Produce not found")
    del produce_db[id]
    return {"message": "Produce deleted successfully"}
