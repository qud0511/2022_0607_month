# ---------------------------------------------------
# 문자열 데이터 타입(str) 전용의 함수 즉 메서드(method)
# ' '.메서드()
# 문자열 변수명.메서드()
# ---------------------------------------------------
data="Happy Summer Happy Happy"

# 문자열 안에서 특정 문자/문자열의 갯수를 체크하는 메서드
# str.count()
print( data.count('m') )

value=data.count('py')
print(value)

value=data.count('Py')
print(value)

# 문자열 안에서 특정 문자/문자열의 인덱스 찾는 메서드
# str.find(), str.index()
data="Happy Summer Happy Happy"
#     0123456789
value=data.find('S')
print(f'\'S\' 인덱스 : {value}')
value=data.find('mer')
print(f'\'mer\' 인덱스 : {value}')
value=data.find('py')
print(f'\'py\' 인덱스 : {value}')
value=data.rfind('py')
print(f'\'py\' 인덱스 : {value}')

value=data.find('zoo')
print(f'\'zoo\' 인덱스 : {value}')

value=data.index('zoo')
print(f'\'zoo\' 인덱스 : {value}')

