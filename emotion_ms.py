import cognitive_face as CF
import httplib2
import base64
import json
import numpy as np
import requests
import http
import urllib

####################################
#####################################################

KEY = '7e52b7f1c2914ed2b360a85d81b92d8e'
key = '6d199a527b2b4a248cc886f142ba6c98'

BASE_URL2 = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'
CF.BaseUrl.set(BASE_URL2)

#img_url = 'http://how-old.net/Images/faces2/main007.jpg'

#pathToFileInDisk = r'/Users/soo/Desktop/park.png'
#pathToFileInDisk='/Users/soo/Desktop/test.jpg'



def msEmotionAPI(pathToFileInDisk):
    with open( pathToFileInDisk, 'rb' ) as f:
        data = f.read()

    #img_urls='/Users/soo/Desktop/park.png'
    #img_urls2='/Users/soo/Desktop/insideout.png'

    headers={'Content-Type':'application/octet-stream', 'Ocp-Apim-Subscription-Key': KEY}
    params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'emotion',
    }

    response = requests.post(BASE_URL2, params=params, headers = headers,data=data)

    dict=response.json()

    #print(dict)

    return dict