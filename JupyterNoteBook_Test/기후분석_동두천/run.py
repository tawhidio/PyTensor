import csv

f = open('ta_20201208150322.csv', 'r', encoding='cp949') # csv 파일을 읽기전용으로 인코딩은 cp949 형식으로
data = csv.reader(f, delimiter=',')                      # csv를 ',' 구분자로 읽어와 data 변수에 치환

for row in data : {                                      # data를 row에 담아 반복문으로 한줄식 출력
    print(row)                                           # 화면에 출력
}

f.close()                                                # 출력후 csv파일 닫아주고 끝낸다.
