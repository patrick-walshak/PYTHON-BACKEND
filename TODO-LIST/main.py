from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
app = FastAPI(title="Todo list")

id = 1
class TaskCreate(BaseModel):
    title: str
    description: str

class Task(TaskCreate):
    id: int
    created_at: datetime
    updated_at: datetime
    is_completed: bool

class TaskUpdate(BaseModel):
    id: int
    title: Optional[str] = None
    description: Optional[str] = None

class Database:
    def __init__(self):
        self._task:List[Task] = []

    def add(self, task:Task ):
        self._task.append(task)

    def get_tasks(self):
        return self._task

task_instance = Database()
def generate_next_id():
    global id
    id += 1
# Endpoints

@app.get("/")
def index():
    return{
        "message": "Todo App"
    }

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    if not task.title or not task.description:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="All fields are required"
        )
    global id
    new_task = Task(
        title=task.title,
        description= task.description,
        id =id,
        created_at= datetime.utcnow(),
        updated_at=datetime.utcnow(),
        is_completed=False
    )
    generate_next_id()
    task_instance.add(task=new_task)

    return {
        "success": True,
        "data": new_task,
        "message": "Task created successfully"
    }

@app.get("/tasks")
def get_all_task():
   tasks =  task_instance.get_tasks()
   return{
       "data": tasks
   }

@app.patch("/tasks/")
def partial_update(task: TaskUpdate):
    if not task.title and not task.description:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="Atleast One field is required"
        )
    value_to_update = None
    flag = False
    if task.title:
        value_to_update = task.title
        flag=True
    else:
        value_to_update = task.description
    for  task_in_db in range(len(task_instance._task)):
        if task_instance._task[task_in_db].id == task.id:
            if flag:
                task_instance._task[task_in_db].description = value_to_update
            else:
                task_instance._task[task_in_db].title = value_to_update