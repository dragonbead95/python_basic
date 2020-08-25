# section 12-2
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3

# DB파일 조회(없으면 새로 생성)
conn = sqlite3.connect("./resource/database.db")  # 본인 db경로

# 커서 바인딩
c = conn.cursor()

# 데이터 조회
c.execute("select * from users")
"""
# 커서 위치가 변경
# 1개 행 선택
print("one -> \n", c.fetchone())

# 지정로우 선택
print("three -> \n", c.fetchmany(size=3))

# 전체 로우 선택
print("All -> \n", c.fetchall())
print("All -> \n", c.fetchall())
"""
print()
# retrieve : 검색

# 순회1
# rows = c.fetchall()
# for row in rows:
#     print("retrieve1 > ", row)

# 순회2
# 보통 순회 2와 같은 방법을 사용한다.
# for row in c.fetchall():
#     print("retrieve1 > ", row)

# 순회3
# 단점 : 가독성이 떨어짐
# for row in c.execute("select * from users order by id"):
#     print("retrieve1 > ", row)

print()

# where retrieve1
param1 = (3,)
c.execute("select * from users where id=?", param1)
print("param1", c.fetchone())
print("param1", c.fetchall())

# where retrieve2
param2 = 4
c.execute("select * from users where id='%s'" % param2)
print("param2", c.fetchall())


# where retrieve3
c.execute("select * from users where id=:Id", {"Id": 5})
print("param3", c.fetchall())

# where retrieve4
param4 = (3, 5)
c.execute("select * from users where id in(?,?)", param4)
print("param4", c.fetchall())

# where retrieve5
c.execute("select * from users where id in('%d','%d')" % (3, 4))
print("param5", c.fetchall())

# where retrieve6
c.execute("select * from users where id=:id1 or id=:id2", {"id1": 2, "id2": 5})
print("param6", c.fetchall())


# dump 출력
# dump란 데이터베이스를 백업하는 것
with conn:
    with open("./resource/dump.sql","w") as f:
        for line in conn.iterdump():
            f.write("%s\n" % line)
        print("Dump Print Complete")

# f.close(), conn.close() 이 자동 호출되어 수행된다.
