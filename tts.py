# -*- coding: utf-8 -*-
import sys
from urllib2 import urlopen, Request
import pygame
from pygame import mixer, time
import os


# -*- coding: utf-8 -*-
import sys
from urllib2 import urlopen, Request
import pygame
from pygame import mixer, time
import os

reload(sys)
sys.setdefaultencoding('utf-8')

client_id = "mpjyXTwI7LBYsujU0yvU"
client_secret = "ugI8ewr17N"

def func_tts(input_sentence, i):
    #input
    #encText='안녕'
    encText=input_sentence
    #encText = raw_input('Please type in text : ').decode('euc-kr').encode('utf-8')
    #encText = raw_input('Please type in text : ')
    #윈도우 cmd 쉘에서 입력 받은 한글(\xc7\xd1\xb1\xdb)은 euc-kr로 되어 있는 것이고,
    #리눅스 bash 쉘에서 입력 받은 한글( \xed\x95\x9c\xea\xb8\x80)은 utf-8로 되어 있는 것이다.
    data = "speaker=mijin&speed=0&text=" + unicode(encText)

    q = Request("https://openapi.naver.com/v1/voice/tts.bin")
    q.add_header("X-Naver-Client-Id",client_id)
    q.add_header("X-Naver-Client-Secret",client_secret)

    response = urlopen(q, data=data.encode('utf-8'))
    rescode = response.getcode()

#    audiopath = 'audio.mp3'

    if(rescode==200):
#        print("TTS mp3 save")
        response_body = response.read()
        #audiopath = r'C:\Users\XNOTE\PycharmProjects\speech\Audio.mp3'
        #audiopath = 'Audio.mp3'
        str1 = 'audio' + str(i) + '.mp3'
        audiopath = os.path.join('/Users/soo/Downloads/emotion',str1)
        with open(audiopath, 'wb') as f:
            f.write(response_body)

        mixer.pre_init(44100, -16, 2, 256)
        mixer.init(frequency=16000, buffer=24000)
        pygame.init()
        mixer.music.load(audiopath)
        mixer.music.play(loops=1)

        while mixer.music.get_busy():
            time.Clock().tick(100)

        #f.close()
        #os.remove(audiopath)
        #print('close')

    else:
        print("Error Code:" + rescode)




