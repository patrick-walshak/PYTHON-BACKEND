
FROM python:3.11-slim


WORKDIR /app


COPY requirements.txt .

RUN pip install --default-timeout=100 -r requirements.txt

# Copy your application code
COPY . .

EXPOSE 8000
 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]