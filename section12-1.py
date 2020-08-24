# section 12-1
# 파이썬 데이터베이스 연동 (SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print(now)

nowDateTime = now.strftime("%Y-%m-%d %H:%M:%S")
print("nowDateTime : {}".format(nowDateTime))
# sqlite3
print("sqlite3 version : {}".format(sqlite3.version))
print("sqlite3 sqite_version : {}".format(sqlite3.sqlite_version))


# db생성 & Auto commit(Rollback)
# isolation_level=None -> auto commit 적용
conn = sqlite3.connect("./resource/database.db", isolation_level=None)

# Cursor
c = conn.cursor()

print("Cursor Type : ", type(c))

# 테이블 생성 (Data Type : TEXT, NUMERIC, INTEGER, REAL, BLOB)
c.execute("create table if not exists users(id INTEGER primary key, \
            username text, email text, \
            phone text, website text, regdate text)")
try:
    # 데이터 삽입
    c.execute(
        "insert into users values(1,'Kim','Kim@naver.com','010-1234-5678','Kim.com',?)", (nowDateTime,))
    c.execute("insert into users(id, username, email, phone, website, regdate) values \
            (?,?,?,?,?,?)", (2, "Park", "Park@daum.net", "010-1111-1111", "Park.com", nowDateTime))

    # many 삽입

    userList = {
        (3, "Lee", "Lee@naver.com", "010-2222-2222", "Lee.com", nowDateTime),
        (4, "Cho", "Cho@naver.com", "010-3333-3333", "Cho.com", nowDateTime),
        (5, "Yoo", "You@naver.com", "010-4444-4444", "Yoo.com", nowDateTime)
    }

    c.executemany("insert into users(id, username, email, phone, website, regdate) \
                values(?,?,?,?,?,?)", userList)
except:
    print("unique constrant failed")
finally:
    pass


# 테이블 데이터 삭제
#conn.execute("delete from users")
#print("users db deleted : ", conn.execute("delete from users").rowcount)


# 커밋 : isolation_level= None 일 경우 오토커밋 적용
# conn.commit()

# conn.rollback()
conn.close()
