FROM python:3.12-slim

WORKDIR /mcp_prueba

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

COPY . .

CMD ["python","main.py"]
    