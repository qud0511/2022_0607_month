# 계산기 프로그램
class Calculator:
    # 객체 생성 -> 색상, 제조사, 데이터(가변인자)
    def __init__(self,maker,color,*data):
        self.maker=maker
        self.color=color
        self.data=data#튜플로 받아짐

    # getter/setter 선택 -> data
    def getData(self): return self.data
    def setData(self,*data): self.data=data

    # 4칙연산 기능
    def plus(self):
        num1=list(self.data)[0]
        num2=input('숫자 입력: ')
        total=int(num1)+int(num2)
        print(f'누적 => {total}')
        cal.setData(total)

    def minus(self):
        num1 = list(self.data)[0]
        num2 = input('숫자 입력: ')
        total = int(num1) - int(num2)
        print(f'누적 => {total}')
        cal.setData(total)
    def multi(self):
        num1 = list(self.data)[0]
        num2 = input('숫자 입력: ')
        total = int(num1) * int(num2)
        print(f'누적 => {total}')
        cal.setData(total)
    def div(self):
        num1 = list(self.data)[0]
        num2 = input('숫자 입력: ')
        try:
            total=int(num1)/int(num2)
            print(f'누적 => {total}')
            cal.setData(total)
        except:
            print("ZeroDivisionError")

    # 유저 인터페이스(UI) 기능
    def showUI(self):
        print('***** Calculator ******')
        print('1. +')
        print('2. -')
        print('3. x')
        print('4. %')
        print('5. END')
        print('***********************')

cal=Calculator('Shap', 'Black')
cal.setData(input('숫자 입력: '))
while True:
    cal.showUI()
    select=input('번호 입력: ')
    if select=='5':
        result=list(cal.getData())
        print(result[0])
        break
    elif select=='1': cal.plus()
    elif select=='2': cal.minus()
    elif select=='3': cal.multi()
    elif select=='4': cal.div()
    else: print('다시 입력해 주세요.')