# section09
# 파일 읽기 쓰기
# 읽기모드 r, 쓰기모드(기존파일 삭제) w, 추가모드(파일 생성 또는 추가) a
# 기타 : https://docs.python.org/3.7/library/functions.html#open


# 파일 읽기
# 예제1
from random import randint
f = open("./resource/review.txt", "r")
content = f.read()
print(content)
print(dir(f))
# 완료시 close 리소스 반환
f.close()

print("/////////////////////////////////")
# 예제2
with open("./resource/review.txt", "r") as f:
    content = f.read()
    print(content)
    print(list(content))
    print(iter(content))

    print("/////////////////////////////////")
    print("/////////////////////////////////")

with open("./resource/review.txt", "r") as f:
    for c in f:
        # print(c)
        print(c.strip())

with open("./resource/review.txt", "r") as f:
    content = f.read()
    print(">", content)
    content = f. read()
    print(">", content)

    print("/////////////////////////////////")
    print("/////////////////////////////////")
with open("./resource/review.txt", "r") as f:
    line = f.readline()
    # print(line)
    while line:
        print(line, end=" ##### ")
        line = f.readline()

    print("/////////////////////////////////")
    print("/////////////////////////////////")
# 예제6
with open("./resource/review.txt", "r") as f:
    contents = f.readlines()
    print(contents)
    for c in contents:
        print(c, end=" ***** ")

print()
# 예제7
with open("./resource/score.txt", "r") as f:
    score = []
    for line in f:
        score.append(int(line))
    print(score)

    print("avg : {:6.3}".format(sum(score)/len(score)))

# 파일 쓰기
# 예제1
with open("./resource/text1.txt", "w") as f:
    f.write("niceman!")

# 예제2
with open("./resource/text1.txt", "a") as f:
    f.write("goodman")


# 예제3
with open("./resource/text2.txt", "w") as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write("\n")

# 예제4
# writelines : 리스트 -> 파일로 저장
with open("./resource/text3.txt", "w") as f:
    list = ["Kim\n", "Park\n", "Lee\n"]
    f.writelines(list)
    """
    Kim
    Park
    Lee
    """

# 예제4
# writelines : 리스트 -> 파일로 저장
with open("./resource/text4.txt", "w") as f:
    print("text content!1", file=f)
    print("text content!2", file=f)
