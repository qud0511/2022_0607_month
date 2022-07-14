# ----------------------------------------------------------------------
# 함수(Function) : 자주 사용되는 코드 묶음
#                 그 코드 묶음에 이름(즉, 함수명)을 붙임
#                 해당 코드가 필요한 경우 이름을 불러서 사용
#                 => 함수호출
# 종류   - (1) 내장함수(Builtin function) : print(), len(), type(), id()
#       - (2) 사용자정의함수
# ---------------------------------------------------------------------
greeting="Hello~!"

# 화면출력하기 => print()
print(greeting)

# 문자열(str)안에 문자가 몇개 있는지 알려주는 함수 => len()
print(f'{greeting}의 문자 갯수/길이 : {len(greeting)}')

# 데이터 타입 알려주는 함수  => type()
print(f'{greeting}의 자료형 : {type(greeting)}')

# 변수에 저장된 주소값 확인 함수 => id()
print(f'greeting변수 저장값 : {id(greeting)}')

# 여러개의 데이터를 저장하는 타입 => 리스트 (list)
jumsu=[30,5,4,19,21,94,87,100]
print(f'jumsu 리스트의 갯수/길이 : {len(jumsu)}')

greeting="Hlelo~!"
nums=[ 10, 20, 30]


