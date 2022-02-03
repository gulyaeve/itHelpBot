FROM python:3.9

WORKDIR /home

RUN pip install -U pip aiogram && apt-get update
COPY . ./

ENTRYPOINT ["python", "app.py"]
