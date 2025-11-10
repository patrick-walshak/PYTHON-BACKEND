# Configure your database engine and session management using SQLAlchemy or SQLModel.

from sqlmodel import create_engine, Session, SQLModel
import os

DATABASE_URL = os.getenv("DATABSE_URL")

engine = create_engine(DATABASE_URL)

def creat_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session