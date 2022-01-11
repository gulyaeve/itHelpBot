FROM python:3.9

WORKDIR /home

ENV TELEGRAM_API_TOKEN="482531669:AAF5r21uasPUs3aqMVE81q9nev2-VF4suUg"

RUN pip install -U pip aiogram opencv-python && apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
COPY . ./

ENTRYPOINT ["python", "app.py"]