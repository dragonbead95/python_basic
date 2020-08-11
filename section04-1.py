# 데이터 타입

import math
v_str1 = "GoodMan"
v_bool = True
v_str2 = "GoodBoy"
v_float = 10.3
v_int = 7
v_dict = {
    "name": "Kim",
    "age": 25
}

v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {3, 5, 7}

print(type(v_str1))
print(type(v_bool))
print(type(v_float))
print(type(v_tuple))
print(type(v_int))
print(type(v_dict))
print(type(v_list))
print(type(v_set))

i1 = 39
i2 = 939
big_int1 = 9999999999999999999999999999999999
big_int2 = 7777777777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5  # 0.5
f4 = 10.  # 10.0
print(i1*i2)
print(big_int1*big_int2)
print(f1**f2)  # 제곱
print(i2+f3)

a = 5.
b = 4
print(type(a), type(b))
result2 = a+b
print(result2, type(result2))

# 형변환
# int, float, complex(복소수)

print(int(result2))

c = 10
print(float(c))
print(complex(3))
print(int(True))
print(int(False))
print(int("3"))

# 수치연산함수
# https://docs.python.org/3/library/math.html
print(abs(-7))
n, m = divmod(100, 8)  # 몫, 나머지
print(n, m)

print(math.ceil(5.1))  # 천정 6
print(math.floor(3.874))  # 바닥 3
