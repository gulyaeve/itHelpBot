FROM python:3.9

WORKDIR /home

RUN pip install -U pip aiogram, requests && apt-get update
COPY . ./

ENTRYPOINT ["python", "app.py"]
