# section 02-2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습

# import this
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print("My name is good boy")

# 변수
myname = "Good Boy!"

# 조건문
if myname == "Good Boy!":
    print("Ok")

# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print("%d * %d = " % (i, j), i*j)

# 변수선언
김 = "좋은사람"

print(김)

# 함수


def greeting():
    print("hello")


greeting()

# 클래스


class Cookie:
    pass


# 객체생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))
