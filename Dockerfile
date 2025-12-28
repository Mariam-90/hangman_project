FROM python:3.13-alpine

WORKDIR /app

COPY . /app

CMD ["python", "main_game.py"]
