# -------------------------------------------------------------------------
# 계산기 프로그램
# 필수 조건 : 계산기 클래스
# -------------------------------------------------------------------------
class Calculator:

    # 인스턴스 생성자
    def __init__(self, maker, color, *data):  # 가변인자는 튜플로 받음
        self.maker = maker
        self.color = color
        self.data = data

    # getter/setter메서드 (선택)
    def getData(self): return self.data

    def setData(self, *data): self.data = data

    # 내가 원하는 계산기 기능 -------------------------------------------------
    def plus(self):                                 #self.data에 있는 값을 모두 더하는 함수입니다.
        print(f'plus => {self.data}')               #self.data는 밑에서 입력받은 수는 튜플형태가 됩니다.
        total=0                                     #초기값 0
        for i in range(0, len(self.data)):
            total+=self.data[i]
        return total

    def minus(self):                                #self.data에 있는 값을 0에다가 모두 빼는 함수입니다.
        print(f'minus => {self.data}')
        total=0                                      #초기값 0
        for i in range(0, len(self.data)):
            total-=self.data[i]
        return total

    def mul(self):                                   #self.data에 있는 값을 모두 곱하는 함수입니다.
        print(f'nul => {self.data}')
        total=1                                     #초기값 1
        for i in range(0,len(self.data)):
            total*=self.data[i]
        return total

    def div(self):                                  #self.data에 있는 값을 모두 1에다가 나누는 함수입니다.
        print(f'div => {self.data}')
        total=1
        for i in range(0,len(self.data)):
            total/=self.data[i]
        return total


    # 사용자 인터페이스(CUI) 기능 메서드
    def showUI(self):
        print("****** 계산기 ******")
        print("1. 덧      셈")
        print("2. 뺄      셈")
        print("3. 곱      셈")
        print("4. 나  눗  셈")
        print("5. 종      료")
        print("*****************")


# -------------------------------------------------------------------------
calcApp = Calculator('Sharp', 'Pink', None)  # None 이라고 적힌 곳에 수를 입력 받습니다. 예) 1, 2, 3
                                             # 수를 입력받지 않으면 오류가 뜹니다.
                                             # 일반 계산기와는 다르게 모든 수를 더하면 전부 더하고 빼면 전부 빼는데 이렇게 하는 것이 맞나요..??
while True:
    calcApp.showUI()
    select = input("메뉴 선택:")
    
    if select == '5':
        break

    elif select == '1':
        print(calcApp.plus())

    elif select == '2':
        print(calcApp.minus())

    elif select == '3':
        print(calcApp.mul())

    elif select == '4':
        print(calcApp.div())





