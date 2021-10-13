import cv2, datetime


async def videoScreen(host, user_id):
    #TODO: Доделать проверку пинг
    capture = cv2.VideoCapture(f'http://{host}/')
    filename = host.split(":")[0]
    username = user_id

    endTime = datetime.datetime.now() + datetime.timedelta(seconds=10)
    while True:
        ret, frame = capture.read()
        if ret == True:
            if datetime.datetime.now() >= endTime:
                cv2.imwrite(f"screens/{filename}-{username}.png", frame)
                break
        else:
            break

    capture.release()
