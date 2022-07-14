import pandas as pd

DIR_PATH='./projectData/'
FILE_NAME=DIR_PATH + 'fire_allyear.csv'
fireDF=pd.read_csv(FILE_NAME, encoding='cp949')

fireDF2018_01=fireDF[fireDF['년']==2018]
print(fireDF2018_01)



# fireDF2018_02=fireDF2018_01.groupby('시도').sum()['발화열원대분류']
# print(fireDF2018_02)

print(fireDF2018_01['시도'].value_counts())


# 특정 조건을 만족하는 데이터 필터링하기
# 1. 컬럼을 선택
# 2. 컬럼의 데이터와 특정 조건을 비교 => 조건을 만족한다면 True / 조건에 맞지 않다면 False
# 3. 비교 결과를 이용해서 데이터프레임에서 일부 데이터를 추출

print( pd.DataFrame( fireDF2018_01['시도'].value_counts()).rename(columns={'시도':'건수'}) )
