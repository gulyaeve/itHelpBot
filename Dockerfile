FROM python:3.10.2-slim-bullseye
ENV TZ="Europe/Moscow"

WORKDIR /src

COPY requirements.txt /src
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /src
#RUN mkdir ./json
#RUN echo "{}" > ./json/users.json
RUN mkdir /src/logs

#ENTRYPOINT ["python", "app.py"]
