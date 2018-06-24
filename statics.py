# -*- coding: utf-8 -*-
# !/usr/bin/python3.5
# emotion api
import emotion_ms as ms
import emotion_faceplus as f
import emotion_google as g
#------------
import operator
import cv2
import time
import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
from tkinter import *
import shutil
import tkinter.messagebox
# face - master
import recognize
import train
import config
import detect
#----------
CAM_ID = 0

faceSize=config.DEFAULT_FACE_SIZE
recognizer = train.trainRecognizer('imgdb', faceSize, showFaces=True)

def RecognizeFace(image, faceCascade, eyeCascade, faceSize, threshold):
    global label
    found_faces = []

    gray, faces = detect.detectFaces(image, faceCascade, eyeCascade, returnGray=1)

    # If faces are found, try to recognize them
    for ((x, y, w, h), eyedim)  in faces:
        label, confidence = recognizer.predict(cv2.resize(detect.levelFace(gray, ((x, y, w, h), eyedim)), faceSize))
        # note that for some distributions of python-opencv, the predict function
        # returns the label only.
        #label = recognizer.predict(cv2.resize(detect.levelFace(gray, ((x, y, w, h), eyedim)), faceSize))
        #confidence = -1
        if confidence < threshold:
            found_faces.append((label, confidence, (x, y, w, h)))

    return found_faces


def capture(camid=CAM_ID):
    cv2.namedWindow("my webcam")
    cam = cv2.VideoCapture(camid)
    if cam.isOpened() == False:
        print('cant open the cam (%d)' % camid)
        return None

    faceCascade = cv2.CascadeClassifier(config.FACE_CASCADE_FILE)
    eyeCascade = cv2.CascadeClassifier(config.EYE_CASCADE_FILE)
    faceSize = config.DEFAULT_FACE_SIZE
    threshold = 500

#    recognizer = train.trainRecognizer('imgdb', faceSize, showFaces=True)

    while (cam.isOpened()):
        human = False
        ret, frame = cam.read()
        if frame is None:
            print('frame is not exist')
            return None

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        for (label, confidence, (x, y, w, h)) in RecognizeFace(frame, faceCascade, eyeCascade, faceSize, threshold):
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "{} = {}".format(recognizer.getLabelInfo(label), int(confidence)), (x, y),
            cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1, cv2.LINE_AA)
            human = True

        cv2.imshow('my webcam', frame)

        if cv2.waitKey(10) == 27:
            if human is True:
                cv2.imwrite('/Users/soo/Downloads/emotion/Picture/tt.jpg', frame, params=[cv2.IMWRITE_JPEG_QUALITY, 100])
                cv2.destroyAllWindows()
                cam.release()
                break
# 출력값은 recognizer.getLabelInfo(label) == 이름 , int(confidence) == 수치
    return human, recognizer.getLabelInfo(label)

def emotion():
    while (True):
        capture()
        print('Sending Pictures.....')
        picturePath = '/Users/soo/Downloads/emotion/Picture/tt.jpg'
        print('receive MS result....')
        #dict = ms.msEmotionAPI(picturePath)
        print('MS')
        print('receive Faceplus result....')
        face1 = f.faceplusEmotionAPI(picturePath)
        print('FP')
        #print(face1)

        pic = face1['faces']

        anger = 0
        happiness = 0
        sadness = 0
        neutral = 0
        isperson = True

        #if not dict:
        #    isperson = False
        print('receive Google result....')
        faces = g.detect_faces(picturePath)
        print('Google')

        #for i in dict:
        #    s = i['faceAttributes']
        #    pic = s['emotion']
        #    anger += pic['anger']
        #    anger += pic['disgust']
        #    happiness += pic['happiness']
        #    sadness += pic['sadness']
        #    neutral += pic['neutral']

        for i in pic:
            s = face1['faces']
            for j in s:
                t = j['attributes']
                k = t['emotion']
                anger += k['anger']
                anger += k['disgust']
                happiness += k['happiness']
                sadness += k['sadness']
                neutral += k['neutral']

        likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                           'LIKELY', 'VERY_LIKELY')

        for face in faces:
            anger += (face.anger_likelihood * 20)
            happiness += (face.joy_likelihood * 20)
            sadness += (face.sorrow_likelihood * 20)

        if isperson:
            anger /= 3
            happiness /= 3
            sadness /= 3
            neutral /= 2

            dict = {'anger': anger, 'happiness': happiness, 'sadness': sadness, 'neutral': neutral}

            print('************************************')
            print(max(dict.items(), key=operator.itemgetter(1))[0])
            print('************************************')
            return str(max(dict.items(), key=operator.itemgetter(1))[0])

        else:
            print('not person')




def emotion2(flag):
    while (True):
        capture()
        print('Sending Pictures.....')
        picturePath = '/Users/soo/Downloads/emotion/Picture/tt.jpg'
        print('receive MS result....')
        #dict = ms.msEmotionAPI(picturePath)
        print('MS')
        print('receive Faceplus result....')
        face1 =" "
        #if(flag==1):
            #face1 = f.faceplusEmotionAPI(picturePath)
        #else:
            #face1=f.faceplusEmotionAPI2(picturePath)
        #print('FP')
        #print(face1)

        #pic = face1['faces']

        anger = 0
        happiness = 0
        sadness = 0
        neutral = 0
        isperson = True

        #if not dict:
        #    isperson = False
        print('receive Google result....')
        faces = g.detect_faces(picturePath)
        print('Google')

        #for i in dict:
        #    s = i['faceAttributes']
        #    pic = s['emotion']
        #    anger += pic['anger']
        #    anger += pic['disgust']
        #    happiness += pic['happiness']
        #    sadness += pic['sadness']
        #    neutral += pic['neutral']
        '''
        for i in pic:
            s = face1['faces']
            for j in s:
                t = j['attributes']
                k = t['emotion']
                anger += k['anger']
                anger += k['disgust']
                happiness += k['happiness']
                sadness += k['sadness']
                neutral += k['neutral']
        '''
        likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                           'LIKELY', 'VERY_LIKELY')

        for face in faces:
            anger += (face.anger_likelihood * 20)
            happiness += (face.joy_likelihood * 20)
            sadness += (face.sorrow_likelihood * 20)

        if isperson:
            anger /= 3
            happiness /= 3
            sadness /= 3
            neutral /= 2

            dict = {'anger': anger, 'happiness': happiness, 'sadness': sadness, 'neutral': neutral}

            print('************************************')
            print(max(dict.items(), key=operator.itemgetter(1))[0])
            print('************************************')
            return str(max(dict.items(), key=operator.itemgetter(1))[0])

        else:
            print('not person')

