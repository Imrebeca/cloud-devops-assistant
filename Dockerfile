
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir torch==2.15.0 --index-url https://download.pytorch.org/whl/cpu

RUN pip install --no-cache-dir -r requirements.txt

COPY knowledge_base/ ./knowledge_base/
COPY src/ ./src/

CMD ["python", "-m", "src.main"]
