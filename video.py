import cv2, datetime

def videoScreen(host):

    captura = cv2.VideoCapture(f'http://{host}/')
    filename = host.split(":")[0]

    endTime = datetime.datetime.now() + datetime.timedelta(seconds=5)
    while True:
        ret, frame = captura.read()
        if datetime.datetime.now() >= endTime:
            cv2.imwrite(f"screens/{filename}.png", frame)
            break

    captura.release()
    cv2.destroyAllWindows()