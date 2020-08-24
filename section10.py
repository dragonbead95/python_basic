# section 10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크,

# syntax error : 잘못된 문법
# print('test)
# if True
#    pass
# x=>y

# NameError : 참조변수없음
import time
a = 10
b = 15
# print(c)

# zerodivisionError : 0나누기 에러
# print(10/0)

# indexerror : 인덱스 범위 오버
x = [10, 20, 30]
print(x[0])
# print(x[3])


# key Error
dic = {"name": "kim", "Age": 35, "City": "Seoul"}
# print(dic["hbooy"])
print(dic.get("hobby"))

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외

print(time.time())
# print(time.month())

# valueError : 참조값이 없을대 발생
x = [1, 5, 9]
# x.remove(10)
# x.index(10)

# FileNotFoundError
# f = open("test.txt", "r")

# typeerror
x = [1, 2]
y = (1, 2)
z = "test"
# print(x+y)
# print(x+z)
# print(x+list(y)) #예외 형변환

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그후 런타임 예외 발생시 예외 처리 코딩 권장(EAFP 코딩 스타일)

# 예외 처리 기본
# try: 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# 예외1
name = ["Kim", "Lee", "Park"]
try:
    z = "Kim"
    x = name.index(z)
    print("{} Found it! in name".format(z, x+1))
except ValueError:
    print("Not found it! - Occurred ValueError!")
else:
    print("Ok! else!")

# 예외2
try:
    z = "Jho"
    x = name.index(z)
    print("{} Found it! in name".format(z, x+1))
except:
    print("Not found it! - Occurred ValueError!")
else:
    print("Ok! else!")


# 예외3
try:
    z = "Jho"
    x = name.index(z)
    print("{} Found it! in name".format(z, x+1))
except:
    print("Not found it! - Occurred ValueError!")
else:
    print("Ok! else!")
finally:
    print("finally ok")

# 예외4
# 예외처리는 하지 않지만, 무조건 수행되는 코딩 패턴
try:
    print("try")

finally:
    print("finally ok")

# 예외5
try:
    z = "Jho"
    x = name.index(z)
    print("{} Found it! in name".format(z, x+1))
except ValueError as l:
    print(l)
    print("Not found it! - Occurred ValueError!")
except IndexError:
    print("Not found it! - Occurred IndexError!")
except:
    print("Not found it! - Occured except")
else:
    print("Ok! else!")
finally:
    print("finally ok")

# 예제6
# 예외발생 : raise
# raise 키워드로 에외 직접 발생
try:
    a = "3"
    if a == "Kim":
        print("Ok 허가!!")
    else:
        raise ValueError
except ValueError:
    print("ValueError!")
except Exception as f:
    print(f)
else:
    print("Ok")
