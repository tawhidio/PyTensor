#!/usr/bin/env python
# coding: utf-8

# # 피마 인디언 당뇨병 예측

# In[1]:


import pandas as pd

df = pd.read_csv('./dataset/pima-indians-diabetes.csv', names=["Pregnant", "Plasma", "Pressure", "Thickness", "Insulin", "BMI", "Pedigree", "Age", "Class"])

print(df, "\n\n")             # 전체 데이타 출력 
print(df.info(), "\n\n")     # 데이타에 대한 입력정보 출력

# 데이타에대한 특징 정보들 자동산출 출력
# 샘플수, 평균, 표준편차, 최솟값, 백분위 25%, 50%, 75%의 최댓값 
print(df.describe(), "\n\n") 

# 특정정보만 출력
print(df[['Pregnant', 'Class']])


# In[2]:


# 데이터 가공
df_prt = df[['Pregnant', 'Class']].groupby(['Pregnant'],as_index=False).mean().sort_values(by='Pregnant',ascending=True)
print(df_prt)


# In[3]:


# 그래프로 표현하기
import matplotlib.pyplot as pl
import seaborn as sbn

pl.figure(figsize=(12, 12))

# heatmap() 함수는 두항목씩 짝을지어 각각 패턴의 변화를 관찰하는 함수
# 두항목의 패턴이 비슷하거나(같으면) 1 가깝다., 서로 다른방향이면 0 에 가깝다
# df.corr() : Pandas DataFrame이 제공되면 인덱스 / 열 정보가 열과 행에 레이블을 지정
# 아래 옵션값 순서는 상관없음
# linewidths : 가로세로를 나누는 경계 선의 두께
# vmax : 오른쪽 수직 바의 최댓값
# vmin : 오른쪽 수직 바의 최솟값
# cmap : 컬러맵 종류 설정(원하는 방식의 색깔)
# linecolor : 선 색깔
# annot : 그래프 셀위에 숫자 표시여부
# annot_kws : 셀위의 숫자 크기 설정
sbn.heatmap(df.corr(), linewidths='1', cmap="YlGnBu", annot=True, annot_kws = {"size" : 16})
pl.show()


# In[4]:


grid = sbn.FacetGrid(df, col='Class')
grid.map(pl.hist, 'Plasma', bins=10)
pl.show()


# In[5]:


# 파마 인디언 당뇨예측
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
import tensorflow as tf

# seed값 생성
np.random.seed(3)
tf.random.set_seed(3)

# 데이타 로드
dataset = np.loadtxt("./dataset/pima-indians-diabetes.csv", delimiter=",")
x = dataset[:,0:8]
y = dataset[:,8]

# 모델 설정
model = Sequential()
model.add(Dense(16,input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 모델 컴파일
model.compile(loss='binary_corrsentropy', optimizer='adam', metrics=['accuracy'])

# 모델 실행
model.fit(x, y, epochs=200, batch_size=10)

print("\n Accurary : %.4f" %(model.evaluate(x, y)[1]))

