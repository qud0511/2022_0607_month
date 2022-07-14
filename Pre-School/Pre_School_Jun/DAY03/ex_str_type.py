# --------------------------------------------------------------------------------------
# 문자 자료형 => 문자열 string ---> str 타입
# --------------------------------------------------------------------------------------
movie_tltle='신비한 동물사전'
school_name="대학"
msg="'만나서 반갑습니다!'"
print(msg)
msg2='"만나서 반갑습니다!"그는 나에게 악수를 청하며 말했다.'
print(msg2)
# 모니터 화면에 출력하기 => print()
print(msg, msg2)
# --------------------------------------------------------------------------------------
# 이스케이프 문자 => \
# \n 줄 바꿈할 때
# \t 문자열 사이에 탭(스페이스바 2번) 간격을 줄 때
# \\ 문자 \를 그대로 표현할 때
# \' 작은따옴표 그대로 사용할 때
# \" 큰 따옴표 그대로 사용할 때
# \r 캐리지 리턴(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동)
# \f 폼피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
# \a 벨소리(출력할 때 PC스피커에서 '삑'소리)
# \b 백스페이스
# \000 널문자
msg3='\'만나서 반갑습니다!\''
print(msg3)

# 문자열 안에 \를 그대로 사용하고 싶으면 \\
# 일일이 입력하고 싶다면 r
path='C:\\Users\\user\\.idlerc'
print(path)
path2=r'C:\Windows\ConfigSetRoot\AutoUnattend_Files\Package\x64\ENKR\en-us'
print(path2)
# --------------------------------------------------------------------------------------
# 문자열 타입(str) 연산하기
# 문자열 덧셈(+), 곱셈(*)만 동작함.
# 공백도 문자
name='Pak'
addr='Daegu'
strAdd=name+'   '+addr+'\n'+"2022"+"\tHaHa"
print("문자열 더하기", strAdd)
print(2020, 'Hi', '2022')
# --------------------------------------------------------------------------------------
# 문자 + 숫자
print('ABC'+'2022')
# (str) + (str) 가능, (str) + (int) 불가능
# 문자 + 문자, 숫자 + 숫자로 맞춰야함.

# type casting = 자료형 변환 = 자료형이 변경 => int와 str을, 타입을 변환할 때
print('DDCFF'+str(2022))
#print(int("GYM"+2022)) => 오류, 아라비아 숫자만 가능
print(int('555')+2022)
print(float('5.555')+2022)

# 문자 * 숫자
print('AA'*22)
# (str) * (str) 불가능
# (str) * (int) 가능, (str) * (float) 불가능
print(float('5.555')*2022)
# --------------------------------------------------------------------------------------
# 교재 50페이지
print("="*50)
print("My Program")
print("="*50)

