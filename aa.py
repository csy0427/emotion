#-*- coding:utf-8 -*-

import new_music1 as mu1
import json
import statics
import weather
import new_music1
import time
#import main

import tts
#main.function5()
#print('abcdefgsfjsdfjslfjska')
#global jsonString
#main.function5()

#tts.func_tts(weather.get_weather(),0)
new_music1.checkInitEmotion()

'''
main.function5()
main.getMusicSync2('55.')

tmp,weather_status=weather.get_weather()
print(weather_status)
music=new_music1.getMusicByWeather(weather_status)
musics=music[0:-3]
print("music: ",musics)


test='56 '
test.rstrip()
test.replace(" ","")
print(test)
test+='.'
print(test)
'''





'''
jsonString=mu1.checkInitEmotion()
print("log: jsonString: ",jsonString)
dict = json.loads(jsonString)
print("log: dict: ",dict)
music_name=dict['music']
print("log: music_name: ",music_name)

dict = json.loads(jsonString)
mu1.recordMusic(dict['person'],dict['init_emotion'],music_name)

str='53.mp3'
str1='5434342.mp3'
print(str)
print(str[0:-3])
print(str1[0:-3])

'''