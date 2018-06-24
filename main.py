# -*- coding: utf-8 -*-

import stt
import tts
#from importlib import reload
import sys
import tel
from imp import reload
import json
import weather
import issue
import configparser
import datetime
import numpy as np
import sentence2vec
from os import listdir
from os.path import abspath, dirname
import builder
import sys
import new_music1
import weather

global person_emotion_music
person_emotion_music=""
person_emotion_musics={"music": "01.","person":"bumjun", "init_emotion":"neutral"}
person_emotion_music=json.dumps(person_emotion_musics)

#import new_music as mu

# warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

class Classifier:
    def __init__(self):
        self.s2v = sentence2vec.Sentence2Vec()
        self.model_set = []

        # Read neural network model from file.
        file_list = listdir(''.join([dirname(abspath(__file__)), '/model']))
        file_list.sort()
        for f in file_list:
            self.model_set.append(builder.ModelBuilder(f))

    def classify(self, input_sentence):
        # Convert input_sentence to vector using sentecne2vec.
        result = self.s2v.sentence2vec(input_sentence)
        words_vec = result[0]
        words_raw = result[1]
        input_vector = np.array(words_vec)

        result = np.array([])
        model_number = 1

        # Put pre-processed vector to neural network model.
        for model in self.model_set:
            status_1 = np.zeros([100])
            status_2 = np.zeros([100])
            for i in xrange(input_vector.shape[0]):
                prop, status_1, status_2 = model.run(input_vector[i, :], status_1, status_2)
            result = np.append(result, prop)
            print(''.join(['[iNa] Model', str(model_number), ' :: ', str(result[model_number - 1])]))
            model_number = model_number + 1

        max_index = np.argmax(result)

        # No answer in model
        if result[max_index] < 0.5:
            return 0, words_raw
        # Return argmax index
        else:
            return max_index + 1, words_raw


classifier = Classifier()

# ???
config = configparser.RawConfigParser()
config.read('config.ini')

#trans = u'음악 켜'
#reonse_number, words = classifier.classify(sentence)
#print("response_number: ", response_number)

#날씨 1
#이슈 2
#시간 3
#음악 켜 5
#음악 꺼 6

def function1():
    tmp, weather_status = weather.get_weather()
    print("log function1: ",weather_status)
    music = new_music1.getMusicByWeather(weather_status)
    #musics = music[0:-3]
    print("function1 music: ", music)
    tts.func_tts(tmp, i)
    output2 = ''
    output2 += '날씨에 맞는 노래를 추천드려요...'
    tts.func_tts(output2, 0)
    return music

def function2():
    return issue.get_issue()

def function3():
    now = datetime.datetime.now()
    print(u'지금은 {h}시 {m}분 입니다.'.format(h=now.hour, m=now.minute))
    return u'지금은 {h}시 {m}분 입니다.'.format(h=now.hour, m=now.minute)

def function4():
    return u'무슨 말을 하는 지 모르겠습니다.'

def function5():
    global person_emotion_music
    jsonString=new_music1.checkInitEmotion()
    person_emotion_music=jsonString
    dict = json.loads(jsonString)
    music_name=dict['music']
    music_name+="mp3"
    print(music_name)
    tel.sending(music_name)
    #tel.sending('01')

def getMusicSync():
    global person_emotion_music
    dict = json.loads(person_emotion_music)
    now_music=tel.receive()
    print("log getMusicSync: ",now_music)
    now_music_str=now_music[0:-3]
    print("log getMusicSync print dict: ",dict['person'],dict['init_emotion'])
    new_music1.recordMusic(dict['person'],dict['init_emotion'],now_music_str)

def getMusicSync2(music):
    global person_emotion_music
    dict = json.loads(person_emotion_music)
    print("log getMusicSync: ",music)
    print("log getMusicSync print dict: ",dict['person'],dict['init_emotion'])
    new_music1.recordMusic(dict['person'], dict['init_emotion'], music)

i= 0

tel.config()
global flag
flag=6
while(1):
    try:
        global flag
        trans = tel.receive()
        #만약 음악 이름이 오면 sync하고 continue
        if(trans.endswith(".mp3")):
            rec_mu = trans[0:3]
            #rec_mu += '.'
            print("trans: ", rec_mu)
            getMusicSync2(rec_mu)
            continue
        response_number, words = classifier.classify(trans)
        i = 0
        print("response number: ", flag)
        if(response_number==flag):
            print("Same Response Number")
            continue
        if response_number == 1:
            flag=1
            mu=function1()
            tel.sending(mu)
        elif response_number == 2:
            flag=2
            tts.func_tts(function2(), i)
        elif response_number == 3:
            flag=3
            tts.func_tts(function3(), i)
        elif response_number == 5:
            flag=5
            function5()
        elif response_number == 6:
            print("음악 꺼!")
        else:
            print("There is no matching number")

    except Exception as ex:
        print("err: main while error ",ex)
        break




tel.closeSocket()