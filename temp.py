import pymysql
import db
db=pymysql.connect(user='root', password='12345', host='127.0.0.1', database='ina')
select_sql = "select * from user_emotion_music where user_id=%s and init_emotion_name=%s and score=(select MAX(score) from user_emotion_music)"
cursor=db.cursor()
cursor.execute(select_sql,('a','neutral'))

rs=cursor.fetchall()

for n in rs:
    print(n)

select_sql ="select MAX(score) from user_emotion_music"
cursor.execute(select_sql)

rs=cursor.fetchone()

print(rs)


cursor = db.cursor()

insert_sql = "insert into music values(%s)"
cursor.execute(insert_sql, 'usr1')
select_sql ="select * from music"
cursor.execute(select_sql)
rs=cursor.fetchone()

print(rs)

cursor.close()
db.commit()
db.close()