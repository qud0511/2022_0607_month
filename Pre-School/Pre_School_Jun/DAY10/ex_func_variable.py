# ----------------------------------------------------------------------
# 변수의 동작 범위(Scope스코프)

# 1. 전역볌수(Global Variable)
#       > 프로그램 실행 시 메모리에 생성
#       > 프로그램 종료 시 메모리에서 삭세
#       > 파일 안에 모든 곳에서 사용 가능한 변수

# 2. 지역변수(Local Variable)
#       > 함수 실행 시 메모리에 생성
#       > 함수 종료 시 메모리에 삭제
#       > 함수 안에서만 사용 가능한 변수
# ----------------------------------------------------------------------
year=2022
msg='행복한 주말이군요!'

def testVariable(num):
    year=3000           # 지역 변수, 함수 안에서는 우선 함?
    print(num)
    print(year)
    print(msg)

testVariable(1000)
# print(f'num => {num}')  ==> 실행 오류, num is not defined
# num은 지역 변수로 testVariable함수가 실행을 종료하고 메모리에서 삭제되었기 때문.
# 즉, 함수 안에 지역변수는 사용 불가.

print(f' year => {year}')
# 2022 출력, 전역변수를 우선함.

print('\n')    # -----------------

year=2022
msg='행복한 주말이군요!'

def testVariable(num):
    global year           # global 전역변수 수정 사용 알림.
    year=3000
    print(num)
    print(year)
    print(msg)

testVariable(1000)
print(f' year => {year}')





