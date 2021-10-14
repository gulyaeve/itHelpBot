import cv2
import datetime


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
