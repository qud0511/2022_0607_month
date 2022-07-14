import pandas as pd

DIR_PATH='./projectData/'
FILE_NAME=DIR_PATH + 'fire_allyear.csv'
fireDF=pd.read_csv(FILE_NAME, encoding='cp949')

# print(fireDF)

# print('='*40)

# print(fireDF.columns)

yearIndex = fireDF.set_index('년')
print(yearIndex)

print('='*20, '2018년 화재', '='*20)
year2018 = yearIndex.loc[2018]
print(year2018)


print('='*20, '시도', '='*20)
ChungBuk=year2018['시도'].value_counts()
print(ChungBuk)

print('='*20, '월', '='*20)
month=year2018['월'].value_counts()
print(month)

print('='*20, '시간대', '='*20)
time=year2018['시간대'].value_counts()
print(time)

print('='*20, '화재유형', '='*20)
firType=year2018['화재유형'].value_counts()
print(firType)

print('='*20, '발화열원대분류', '='*20)
fireCause1=year2018['발화열원대분류'].value_counts()
print(fireCause1)

print('='*20, '발화요인대분류', '='*20)
fireCause2=year2018['발화요인대분류'].value_counts()
print(fireCause2)

print('='*20, '최초착화물대분류', '='*20)
firstFire=year2018['최초착화물대분류'].value_counts()
print(firstFire)

print('='*20, '장소대분류', '='*20)
location=year2018['장소대분류'].value_counts()
print(location)

print('='*20, '사망', '='*20)
death=year2018['사망'].value_counts()
print(death)

print('='*20, '부상', '='*20)
Injury=year2018['부상'].value_counts()
print(Injury)

print('='*20, '인명피해(명)소계', '='*20)
DI=year2018['인명피해(명)소계'].value_counts()
print(DI)

print('='*20, '재산피해소계', '='*20)
Property=year2018['재산피해소계'].value_counts()
print(Property)


# 0을 엔에이 값으로 바뀨고, 드롭 엔에이로 날려버린다. 넘파이로 한다.


# Gyeonggi = pd.DataFrame( Gyeonggi.value_counts().sort_values(ascending=False) )
# Gyeonggi