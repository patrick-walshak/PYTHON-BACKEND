FROM python:3.11-slim

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

# "uvicorn" #The engine that starts your FastAPI API and keeps it running. (Starts FastAPI)
# "--host""0.0.0.0", It means “listen on all available network interfaces,” so any device that reaches your server can connect. (Locate your FastAPI instance
# in app.py)
#  8000   The specific port number where your app listens for incoming HTTP requests.
#  "--port" This tells Uvicorn which port number to use for your API.(Run the API on port 8000)