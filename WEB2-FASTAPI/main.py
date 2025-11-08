   
from fastapi import FastAPI, HTTPException, status
from typing import Dict, List

app = FastAPI()

db: Dict[int, str] = {
    1: "Alice",
    2: "Bob",
    3: "Jamse",
    4: "Tom",
    5: "Peter"
}


@app.get("/")
def read():
    return {
        "Message": "Hello from docker FastAPI!"
    }

@app.get("/names",)
def root():
    return {
        "success": True,
        "data": db,
        "message": "Names retieved successfully"
    }

@app.get("/names/{id}")
def get_student_name(id: int):
    if id not in db:
        raise HTTPException(status_code=404, detail="Name not found")
    return {"id": id, "name": db[id]}




@app.post("/names", status_code=status.HTTP_201_CREATED)
def add_student(data: Dict[str, str]):
    new_id = int(data["id"])
    new_name = data["name"]

    if new_id in db:
        raise HTTPException(status_code=400, detail="ID already exists")

    db[new_id] = new_name
    return {
        "success": True,
        "message": "New name added successfully",
        "data": {new_id: new_name}
    }