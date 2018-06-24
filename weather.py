# -*- coding:utf-8 -*-
# pyowm을 이용하기위해 import 해줍니다.
import pyowm
import sys
import tts

# import music2

reload(sys)
sys.setdefaultencoding('utf-8')


def get_weather():
    # 자신의 API_Key로 OWM에 접근할수있도록 Global OWM Object를 만듭니다.
    API_Key = 'b82ba8580f453653b35e184ab7d9d4a6'
    owm = pyowm.OWM(API_Key)

    City_ID = 1835848
    obs = owm.weather_at_id(City_ID)

    # get_location은 지역에 대한 정보를 가져 옵니다.
    L = obs.get_location()
    City_name = L.get_name()
    # print('City_ID의 도시명은 ' + City_name + ' 입니다.')

    # get_weather는 기상정보에 대한 정보를 가져옵니다.
    W = obs.get_weather()
    Temp = W.get_temperature(unit='celsius')
    output = ''
    output += '오늘의 최고기온은 ' + str(Temp['temp_max']) + ' 도, '
    output += '최저기온은 ' + str(Temp['temp_min']) + ' 도, '
    output += '현재기온은 ' + str(Temp['temp']) + ' 도 입니다. '

    Status = W.get_status()
    Statusk = ''

    if (Status == 'Mist'):
        Statusk += u'안개'
    elif (Status == 'Rain'):
        Statusk += u'비가 오는 중'
    elif (Status == 'Haze'):
        Statusk += u'안개'
    elif (Status == 'Clouds'):
        Statusk += u'구름이 많은 날씨';
    elif (Status == 'Clear'):
        Statusk += u'맑음'
    elif (Status == 'Thunderstorm'):
        Statusk += u'천둥번개'
    # rain mist haze

    if (Statusk != ''):
        output += '현재날씨는 ' + Statusk + ' 입니다.'
    else:
        output += '현재날씨는 ' + Status + ' 입니다.'

    #output += '날씨에 어울리는 노래를 들려 드릴게요.'
    print(output)
    return output, Status

'''
out, st = get_weather()
tts.func_tts(out, 0)
output2=''
output2+= '날씨에 맞는 노래를 추천드려요...'
tts.func_tts(output2,0)'''