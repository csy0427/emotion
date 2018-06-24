# -*- coding: utf-8 -*-
import pymysql
import os

from mutagen.id3 import ID3

#db=pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')

select_sql=""
insert_sql=""
delete_sql=""
update_sql=""
sql=""
#cursor=db.cursor()

def getNumberOfUser():
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()

    sql="select count(*) from user";
    cursor = db.cursor()
    count=cursor.execute(sql)
    cursor.close()
    db.close()
    return count

def userSelect():
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()

    select_sql = "select * from user"
    cursor.execute(select_sql)
    rows = cursor.fetchall()
    print(rows)
    cursor.close()
    db.close()


def findUser(_user_name):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()

    select_sql="select user_name from user where user_name=%s"
    cursor.execute(select_sql,_user_name)
    id=cursor.fetchone()
    cursor.close()
    print("findUser id : ", id)
    db.close()
    if(id==None):
        return True
    return False

def userInsert(name):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()
    insert_sql = "insert into user values(%s,%s)"
    id=getNumberOfUser()+2
    print("userInsert: ", id)
    id=str(id)
    cursor.execute(insert_sql,(id,name))
    cursor.fetchall()
    userSelect()
    cursor.close()
    db.commit()
    db.close()

def userDelete(_name):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()

    delete_sql= "delete from user where user_name=%s"
    cursor.execute(delete_sql,_name)
    cursor.fetchall()
    userSelect()
    cursor.close()
    db.commit()
    db.close()

def userUpdate(original_name,modi_name):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()

    update_sql="update user set user_name=%s where user_name=%s"
    cursor.execute(update_sql,(modi_name,original_name))
    cursor.fetchall()

    userSelect()
    cursor.close()
    db.commit()
    db.close()

def findMusic(_name):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()
    print(_name)
    select_sql = "select * from music where music_name=%s"
    cursor.execute(select_sql,_name)
    music_name=cursor.fetchone()
    print("findMusic called: ",music_name)
    cursor.close()
    db.close()
    if(music_name==None):
        print('True')
        return True
    else:
        print('False')
        return False


def musicSelcet():
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()

    select_sql = "select * from music"
    cursor.execute(select_sql)
    rows = cursor.fetchall()
    print(rows)
    cursor.close()
    db.close()

def musicInsert(name):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()
    print("musicInsert: ", name)
    insert_sql="insert into music values(%s)"
    cursor.execute(insert_sql,name)

    musicSelcet()
    cursor.close()
    db.commit()
    db.close()

def musicUpdate(original_name,modi_name):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()

    update_sql="update music set music_name=%s where music_name=%s"
    cursor.execute(update_sql, (modi_name, original_name))
    musicSelcet()
    cursor.close()
    db.commit()
    db.close()

def musicDelete(_name):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()

    delete_sql = "delete from music where music_name=%s"
    cursor.execute(delete_sql, _name)
    musicSelcet()
    cursor.close()
    db.commit()
    db.close()

def emotionSelcet():
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()

    select_sql = "select * from emotion"
    cursor.execute(select_sql)
    rows = cursor.fetchall()
    print(rows)

    cursor.close()
    db.close()

def emotionInsert(_name):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()

    insert_sql = "insert into emotion values(%s)"
    cursor.execute(insert_sql, _name)
    emotionSelcet()

    cursor.close()
    db.commit()
    db.close()


def emotionUpdate(original_name,modi_name):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()

    update_sql = "update emotion set emotion_name=%s where emotion_name=%s"
    cursor.execute(update_sql, (modi_name, original_name))
    emotionSelcet()

    cursor.close()
    db.commit()
    db.close()

def emotionDelete(_name):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()

    delete_sql = "delete from emotion where emotion_name=%s"
    cursor.execute(delete_sql, _name)
    emotionSelcet()

    cursor.close()
    db.commit()
    db.close()

#####

def emotion_scoreSelcet():
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()

    select_sql = "select * from emotion_score"
    cursor.execute(select_sql)
    rows = cursor.fetchall()
    print(rows)

    cursor.close()
    db.close()

def emotion_scoreInsert(_name):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()

    insert_sql = "insert into emotion_score values(%s)"
    cursor.execute(insert_sql, _name)
    emotionSelcet()

    cursor.close()
    db.commit()
    db.close()


def emotion_scoreUpdate(original_name,score):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()

    update_sql = "update emotion_score set emotion_score=%s where emotion_name=%s"
    cursor.execute(update_sql, (score, original_name))
    emotionSelcet()

    cursor.close()
    db.commit()
    db.close()

def emotion_scoreDelete(_name):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()

    delete_sql = "delete from emotion_score where emotion_name=%s"
    cursor.execute(delete_sql, _name)
    emotionSelcet()

    cursor.close()
    db.commit()
    db.close()

#####


def user_emotionSelcet():
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()

    select_sql = "select * from user_emotion"
    cursor.execute(select_sql)
    rows = cursor.fetchall()
    print(rows)

    cursor.close()
    db.close()

def finduser_emotion(_name,emo_name):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()
    print(_name,emo_name)
    select_sql = "select user_id from user_emotion where user_id=%s and emotion_name=%s"
    cursor.execute(select_sql,(_name,emo_name))
    userid=cursor.fetchone()
    print("userid: ", userid)
    cursor.close()
    db.close()
    #when not exist
    if(userid==None):
        print('True')
        return True
    return False

def user_emotionInsert(emo_name,user_name):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()

    insert_sql = "insert into user_emotion(emotion_name,user_id,count_emotion) values(%s,%s,%s)"
    cursor.execute(insert_sql, (emo_name,user_name,1))
    user_emotionSelcet()
    cursor.close()
    db.commit()
    db.close()

def getCounts(original_name,emo_name):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()

    select_sql = "select count_emotion from user_emotion where user_id=%s and emotion_name=%s"
    cursor.execute(select_sql,(original_name,emo_name))
    cnt=cursor.fetchone()
    cursor.close()
    db.close()
    for i in cnt:
        return i


def user_emotionCountUpdate(original_name,emo_name):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()
    print('user_emotionCountUpdate')
    #print(original_name, emo_name)
    update_sql = "update user_emotion set count_emotion=%s where user_id=%s and emotion_name=%s"
    now_cnt=getCounts(original_name,emo_name)+1
    cursor.execute(update_sql, (now_cnt, original_name,emo_name))
    user_emotionSelcet()
    cursor.close()
    db.commit()
    db.close()

def user_emotionDelete(_name):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()

    delete_sql = "delete from user_emotion where user_id=%s"
    cursor.execute(delete_sql, _name)
    user_emotionSelcet()

    cursor.close()
    db.commit()
    db.close()


def user_emotion_musicSelcet():
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()

    select_sql = "select * from user_emotion_music"
    cursor.execute(select_sql)
    rows = cursor.fetchall()
    print(rows)

    cursor.close()
    db.close()

#해당 사용자가 해당 감정을 느낄때 틀어 줄수 있는 음악 데이터가 있는지 확인
def finduser_emotion_music(_name,emo_name):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()

    select_sql = "select music_name from user_emotion_music where user_id=%s and init_emotion_name=%s"
    cursor.execute(select_sql,(_name,emo_name))
    music_name=cursor.fetchone()
    print("music_name: ", music_name)
    print(music_name)
    cursor.close()
    db.close()
    if(music_name==None):
        return True
    return False

#해당 사용자가 해당 감정을 느낄때 해당 노래를 틀어준 데이터가 있으면 반환
def finduser_emotion_musicByMusicName(person, emotionstatus,cursongSub):
    db=pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor=db.cursor()
    select_sql = "select music_name from user_emotion_music where user_id=%s and init_emotion_name=%s and music_name=%s"
    cursor.execute(select_sql, (person,emotionstatus,cursongSub))
    music_name = cursor.fetchone()
    print("finduser_emotion_musicByMusicName music_name: ", music_name)
    cursor.close()
    db.close()
    if (music_name == None):
        return True
    return False


def findMusicuser_emotion_musicByMusicName(person, emotionstatus):
    db=pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor=db.cursor()
    select_sql = "select music_name from user_emotion_music where user_id=%s and init_emotion_name=%s"
    cursor.execute(select_sql, (person,emotionstatus))
    music_name = cursor.fetchall()
    print("findMusicuser_emotion_musicByMusicName music_name: ", music_name)
    cursor.close()
    db.close()
    return music_name


def user_emotion_musicInsert(user_id,emotion_name,music_name):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()
    print("user_emotion_musicInsert")
    insert_sql = "insert into user_emotion_music(user_id,init_emotion_name,music_name,score,count_emotion) values(%s,%s,%s,%s,%s)"
    cursor.execute(insert_sql, (user_id,emotion_name,music_name,0,1))
    user_emotion_musicSelcet()
    cursor.close()
    db.commit()
    db.close()

def getCountFromuser_emotion_music(original_name,emotion_name,music_name):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()
    print("getCountFromuser_emotion_music : ", original_name, emotion_name, music_name)
    select_sql ="select count_emotion from user_emotion_music where user_id=%s and init_emotion_name=%s and music_name=%s"
    cursor.execute(select_sql,(original_name,emotion_name,music_name))
    cnt1=cursor.fetchone()
    print("cnt1: ", cnt1)
    cnt2=cnt1[0]
    print("cnt2: ", cnt2)
    cursor.close()
    db.close()
    return cnt2


def getScoreAndMusicNameFromuser_emotion_music(person,emotion_name):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()
    print("getCountAndMusicNameFromuser_emotion_music : ", person, emotion_name)
    select_sql ="select music_name,score from user_emotion_music where user_id=%s and init_emotion_name=%s"
    cursor.execute(select_sql,(person,emotion_name))
    ans=cursor.fetchall()
    print("ans: ",ans)
    cursor.close()
    db.close()
    return ans


def getScore(original_name,emotion_name,music_name):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()

    select_sql = "select score from user_emotion_music where user_id=%s and init_emotion_name=%s and music_name=%s"
    cnt=cursor.execute(select_sql,(original_name,emotion_name,music_name))
    cursor.close()
    db.close()
    return cnt

def getMaxScore():
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()
    print('getMaxScore')
    select_sql = "select MAX(score) from user_emotion_music"
    cursor.execute(select_sql)
    rs = cursor.fetchall()
    for n in rs:
        print(n)
    cursor.close()
    db.close()
    return rs


def getMusicMaxScore(person,init_emotion):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()
    print('getMusicMaxScore', person, init_emotion)
    select_sql = "select MAX(score) from user_emotion_music where user_emotion_music.user_id=%s and user_emotion_music.init_emotion_name=%s"
    cursor.execute(select_sql,(person,init_emotion))
    _score=cursor.fetchone()
    select_sql = "select music_name from user_emotion_music where user_emotion_music.user_id=%s and user_emotion_music.init_emotion_name=%s and score=%s"
    cursor.execute(select_sql, (person, init_emotion,_score))
    rs = cursor.fetchall()
    for n in rs:
        print(n)
    cursor.close()
    db.close()
    return rs


def getMusicMinCount(person,init_emotion):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()
    print('getMusicMinCount ', person, init_emotion)
    select_sql = "select MIN(count_emotion) from user_emotion_music where user_emotion_music.user_id=%s and user_emotion_music.init_emotion_name=%s"
    cursor.execute(select_sql, (person, init_emotion))
    _score = cursor.fetchone()
    print("min score: ", _score[0])
    select_sql = "select music_name, count_emotion from user_emotion_music where user_emotion_music.user_id=%s and user_emotion_music.init_emotion_name=%s and count_emotion=%s"
    cursor.execute(select_sql, (person, init_emotion, _score))
    rs = cursor.fetchall()
    print("getMusicMinCount__: ",rs)
    for n in rs:
        print(n)
    cursor.close()
    db.close()
    return rs

def getMusicMaxCount(person,init_emotion):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()
    print('getMusicMaxCount', person, init_emotion)
    select_sql = "select MAX(count_emotion) from user_emotion_music where user_emotion_music.user_id=%s and user_emotion_music.init_emotion_name=%s"
    cursor.execute(select_sql, (person, init_emotion))
    _score = cursor.fetchone()
    print("max score: ",_score[0])
    select_sql = "select music_name, count_emotion from user_emotion_music where user_emotion_music.user_id=%s and user_emotion_music.init_emotion_name=%s and count_emotion=%s"
    cursor.execute(select_sql, (person, init_emotion, _score[0]))
    rs = cursor.fetchall()
    print("getMusicMaxCountmax__: ", rs)
    for n in rs:
        print(n)
    cursor.close()
    return rs

def getMusicMaxScoreArr(person,init_emotion):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()
    print('getMusicMaxScoreArr', person, init_emotion)
    select_sql = "select music_name from user_emotion_music where user_emotion_music.user_id=%s and user_emotion_music.init_emotion_name=%s"
    cursor.execute(select_sql,(person,init_emotion))
    _score=cursor.fetchone()
    select_sql = "select music_name, score from user_emotion_music where user_emotion_music.user_id=%s and user_emotion_music.init_emotion_name=%s and score=%s"
    cursor.execute(select_sql, (person, init_emotion,_score))
    rs = cursor.fetchall()
    for n in rs:
        print(n)
    cursor.close()
    db.close()
    return rs

def getCountAll(person,init_emotion):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()
    print('getCountAll',person ,init_emotion)
    select_sql="select music_name from user_emotion_music where user_emotion_music.user_id=%s and user_emotion_music.init_emotion_name=%s and count_emotion<5"
    cursor.execute(select_sql,(person,init_emotion))
    rs=cursor.fetchall()
    print(rs)
    return rs

def user_emotion_musicScoreUpdate(original_name,emo_name,music_name,_score):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()
    print('user_emotion_musicScoreUpdate: ')
    print(original_name, emo_name, music_name , _score)
    update_sql = "update user_emotion_music set user_emotion_music.score=%s where user_id=%s and init_emotion_name=%s and music_name=%s"
    cursor.execute(update_sql, (_score, original_name, emo_name, music_name))
    db.commit()
    now_cnt=getCountFromuser_emotion_music(original_name,emo_name,music_name)+1
    print("now_cnt: ", now_cnt)
    update_sql = "update user_emotion_music set user_emotion_music.count_emotion=%s where user_id=%s and init_emotion_name=%s and music_name=%s"
    cursor.execute(update_sql,(now_cnt,original_name,emo_name,music_name))
    db.commit()
    cursor.close()
    db.commit()
    db.close()


def increaseMusicCount(_name):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()
    db.close()
    update_sql="update "
    cursor.close()
    db.commit()
    db.close()

def user_emotion_musicDelete(_name):
    db = pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
    cursor = db.cursor()
    db.close()

    delete_sql = "delete from user_emotion_music where user_id=%s"
    cursor.execute(delete_sql, _name)
    user_emotion_musicSelcet()
    cursor.close()
    db.commit()
    db.close()



