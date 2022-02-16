FROM python:3.9-bullseye

WORKDIR /home

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
RUN mkdir ./json
RUN echo "{}" > ./json/users.json

ENTRYPOINT ["python", "app.py"]
