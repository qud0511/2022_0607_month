# ----------------------------------------------
# 논리 데이터 타입 - bool 타입
# 2가지 데이터만 저장 가능 => True, False
# ----------------------------------------------
isOk=False
print(f'isOk => {isOk} , type => {type(isOk)}')

isOk=True
print(f'isOk => {isOk} , type => {type(isOk)}')

# 비교연산자 --------------------------------------------------
# 결과는 참과 거짓 (True, False)
# 같다          ==
# 같지않다      !=
# 크다          >
# 크거나 같다    >=
# 작다          <
# 작거나 같다    <=
# ----------------------------------------------------------
data1=10
data2=5

print(f'{data1} == {data2}  : { data1 == data2 }')
print(f'{data1} != {data2}  : { data1 != data2 }')

data1='AbC'
data2='ABc'

print(f'{data1} == {data2}  : { data1 == data2 }')
print(f'{data1} != {data2}  : { data1 != data2 }')
print(f'{data1} >= {data2}  : { data1 >= data2 }')
print(f'{data1} <= {data2}  : { data1 <= data2 }')


# 논리연산자 --------------------------------------------------
# 결과는 참과 거짓 (True, False)
# and       그리고     왼쪽 and 오른쪽   왼쪽, 오른쪽 모두 True
# or        또는       왼쪽 or 오른쪽   왼쪽, 오른쪽 중 한개 이상 True
# not       부정/반대   not True, not False  토글링(Toggle)
# ----------------------------------------------------------
age=20
gender='F'

print( f'{age}>=30 and {gender=="M"} : { age>=30 and gender=="M"}' )
print( f'{age}<=30 and {gender=="M"} : { age<=30 and gender=="M"}' )
print( f'{age}<=30 and {gender=="F"} : { age<=30 and gender=="F"}' )
print('\n')
print( f'{age}>=30 or {gender=="M"} : { age>=30 or gender=="M"}' )
print( f'{age}<=30 or {gender=="M"} : { age<=30 or gender=="M"}' )
print( f'{age}<=30 or {gender=="F"} : { age<=30 or gender=="F"}' )
print('\n')
print( f'not {age}>=30    : { not age>=30 }' )
print( f'not {gender=="F"}: { not gender=="F" }' )

# 데이터 자료형과 논리값 ------------------------------------------------
# 123 ===> 문자형 변환     # str(123)
#
# '23.4' ==> 숫자형 변환  # float('23.4')
#
# 'ABC' ==> 논리형 변환  # bool('ABC')
# --------------------------------------------------------------------
print(f'bool("ABC")  =>  { bool("ABC") }, type : {type(bool("ABC"))}')
print(f'bool("")     =>  { bool("") },    type : {type(bool(""))}')
print(f'bool(" ")    =>  { bool(" ") },   type : {type(bool(" "))}')

print(f'bool(123)    =>  { bool(123) },    type : {type(bool(123))}')
print(f'bool(-123)   =>  { bool(-123) },   type : {type(bool(-123))}')
print(f'bool(0)      =>  { bool(0) },      type : {type(bool(0))}')
print(f'bool(0.1)    =>  { bool(0.1) },    type : {type(bool(0.1))}')
print(f'bool(0.0)    =>  { bool(0.0) },    type : {type(bool(0.0))}')