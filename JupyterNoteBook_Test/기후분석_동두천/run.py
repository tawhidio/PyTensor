import csv
import matplotlib.pyplot as plt

f = open('seoul.csv', 'r', encoding='cp949') # csv 파일을 읽기전용으로 인코딩은 cp949 형식으로
data = csv.reader(f, delimiter=',')                      # csv를 ',' 구분자로 읽어와 data 변수에 치환
header = next(data)

print(header)

max_dig = -999
max_dig_date = ''

for row in data :                           # data 값을 row에 치환하여 반복
    if row[4] != '' :
        if max_dig < float(row[4]) :
            max_dig_date = row[0]
            max_dig = float(row[4])

    print(row)                              # 출력
f.close()                                   # 파일 모두 출력후 파일닫기                                             # 출력후 csv파일 닫아주고 끝낸다.

print("max dig : ", max_dig, "date 한글: " + max_dig_date)

plt.plot([1, 2, 3, 4], [30, 10, 40, 20])
plt.show()
 