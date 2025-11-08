from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_api():
    return {"Message": "Hello walshak form docker compose FastAPI"}

@app.get("/")
def read_us():
    return {"Message": "Hello walshak form docker compose FastAPI"}
