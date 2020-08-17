# Section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명(parameter):
# code

# 함수 호출
# 함수명() or 함수명(parameter)

# 예제1
def hello(world):
    print("hello", world)


hello("python")

# 예제2


def hello_return(world):
    val = "Hello " + str(world)
    return val


str = hello_return("python!!")
print(str)

# 예제3(다중리턴)


def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3


val1, val2, val3 = func_mul(10)
print(val1, val2, val3)

# 예제4(데이터 타입 반환)


def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


lt = func_mul(10)
print(lt)

# 예제5
# *args, *kwargs

# 가변 함수


def args_func(*args):
    print(type(args))
    print(args)
    # for t in args:
    #    print(t, end=" ")
    for i, v in enumerate(args):
        print(i, v)  # index value

    for i, v in enumerate(range(1, 11)):
        print(i, v)  # index value


args_func("kim")
args_func("kim", "park")
args_func("kim", "park", "Lee")


# kwargs
def kwargs_func(**kwargs):
    print(kwargs)  # {"name1":"kim", "name2":"Park"}

    for k, v in kwargs.items():
        print(k, v)


kwargs_func(name1="kim", name2="Park")

# 전체 혼합
# args, kwargs는 선택적 가변 매개변수


def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)


example_mul(10, 20)
example_mul(10, 20, "park", "kim")
example_mul(10, 20, "park", "kim", age1=24, age2=26)

# 중첩함수 (클로저)


def nested_func(num):
    # 중첩함수 선언부, 실행x
    def func_in_func(num):
        print(num)
    # 실행은 이부분에서 실행
    print("in func")
    func_in_func(num+10000)


nested_func(10000)

# 예제6
# int형을 입력받아 list형을 반환한다.
# 힌트를 알려준다.


def func_mul(x: int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


print(func_mul(5))

# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당


def mul_10(num: int) -> int:
    return num*10


var_func = mul_10  # 메모리 할당
print(var_func)
print(type(var_func))

print(var_func(10))  # 일반적인 함수 호출


def lambda_mul_10(num): return num*10


print(">>>", lambda_mul_10(10))


def func_final(x, y, func):
    print(x*y*func(10))


func_final(10, 10, lambda_mul_10)

print(func_final(10, 10, lambda x: x*10))
