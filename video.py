import cv2
import datetime


def videoScreen(host, username, date):
    capture = cv2.VideoCapture(f'http://{host}/')
    filename = host.split(":")[0]
    endTime = datetime.datetime.now() + datetime.timedelta(seconds=3)
    while True:
        ret, frame = capture.read()
        if ret:
            if datetime.datetime.now() >= endTime:
                cv2.imwrite(f"screens/VLC-{filename}-{username}-{date}.png", frame)
                break
        else:
            break

    capture.release()


def videoScreen2(host, username, date):
    capture = cv2.VideoCapture(f'rtsp://admin:admin123@{host}:554/')
    filename = host
    endTime = datetime.datetime.now() + datetime.timedelta(seconds=3)
    while True:
        ret, frame = capture.read()
        if ret:
            if datetime.datetime.now() >= endTime:
                cv2.imwrite(f"screens/ЕЦХД-{filename}-{username}-{date}.png", frame)
                break
        else:
            break

    capture.release()


def videoCap(host, username, date):
    filename = host.split(":")[0]

    cap = cv2.VideoCapture(f'http://{host}/')
    cap.set(3,640)
    cap.set(4,480)

    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(f"videos/{filename}-{username}-{date}.mp4", fourcc, 5.0, (640,480))

    endTime = datetime.datetime.now() + datetime.timedelta(seconds=5)

    while True:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            if datetime.datetime.now() >= endTime:
                break

    cap.release()
    out.release()
