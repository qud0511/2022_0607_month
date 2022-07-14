# -----------------------------------------------------------------------
#  계산기 프로그램
# 필수조건 : 계산기 클래스

# 클래스명 : Calculator
# 속성/특징 : 필드 --> 색상, 제조자
# 역할/기능 : 함수/메서드 -->
#           - 계산기 인스턴스 생서에서드 ==> __init__()
#           - 계산기 속성/특징 값 읽기 ==> getter method
#           - 계산기 속성/특징 값 변경 ==> setter method
#           - 4칙연산 기능 메서드 => plus, minus, mul, div

# -----------------------------------------------------------------------

class Calc:
    # 인스턴스 생성자
    def __init__(self,maker,color,result=0):
        self.maker=maker
        self.color=color
        self.result=result


    # getter/method (선택)
    def getData(self): return self.data
    def setData(self,*data): self.data=data

    # 내가 원하는 계산기 기능
    def plus(self,num):
        self.result=self.result+num
        print(f'plus => {self.result}')

    def minus(self,num):
        self.result=self.result-num
        print(f'minus => {self.result}')

    def mul(self,num):
        self.result = self.result * num
        print(f'mul => {self.result}')


    def div(self,num):
        self.result = self.result / num
        print(f'mul => {self.result}')


    # 사용자 인터페이스(CUI) 기능 메서드
    def showUI(self):
        print('****** 계산기 ******')
        print('1. 더하기')
        print('2. 빼기')
        print('3. 곱하기')
        print('4. 나누기')
        print('5. 초기화')
        print('6. 종료')
        print('*******************')

# -----------------------------------------------------------------------

calc1=Calc('Sharp','Pink')

num=int(input('초기값 : '))
calc1.result=num
while True:
    calc1.showUI()
    select=input('메뉴선택 :')
    if select=='6': break


    elif select=='1':
        num=int(input('숫자를 입력해 주세요.'))
        calc1.plus(num)

    elif select=='2':
        num=int(input('숫자를 입력해 주세요.'))
        print(num)
        calc1.minus(num)

    elif select=='3':
        num = int(input('숫자를 입력해 주세요.'))
        calc1.mul(num)

    elif select=='4':
        num = int(input('숫자를 입력해 주세요.'))
        calc1.div(num)

    elif select=='5':
        calc1.result=0
