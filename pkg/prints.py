def prt1():
    print("I'm Niceboy!")


def prt2():
    print("I'm Goodboy!")

# 단위 실행 (독립적으로 파일 실행)


# section08에서 호출시 pkg.prints로 출력
# prints.py에서 호출시 __main__로 출력
if __name__ == "__main__":
    prt1()
    prt2()
