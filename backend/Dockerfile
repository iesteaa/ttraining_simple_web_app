FROM python:3.13-slim

WORKDIR /workspace/simple-web-app/backend

COPY requirements.txt ./requirements.txt
COPY requirements-dev.txt ./requirements-dev.txt
RUN pip install --no-cache-dir -r requirements-dev.txt

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
