# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def get_issue():
    req = requests.get("https://www.naver.com/")  # connection
    html = req.text  # 소스 가져오기

    soup = BeautifulSoup(html, 'html.parser')
    sillsigan = soup.select('div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li')
    # 실시간 검색어 부분 copy select

    b = []
    for sill in sillsigan:
        b.append(sill.text)  # 태그 내 문자열을 b리스트에 추가

    k = 1
    list_sillsigan = []
    cnt=0
    for i in b:  # 문자열에서 핵심 문자열만 list_sillsigan 리스트에 추가
        cnt += 1
        if cnt > 10:
            break
        if k > 9:
            list_sillsigan.append(i[5:-2])
        else:
            list_sillsigan.append(i[4:-2])
        k += 1

    output='실시간 검색어는 ,'
    for s, list in enumerate(list_sillsigan):
        # enumerate를 이용하면 s는 개수를 셀 수 있고 list는 리스트 요소에 접근 가능
#        print (list)  # 출력
        output += list +', '
    output += '입니다.'

    print(output)
    return output

