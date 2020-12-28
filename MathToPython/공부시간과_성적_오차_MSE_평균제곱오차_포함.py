#!/usr/bin/env python
# coding: utf-8

# <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>
# # 공부시간과 성적의 관계 
# 
# |공부시간|성적|예측값|
# |:---:|:---:|:---:|
# |2|81|**83.6**|
# |4|93|**88.2**|
# |6|91|**92.8**|
# |8|97|**97.4**|
# 
# # fake_a_b는 임의의 예측값을 넣으면된다 
# # 아래는 공식으로 순차적으로 풀기위해 
# # 기본에서 계산처리한값들 
# 
# ##  공식
# * $ 공부시간(x) 평균 : (2 + 4 + 6 + 8) / 4 = 5 $
# * $ 성적(y) 평균     : (81 + 93 + 91 + 97) / 4 = 90.5 $
# ### 1.  $ 기울기 a = {(x - x평균)(y - y평균)의 합     \over (x - x평균)^2의 합    } $
# ==> $ a = {(2-5)(81-90.5)+(4-5)(93-90.5)+(6-5)(91-90.5)+(8-5)(97-90.5) \over ((2-5)^2+(4-5)^2+(6-5)^2+(8-5)^2} $   
# ===> $ {46 \over 20} $   
# ====> $ 기울기 a = 2.3 $   
# ### 2 . $ y절편의 값 b = y의 평균 - (x의 평균 \times 기울기 a) $
# ==> $ b = 90.5 - (5 \times 2.3) $   
# ===> $ b = 90.5 - 11.5 $   
# ====> $ y절편의 값 b = 79 $
# ### 3. $ y = ax + b $
# ==> $ y = 2.3x + 79 $    
# ===> $y = 2.3 \times 2 + 79  = 83.6 $   
# ===> $y = 2.3 \times 4 + 79  = 88.2 $   
# ===> $y = 2.3 \times 6 + 79  = 82.8 $   
# ===> $y = 2.3 \times 8 + 79  = 87.4 $   
# ### 4.$ 오차 값 $
# ==> $ 오차 = 예측값 - 실제값 $   
# ===> $ 83.6 - 81 = 1.0 $   
# ===> $ 88.2 - 93 = 25.0 $   
# ===> $ 92.8 - 91 = 9.0 $  
# ===> $ 97.4 - 97 = 9.0 $
# ### 5.$ 평균 제곱 오차(MSE) $
# ==> $ \frac{1}{n}\sum (y_i - \hat{y_i})^2 또는 \sum\limits_{i}^n (y_i - \hat{y_i})^2 $   
# ===> $ (83.6 - 81)^2 = 6.7599999999999705    $         
# ===> $ (88.2 - 93)^2 = 23.039999999999974^2  $   
# ===> $ (92.8 - 91)^2 = 3.2399999999999896^2  $   
# ===> $ (97.4 - 97)^2 = 0.16000000000000456^2 $   
# ====> $ (6.7599999999999705 + 23.039999999999974 + 3.2399999999999896 + 0.16000000000000456) / 4 $   
# =====> $ 평균 제곱 오차(MSE) = 8.299999999999985 $

# In[1]:


import numpy as np
import matplotlib.pyplot as pl

fake_a_b = [2.3, 79.0]

data = [[2, 81], [4, 93], [6, 91], [8, 97]]

## i[0]은 첫번째값(a), i[1]은 두번째값(y)
x = [i[0] for i in data]
y = [i[1] for i in data]

print("x => ", x)
print("y => ", y)


# In[2]:


## y = ax + b 에 대한 결과 처리 함수, EX)  예측값A * X값 + 예측값B = 3 * 2 + 76
def predict(x):
    return (fake_a_b[0] * x) + fake_a_b[1]


# In[3]:


## MES 평균제곱오차, EX) Y값 점수 - 예측값, 81 - 82 = 1,0 = 1,0 * 1,0 = 1.0
def mse(y, y_hat):
    return np.mean(((y - y_hat) ** 2))


# In[4]:


# MSE 평균오차 값 
def mse_val(y, preidct_res):
    return mse(np.array(y), np.array(predict_res))


# In[5]:


# 예측값 배열
predict_res = []
 
for i in range(len(x)):
    predict_res.append(predict(x[i]))
    print("시간 : ", x[i], 
          " 성적 : ", y[i],
          " 예측값 : ", predict_res[i], 
          " 오차값 : ", mse(y[i], predict_res[i])
        )


# In[6]:


print("MSE 값 : ", mse_val(y, predict_res))


# In[7]:


# 그래프 처리 
pl.plot(x, y, label='BASE')
pl.scatter(x, y)

pl.plot(x, predict_res)
pl.scatter(x, predict_res)

pl.legend()
pl.show()

