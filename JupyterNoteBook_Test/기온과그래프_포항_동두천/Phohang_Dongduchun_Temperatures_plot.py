#!/usr/bin/env python
# coding: utf-8

# # 포항과 동두천의 각 자료 별 온도변화 분석 그래프
# ***
# * 작성자 : sidcode(Abdullah.Kim) <sidcode@gmail.com>
# * 자료출처 : **[기상자료개방포털(기온분석)]**(https://data.kma.go.kr/stcs/grnd/grndTaList.do?pgmNo=70)
# 
# ### 1.포항
#    * 1944년 01월 01일 부터 2020년 12월 09일 까지의 기온변화 자료
# 
# 
# ### 2. 동두천
#    * 1998년 01월 01일 부터 2020년 12월 07일 까지의 기온변화 자료   

# ***
# 
# * 포항과 동두천 CSV 파일 읽어 드림
#     * 포항   : pohang_19440717_to_20201209.csv   
#     * 동두천 : dongduchun_19980101_to_20201207.csv
#     
#     
# * 각 지역별 온도변화그래프 처리

# In[96]:


import csv
import matplotlib.pyplot as plt

phohang = open('pohang_19440717_to_20201209.csv', 'r', encoding='cp949')
p_data = csv.reader(phohang)

dongduchun = open('dongduchun_19980101_to_20201207.csv', 'r', encoding='cp949')
d_data = csv.reader(dongduchun)


# 
# 
# ***
# * 포항 데이터 출력
#     * next() 함수를 이용하여 구분 항목 제거
#     * 평균기온, 최저기온, 최고기온 이 모두 존재하는 날만 처리

# In[97]:


next(p_data)

p_n_result = []
p_l_result = []
p_h_result = []
p_date     = []

for prow in p_data :
    if prow[2] != '' and prow[3] != '' and prow[4] != '' :
        p_n_result.append(float(prow[2])) # 평균기온
        p_l_result.append(float(prow[3])) # 최저기온
        p_h_result.append(float(prow[4])) # 최고기온
        p_date.append(int(prow[0].split('-')[0]))    # 연도
        print(prow)
    
phohang.close()


# In[93]:


print(p_date)


# *** 
# * 그래프 출력

# In[102]:


plt.figure(figsize = (20, 7))
plt.plot(p_date, p_l_result, label="Low")
plt.plot(p_date, p_n_result, 'g', label="Nomal")
plt.plot(p_date, p_h_result, 'r', label="Hight")
plt.legend()
plt.show()


# 
# 
# ***
# * 동두천 데이터 출력
#     * next() 함수를 이용하여 구분 항목 제거
#     * 평균기온, 최저기온, 최고기온 이 모두 존재하는 날만 처리    

# In[99]:


next(d_data)

d_n_result = []
d_l_result = []
d_h_result = []
d_date     = []

for drow in d_data :
    if drow[2] != '' and drow[3] != '' and drow[4] != '' :
        d_n_result.append(float(drow[2]))
        d_l_result.append(float(drow[3]))
        d_h_result.append(float(drow[4]))
        d_date.append(int(drow[0].split('-')[0]))    # 연도
        print(drow)
    
dongduchun.close()


# In[71]:


print(d_date)


# * 그래프 출력

# In[100]:


plt.figure(figsize = (15, 5))
plt.plot(d_date, d_l_result, label="Low")
plt.plot(d_date, d_n_result, 'g', label="Nomal")
plt.plot(d_date, d_h_result, 'r', label="Hight")
plt.legend()
plt.show()


# * 두 도시의 통합 온도 그래프

# In[101]:


plt.figure(figsize=(20, 7))

# 포항
plt.plot(p_date, p_l_result, label="PL")
plt.plot(p_date, p_n_result, label="PN")
plt.plot(p_date, p_h_result, 'r', label="PH")

# 동두천
plt.plot(d_date, d_n_result, label="DN")
plt.plot(d_date, d_l_result, 'k', label="DL")
plt.plot(d_date, d_h_result, label="DH")

plt.legend()
plt.show()

