# -----------------------------------------------------------------------------------
# 문자열 데이터 타입(str) 전용의 함수, 즉 메서드(method)
# '    '.메서드()
# 문자열 변수명.메서드()
# -----------------------------------------------------------------------------------

data='Happy Summer Happy Summer Happy Summer'

# 문자열 안에서 특정 문자/문자열의 갯수를 세는 메서드
# str.count()
# 문자열 안에 m은 몇개?
data.count('m')
print(data.count('m'))

value=data.count('m')
print(value)

value=data.count('M')
print(value)

value=data.count('py')
print(value)

# -----------------------------------------------------------------------------------

# 문자열 안에서 특정 문자/문자열의 인덱스를 찾는 메서드
# str.find(), str.index()

# str.find()
value=data.find('S')
print(f'\'S\' 인덱스 : {value}')
print(f'"S" 인덱스 : {value}')
print(data.find('S'))
print('"S" 인덱스 : ', data.find('S'))

# find는 제일 앞에 있는 문자열의 인덱스만 알려줌.
# 음(-)의 인덱스는 안 찾아줌.

print(data.find('Zoo'))
# 문자열에 없으면 -1로 출력햄.


# str.index()
print(data.index('S'))

# print(data.index('Zoo'))
# str.index()는 없은 문자를 찾으면 오류 발생함.



