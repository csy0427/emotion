# -*- coding: utf-8 -*-
# !/usr/bin/python3.5
import cv2

CAM_ID = 0


def capture(camid=CAM_ID):
    cv2.namedWindow("my webcam")
    cam = cv2.VideoCapture(camid)
    if cam.isOpened() == False:
        print('cant open the cam (%d)' % camid)
        return None

    face_cascade = cv2.CascadeClassifier()
    face_cascade.load('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')

    while (cam.isOpened()):
        human = False
        ret, frame = cam.read()
        if frame is None:
            print('frame is not exist')
            return None

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        # big number can detect small face
        faces = face_cascade.detectMultiScale(gray, 1.2, 2, 0, (30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3, 4, 0)
            human = True;

        cv2.imshow('my webcam', frame)

        if human == True:
            cv2.imwrite('tt.jpg', frame, params=[cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.destroyAllWindows()
            cam.release()
            break

        human = False
    return

