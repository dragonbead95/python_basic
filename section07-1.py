# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성후 존재

# 선언
# class 클래스명:
# 함수
# 함수
# 함수

# 예제1
# 클래스 이름 작성규칙은 파스칼 코드를 따름
class UserInfo:
    def __init__(self, name):  # 클래스 초기화
        self.name = name

    def user_info_p(self):
        print("Name : ", self.name)


# 네임스페이스
user1 = UserInfo("kim")
user1.user_info_p()
user2 = UserInfo("Park")
user2.user_info_p()

print(id(user1))
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)

# 예제2
# self의 이해


class SelfTest:
    def function1():  # 클래스 메소드
        print("function1 called!")

    def function2(self):  # 인스턴스 메소드
        print(id(self))
        print("function2 called!")


self_test = SelfTest()
# function1은 self 인자가 없기 때문에 누구의 function1 함수인지 모름
# 다시말해 클래스 변수를 의미
# self_test.function1()

# 해결법은 다음과 같이 호출
SelfTest.function1()
self_test.function2()
print(id(self_test))
SelfTest.function2(self_test)

# 예제3
# 클래스 변수, 인스턴스 변수


class WareHouse:
    # 클래스 변수
    stock_num = 0

    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1

    def __del__(self):
        WareHouse.stock_num -= 1


user1 = WareHouse("Kim")
user2 = WareHouse("Park")
user3 = WareHouse("Lee")

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

# 클래스 네임스페이스, 클래스 변수(공유)
print(WareHouse.__dict__)
print(user1.stock_num)  # 3
