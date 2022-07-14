# 현재 상태 -> 클래스는 만들었으나 메서드는 만들지 않고 바로 코딩


#
# 계산기 프로그램
# 필수 조건 : 계산기 클래스

class Calculator:
    # 인스턴스 생성자
    def __init__(self, maker, total=0):
        self.maker=maker
        self.total=total

    # # getter / setter (선택)
    # def getData(self):
    #     return self.data
    # def setData(self, *data):
    #     self.data=data

    # 원하는 계산기 기능


    # def plus(self,a,b):
    #     return a+b
    # def minus(self,a,b):
    #     return a-b
    # def multiple(self,a,b):
    #     return a*b
    # def divide(self,a,b):
    #     try:
    #         dividied = a/b
    #         return dividied
    #     except: print('<0으로 나눌 수 없습니다.>')


    # 사용자 인터페이스 = CUI(캐릭터 유저 인터페이스, 콘솔에 찍히는거)
    def showUI(self):
        print('***** 계산기 *****')
        print('* 1. 덧  셈')
        print('* 2. 뺄  셈')
        print('* 3. 곱  셈')
        print('* 4. 나 눗 셈')
        print('* 5. 종  료 ')
        print('****************')

# -------------------------------------------------------------------------------------
calcApp=Calculator('SHARP')

while True:
    calcApp.showUI()
    menuSelect=input('메뉴를 선택하세요. : ')
    if menuSelect=='5':
        break
    elif menuSelect=='1':
        result=0
        while True:
            num1=input('숫자를 입력하거나 =를 입력해 결과를 확인하세요 : ')
            if num1 == '=':
                print(result)
                break
            else:
                try:
                    num1=int(num1)
                    result+=num1
                except Exception:
                    print('숫자가 아닙니다.')
    elif menuSelect=='2':
        while True:
            num1 = input('첫번째 숫자를 입력하세요. : ')
            try:
                result=int(num1)
                break
            except Exception:
                print('숫자가 아닙니다.')
        while True:
            num2 = input('뺄 숫자를 입력하거나 =를 입력해 결과를 확인하세요. : ')
            if num2 == '=':
                print(result)
                break
            else:
                try:
                    num2 = int(num2)
                    result-=num2
                except Exception:
                    print('숫자가 아닙니다.')
    elif menuSelect=='3':
        result=1
        while True:
            num1=input('숫자를 입력하거나 =를 입력해 결과를 확인하세요 : ')
            if num1 == '=':
                print(result)
                break
            else:
                try:
                    num1=int(num1)
                    result*=num1
                except Exception:
                    print('숫자가 아닙니다.')
    elif menuSelect=='4':
        while True:
            num1 = input('첫번째 숫자를 입력하세요. : ')
            try:
                result = int(num1)
                break
            except Exception:
                print('숫자가 아닙니다.')
        while True:
            num2 = input('나눌 숫자를 입력하거나 =를 입력해 결과를 확인하세요. : ')
            if num2 == '=':
                print(result)
                break
            elif num2=='0':
                print('0으로 나눌 수 없습니다.')
            else:
                try:
                    num2 = int(num2)
                    result /= num2
                except Exception:
                    print('숫자가 아닙니다.')

