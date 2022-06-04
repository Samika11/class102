import cv2
import dropbox
import time
import random
def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite("newpictureone.jpg",frame)
        result=False
    return img_name
    print("snapshotTaken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
take_snapshot()