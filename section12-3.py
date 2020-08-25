# section 12-3
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 데이터 수정 및 삭제

import sqlite3

# DB생성 (파일)
conn = sqlite3.connect("./resource/database.db", isolation_level=None)

# Cursor 연결
c = conn.cursor()

# 데이터 수정1
# c.execute("update users set username = ? where id = ?", ("niceman", 2))

# # 데이터 수정2
# c.execute("update users set username = :name where id = :id",
#           {"name": "goodman", "id": 5})

# # 데이터 수정3
# c.execute("update users set username = '%s' where id = '%s'" % ("badboy",3))

# conn.commit()

# 중간 데이터 확인1
for user in c.execute("select * from users"):
    print(user)

# row delete1
c.execute("delete from users where id = ?", (2,))

# row delete2
c.execute("delete from users where id = :id", {"id": 5})

# row delete3
c.execute("delete from users where id = '%s'" % 4)

# 중간 데이터 확인2
for user in c.execute("select * from users"):
    print(user)

# 테이블 전체 데이터 삭제
print("user db deleted :", conn.execute("delete from users").rowcount, "rows")

# 접속 해제
conn.close()
