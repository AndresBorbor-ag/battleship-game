FROM python:3.11-slim

WORKDIR /app

COPY battleship.py .

CMD ["python3", "battleship.py"]
