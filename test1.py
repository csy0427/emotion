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


global person_emotion_music
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
    return weather.get_weather()

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
    tel.sending(music_name)

def getMusicSync():
    global person_emotion_music
    dict = json.loads(person_emotion_music)
    now_music=tel.receive()
    new_music1.recordMusic(dict['person'],dict['init_emotion'],now_music)

i = 0

while(1):
    trans = tel.receive()

