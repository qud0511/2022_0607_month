# -----------------------------------------------------------------------------
# 문자열 데이터 타입(str) 전용의 함수, 즉 메서드(method)
# ' '.매서드()
# -----------------------------------------------------------------------------

# 대소문자 변환 메서드 ==> str.upper(), str.lower

# 대문자로 변환 ==> str.upper()
msg='Good Luck'
msg=msg.upper()
print(f'msg : {msg}')

# 소문자로 변환 ==> str.lower
msg=msg.lower()
print(f'msg : {msg}')

# -----------------------------------------------------------------------------

# 문자열 데이터의 좌우공백 제거하는 메서드
# 단, 'aaa          ', "" aaaa mmmm                 " 등 가능. 중간의 공백 제거 불가
#  str.strip(),  str.lstrip(), str.rstrip()
msg="        Happy New Year         "
print("원본 : ", msg)
print( "좌우 : ", msg.strip() )
print( msg.lstrip() )     #좌
print( msg.rstrip() )     #우

# 문자열 데이터 안에서 일부 변경해주는 메서드
# str.replace(old, new)
# 갯수 설정하지 않으면 전부 변경
# 갯수 결정하면 지정된 갯수 만큼만 변경
msg='Pithon i i i i i'
msg=msg.replace('i', 'y')
print(msg)

msg=msg.replace('i', 'y', 2)
print(msg)

# 문자열 데이터를 쪼개는(나누어주는) 메서드
# str.split() : 공백을 기준으로 나눔. 이것이 기본값.
msg='Happy New Year 2022'
result=msg.split()
print(f'result => { result }')

msg='HappyNew Year2022'
result=msg.split()
print(f'result => { result }')

msg='HappyNewYear2022'
result=msg.split()
print(f'result => { result }')

msg='010-5241-0476'
result=msg.split('-')
print(f'result => { result }')

path='C:\Program Files\Common Files\microsoft shared\OfficeSoftwareProtectionPlatform'
result=path.split('\\')
print(f'result => { result }')

# 문자열들을 합쳐서 하나의 문자열을 만들어주는 메서드
# '합쳐줄 문자'.join(여러개의 문자열)
print( '*^^*'.join(result) )

# 공백을 주거나 아무 것도 주지 않을 수도 있음.
print( ' '.join(result) )
print( ''.join(result) )



# -----------------------------------------------------------------------------

# 문자에 해당하는 코드갑 알려주는 내장함수
# ord('문자 1개')
print( 'A :', ord('A'), bin(ord('A')) )
print( 'A :', ord('B'), bin(ord('B')) )
print( 'A :', ord('a'), bin(ord('a')) )
print( 'A :', ord('b'), bin(ord('b')) )

# 코드에 해당하는 문자 알려주는 내장함수
# chr(10진수 코드값)
print( 'code 97 :', chr(97) )
print( 'code 65 :', chr(65) )

# -----------------------------------------------------------------------------

# 숫자형 -> int 정수 integer => 15, -15
#       -> float 실수 floating-point => 3.33, -3.33

# 문자형 -> str 문자열 string => '', ""

# 논리형 -> bool 논리 boolean => True, False
#                               1,     0




