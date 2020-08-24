# section 11
# 파이썬 외부 파일 처리
# 파이썬 엑셀 csv 파일 읽기 및 처리

# csv: MIME - text/ csv

import pandas as pd
import csv
# 예제 1
with open("./resource/sample1.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # header skip

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))

    for c in reader:
        print(c)

# 예제 2
with open("./resource/sample2.csv", "r") as f:
    reader = csv.reader(f, delimiter="|")
    next(reader)  # header skip

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))

    for c in reader:
        print(c)

# 예제3 (Dict 변환)

# 예제 1
with open("./resource/sample1.csv", "r") as f:
    reader = csv.DictReader(f)
    # for c in reader:
    #    print(c)
    """
    {'번호': '1', '이름': '김정수', '가입일시': '2017-01-19 11:30:00', '나이': '25'}
    {'번호': '2', '이름': '박민구', '가입일시': '2017-02-07 10:22:00', '나이': '35'}
    """

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print("--------------------")

# 예제4
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
with open("./resource/sample3.csv", "w", newline="") as f:
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)

# 예제5
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
with open("./resource/sample4.csv", "w", newline="") as f:
    wt = csv.writer(f)

    wt.writerows(w)

# XSL, XLSX
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# pandas 를 주로 사용
# pip install xlrd
# pip install openpyxl
# pip install

# sheetname="시트명" 또는 숫자, header=숫자, skirow=숫자
xlsx = pd.read_excel("./resource/sample.xlsx")

# 상위 데이터 확인
print(xlsx.head())
print()

# 데이터 확인
print(xlsx.tail())

# 데이터 확인
print(xlsx.shape)  # output : (20, 7 ) ->행 열

# 엑셀 or csv 다시 쓰기
xlsx.to_excel("./resource/result.xlsx", index=False)
xlsx.to_csv("./resource/result.csv", index=False)
