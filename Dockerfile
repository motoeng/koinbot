FROM python:3.12-alpine

WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3", "/app/telegrambot.py" ]
