# section 02-1
# 파이썬 기초 코딩
# print 구문의 이해

# 기본 출력
print('hello python')
print("hello python")
print("""hello python""")
print('''hello python''')

print()

# separater 옵션 사용
# 사이값을 sep로 연결해줌
print('T', 'E', 'S', 'T', sep='')
print("2019", "02", "19", sep="-")
print("niceman", "google.com", sep="@")
print(1, 2, 3, 4, sep='')

# end 옵션 사용
# 두 라인이 다음 문장과 연결해줌
print("Welcome To", end=" ")
print("The black paradice", end=" ")
print("piano notes")

print()

# format 사용 [], {}, ()
print("{} and {}".format("You", "Me"))  # You and Me
# {}안에 번호를 넣어서 0번째, 1번째와 같이 매핑이 가능하다.
print("{0} and {1} and {0}".format("You", "Me"))  # You and Me and You

# 직관적으로 매핑이 가능하다.
print("{a} are {b}".format(a="You", b="Me"))

# %s : 문자 , %d : 정수 , #f : 실수
print("%s's favorite number is %d" % ("Eunki", 7))

# 5자리 정수, 4자리 정수와 소수점아래2자리
# {}를 이용해서 매핑이 가능
print("test1 : %5d, Price: %4.2f" % (123, 6534.123))
print("Test1 : {0: 5d}, Price: {1:4.2f}".format(123, 6534.123))
print("Test1 : {a: 5d}, Price: {b:4.2f}".format(a=123, b=6534.123))

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
"""

print("'You'")
print("\'You\'")
print('"You"')
print("""'You'""")
print('\\You\\\n')  # 2줄이 띄워짐
print("test")
print("\t\t\ttest")
