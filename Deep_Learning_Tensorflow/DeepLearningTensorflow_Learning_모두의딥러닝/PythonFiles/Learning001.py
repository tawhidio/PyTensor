#!/usr/bin/env python
# coding: utf-8

# # Deep Learning Tensorflow 시작
# ## 1. 폐암 수술 환자의 생존율 예측하기
# 
# 
# 

# In[1]:


# 케라스 함수 호출
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 계산을 위한 numpy 와 tensorflow 호출
import numpy as np
import tensorflow as tf

# 매 실행시 마다 같은 결과를 출력하기위한 설정
np.random.seed(3)
tf.random.set_seed(3)

# 수술 환자 데이터 호출
data_set = np.loadtxt("./dataset/ThoraricSurgery.csv", delimiter=",")
print(data_set)


# In[2]:


x = data_set[:,0:17]
print(x)
y = data_set[:,17]
print(y)


# In[3]:


# 모델 생성및 설정 
model = Sequential()
model.add(Dense(30, input_dim=17, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


# In[4]:


# 모델 실행
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
model.fit(x, y, epochs=100, batch_size=10)

