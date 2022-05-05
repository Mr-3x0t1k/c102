import cv2
from cv2 import VideoCapture
def takeSnapShot():
    video_capture = cv2.VideoCapture(0)
    result = True
    while (result):
        ret, frame = video_capture.read()
        cv2.imwrite("picture.jpg", frame)
        result = False
    video_capture.release()
    cv2.destroyAllWindows()

takeSnapShot()