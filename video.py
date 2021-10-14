import cv2
import datetime
from loader import bot
from aiogram.types import InputFile


def videoScreen(host, username, date):
    capture = cv2.VideoCapture(f'http://{host}/')
    filename = host.split(":")[0]

    endTime = datetime.datetime.now() + datetime.timedelta(seconds=1)
    while True:
        ret, frame = capture.read()
        if ret:
            if datetime.datetime.now() >= endTime:
                cv2.imwrite(f"screens/{filename}-{username}-{date}.png", frame)
                break
        else:
            break

    capture.release()
    # await bot.send_photo(username, InputFile(f"screens/{filename}-{username}.png"))
