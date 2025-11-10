    🏀👿🏀# creat an endpoit to get user task using the user name
from fastapi import FastAPI, HTTPException, status
from typing import List
from pydantic import BaseModel

app = FastAPI()

id = 1
class TaskCreate(BaseModel):
    title: str
    content: str
    username: str

class Task(TaskCreate):
    id: int🏀
    is_completed: bool


@app.post("/tasks")
def create_task(task: TaskCreate):
    if not task.title or not task.description or not task.username:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="All fields are required"
        )

    global id
    new_task = Task(
        id=id,
        title=task.title,
        content=task.content,
        username=task.username,
    )

  

    return {
        "success": True,
        "data": new_task,
        "message": "Task created successfully"
    }

@app.get("/tasks/{username}")
def get_user_tasks(username: str):
    user_tasks = [task for task in task_instance._tasks if task.username == username]

    if not user_tasks:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found or no tasks available"
        )

    return {
        "username": username,
        "total_tasks": len(user_tasks), 
        "tasks": user_tasks
    }

# go and learn about sort and implement it in your work
