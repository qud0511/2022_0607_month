# 과제 0704-(1) 2010년 1월~12월까지 최고온도-최저온도 추출
# 모듈 로딩 --------------------------------
import pandas as pd
# 파일 관련 변수 선언 ------------------------
DIR_PATH='../../Data/'
FILE_NAME=DIR_PATH+'weather.csv'

# (1) CSV FILE => DataFrame으로 로딩----------------
wt=pd.read_csv(FILE_NAME)
wt.info()

# (2) 데이터 정보 확인------------
print('wt.columns->\n', wt.columns)
print('wt.head()->\n', wt.head())
print('wt->\n', wt)

# 결측치 갯수 파악 -------------
print('wt.isnull()->\n', wt.isnull())
print('wt.isnull().sum()->\n', wt.isnull().sum())

wt_1_1=wt.set_index('month')
print('wt_1_1->\n', wt_1_1)


# 1월 ~ 8월
for i in range(8):
    MonthMax = wt_1_1.iloc[[2*i]].dropna(axis=1, how='all')
    MonthMin = wt_1_1.iloc[[2*i+1]].dropna(axis=1, how='all')
    MMd_Max=MonthMax.drop(axis=1, columns=['id', 'year', 'element'])
    MMd_Min=MonthMin.drop(axis=1, columns=['id', 'year', 'element'])
    print(f'{i+1}월의 최고온도', MMd_Max.max(axis=1))
    print(f'{i+1}월의 최저온도', MMd_Min.min(axis=1))

# 10월 ~ 12월
for i in range(8, 11):
    MonthMax = wt_1_1.iloc[[2*i]].dropna(axis=1, how='all')
    MonthMin = wt_1_1.iloc[[2*i+1]].dropna(axis=1, how='all')
    MMd_Max=MonthMax.drop(axis=1, columns=['id', 'year', 'element'])
    MMd_Min=MonthMin.drop(axis=1, columns=['id', 'year', 'element'])
    print(f'{i+2}월의 최고온도', MMd_Max.max(axis=1))
    print(f'{i+2}월의 최저온도', MMd_Min.min(axis=1))