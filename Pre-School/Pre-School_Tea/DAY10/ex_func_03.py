# ----------------------------------------------------
# 변수의 동작범위 (Scope 스코프)
# - 전역변수(Global Variable)
#       > 프로그램 실행시 메모리에 생성
#       > 프로그램 종료시 메모리에서 삭제
#       > 파일안에 모든 곳에서 사용 가능한 변수
# - 지역변수(Local Variable)
#       > 함수 실행시 메모리에 생성
#       > 함수 종료시 메모리에 삭제
#       > 함수 안에서만 사용 가능한 변수
# ----------------------------------------------------
year=2022
msg="행복한 주말이군요!"
money = 1000;

def testVariable(num):
    #global year  # 전역변수 수정 사용 알림
    year=3000
    global  money
    money=0
    print(num)
    print(year)
    print(msg)

def output():
    print(f"현재 잔고 :{money} ")

def inputMoney():
    global  money
    money=money+800

inputMoney()
inputMoney()
output()
testVariable(1000)
#print(f'num => {num}')   # 함수안에 존재하는 지역변수는 사용불가
print(f'year => {year}')

print(10,20,30)
print(10,20,30, sep='*')
print(10,20,30, 40,sep='----', end='***')
print(10,20,30)
print(10,20,30)