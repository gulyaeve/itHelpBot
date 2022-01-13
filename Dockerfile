FROM python:3.9

WORKDIR /home

ENV TELEGRAM_API_TOKEN=""

RUN pip install -U pip aiogram && apt-get update
COPY . ./

ENTRYPOINT ["python", "app.py"]
