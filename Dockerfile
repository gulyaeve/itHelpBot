FROM python:3.9

WORKDIR /home

ENV TELEGRAM_API_TOKEN=""

RUN pip install -U pip aiogram opencv-python && apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
COPY . ./

ENTRYPOINT ["python", "app.py"]
