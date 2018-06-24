#-*- coding: utf-8 -*-
import cognitive_face as CF
import base64
import json
import numpy as np
import requests
import http
import urllib
import base64

#################face plus plus#########################


KEY = '8Q3NOf4Bw1tawrhnUVUDDu9MrsBjFa8Y'
SECRET_KEY='Qjtktivzji_UlmMntJMyE5BGIVnTqTf-'
#pathToFileInDisk='/Users/soo/Desktop/test.jpg'
#pathToFileInDisk = r'/Users/soo/Desktop/park.png'
# 자동으로 읽고 close 해줌



def faceplusEmotionAPI(pathToFileInDisk):
    with open( pathToFileInDisk, 'rb' ) as f:
        data = f.read()


    headers = {
        # Request headers
        'Content-Type': 'multipart/form-data',
        'Ocp-Apim-Subscription-Key': KEY

    }


    params=({
        'api_key' : KEY,
        'api_secret' : SECRET_KEY,
        #'image_file' : data,
        'return_attributes' : 'age,gender,smiling,skinstatus,beauty,emotion'

    })

    BASE_URL='https://api-us.faceplusplus.com/facepp/v3/detect'

    files ={ "image_file": data}
    response = requests.post(BASE_URL,params=params,files=files)

    ########

    ########
    face1 = response.json()
    print(face1)
    pic=''
    pic=face1['faces']

    #print(pic)
    return face1