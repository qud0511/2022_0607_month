# --------------------------------------------------
# 계산기 프로그램
# 필수 조건 : 계산기 클래스
# --------------------------------------------------
class Calculator:

    # 인스턴스 생성자
    def __init__(self, maker, color, *data):
        self.maker=maker
        self.color=color
        self.data=data

    # getter/setter 메서드 (선택)
    # def getData(self): return self.data     # 지금은 필요없는듯
    # maker랑 color는 바뀔 일이 없으니까 data만.

    def setData(self, *data): self.data=data

    # 내가 원하는 계산기 기능
    def plus(self):
        result=0
        for num in self.data:
            result+=num
        return result

    def minus(self):
        result = 0
        result = self.data[0] - self.data[1]
        for i in range(2, len(self.data)):
            result-=self.data[i]
        return result

    def mul(self):
        result=1
        for num in self.data:
            result*=num
        return result

    def div(self):
        result = 0
        result = self.data[0] / self.data[1]
        for i in range(2, len(self.data)):
            result/=self.data[i]
        return result

    # 사용자 인터페이스(CUI) 기능 메서드
    def showUI(self):
        print('***** 계산기 *****')
        print('1. 덧셈')
        print('2. 뺄셈')
        print('3. 곱셈')
        print('4. 나눗셈')
        print('5. 종료')
        print('*****************')

# -----------------------------------------------------
calcApp=Calculator('Sharp', 'Pink', None)

while True:
    calcApp.showUI()
    calcApp.setData(3, 7, 3, 8, 9, 10)
    select=input("메뉴 선택 : ")
    if select=='5': break
    elif select=='1':   # 덧셈
        #calcApp.getData() # getData는 왜 필요? 필요없나
        print(f'plus => {calcApp.plus()}')
    elif select=='2':    # 뺄셈
        print(f'minus => {calcApp.minus()}')
    elif select=='3':   # 곱셈
        print(f'multi => {calcApp.mul()}')
    elif select=='4':   # 나눗셈
        print(f'div => {calcApp.div()}')
    else: print('잘못된 번호입니다. 다시 입력해주세요.')