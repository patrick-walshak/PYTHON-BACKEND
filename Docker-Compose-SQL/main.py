from fastapi import FastAPI, Depends
from database import create_db_and_tables, get_session
from .models import Hero 

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
async def root():
    return {"message": "FastAPI with SQL and Docker Compose!"}

# Add your API endpoints here, using get_session as a dependency
# @app.post("/heroes/")
# def create_hero(hero: Hero, session: Depends(get_session)):
#     session.add(hero)
#     session.commit()
#     session.refresh(hero)
#     return hero