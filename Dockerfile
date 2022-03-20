FROM python:3.10.2-slim-bullseye

WORKDIR /home

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
RUN mkdir ./json
RUN echo "{}" > ./json/users.json
RUN mkdir ./logs

ENTRYPOINT ["python", "app.py"]
