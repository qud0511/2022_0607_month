# ------------------------------------------------------------
# 논리 데이터 타입(bool type)
# 2가지 데이터만 저장 가능 => True, False
# ------------------------------------------------------------

isOk=False
print(f'isOk => {isOk}')
print(f'isOk => {isOk} , type => {type(isOk)}')

isOk=True
print(f'isOk => {isOk}')

print('\n')

# ------------------------------------------------------------
# 비교연산자
# ------------------------------------------------------------

# 결과는 참과 거짓으로 이다 (True, False)
# and          그리고            왼쪽 and 오른쪽            왼쪽, 오른쪽 모두 True
# or            또는            왼쪽  or 오른쪽            왼족, 오른쪽 중 한 개 이상 True
# not        부정, 반대       not True, not False        토글링(Toggle)

# ------------------------------------------------------------

age=20
gender='F'

print(f'{age}>=30 and {gender=="M"} : { age>= 30 and gender =="M" }' )
print(f'{age}<=30 and {gender=="M"} : { age<= 30 and gender =="M" }' )
print(f'{age}>=30 and {gender=="F"} : { age>= 30 and gender =="F"}' )

print('\n')

print(f'{age}>=30 or {gender=="M"} : { age>= 30 or gender =="M" }' )
print(f'{age}<=30 or {gender=="M"} : { age<= 30 or gender =="M" }' )
print(f'{age}>=30 or {gender=="F"} : { age>= 30 or gender =="F" }' )

print('\n')

print(f'not {age}>=30 : { not age>=30 }')
print(f'not {gender}>="F" : { not gender=="F" }')

print('\n')

# ------------------------------------------------------------
# 데이터 자료형과 논리값

# 123 ===> 문자형 변환 ===> str(123)
# '23.4' ===> 숫자형 변환 ===> float('23.4')
# 'ABC' ===> 논리형 변환 ===> bool('ABC')

# ------------------------------------------------------------

print(f'bool("ABC") => { bool("ABC") }, type : {type(bool("ABC"))}')
print(f'bool("") => { bool("") } , type : {type(bool(""))}')
print(f'bool("  ") => { bool("  ") }, type : {type(bool("  "))}')

print(f'bool("123") => { bool("123") }, type : {type(bool("123"))}')
print(f'bool("-123") => { bool("-123") }, type : {type(bool("-123"))}')
print(f'bool("0") => { bool("0") }, type : {type(bool("0"))}')
print(f'bool("0.1") => { bool("0.1")}, type : {type(bool("0.1"))}')
print(f'bool("0.0") => { bool("0.0")}, type : {type(bool("0.0"))}')

print('\n')

# ------------------------------------------------------------

# 같다 ( == )
# 같지 않다 ( != )
# 크다 ( > )
# 크거나 같다 ( >= )
# 작다 ( < )
# 작거나 같다 ( <= )

# ------------------------------------------------------------

data1=10
data2=5
print(f'{data1} == {data2} : { data1 == data2 }')
print(f'{data1} != {data2} : { data1 != data2 }')

print('\n')

data1='A'
data2='a'
print(f'{data1} == {data2} : { data1 == data2 }')
print(f'{data1} != {data2} : { data1 != data2 }')
print(f'{data1} >= {data2} : { data1 >= data2 }')
# 문자는 코드로 크기를 비교함. 단순히 클 것 같은 문자가 있는 것이 아님. 규칙에 의해

print('\n')

data1='Ab'
data2='AB'
print(f'{data1} >= {data2} : { data1 >= data2 }')
print(f'{data1} <= {data2} : { data1 <= data2 }')

print('\n')

data1='AbC'
data2='ABc'
print(f'{data1} >= {data2} : { data1 >= data2 }')
print(f'{data1} <= {data2} : { data1 <= data2 }')
# 앞의 문자가 더 크면 큰 것임. n의 자릿수와 비슷하게 생각.

# ------------------------------------------------------------

# 여러개 Data를 저장하기
# 리스트   [D1,D2,...,DN]
# 튜플    (D1,D2,...,DN)
# 딕셔너리
# 집합











