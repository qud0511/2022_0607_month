# 계산기 프로그램
# 함수 조건 : 계산기 클래스

class Carculator:

    # 인스턴스 생성자
    def __init__(self, maker, color, *data):  # 가변인자는 튜플로 받음 -> 뽑아낼 수 있다는 것
        self.maker = maker
        self.color = color
        self.data = data  # 읽어오는 것, 바꾸는 것 해줘야 함

    # getter/setter 메서드 (선택)
    def getData(self): return self.data
    def setData(self, *data): self.data = data  # 연산 전에 숫자를 받아야 하니까 setter 메서드를 활용

# -----------------------------------------------------

    # 사용자 인터페이스(CUI) 기능 메서드
    def showUI(self):
        print('****** 계산기 ******')
        print('**    1. 덧셈     **')
        print('**    2. 뺄셈     **')
        print('**    3. 곱셈     **')
        print('**    4. 나눗셈   **')
        print('*******************')

# -------------------------------------------------------

    # 내가 원하는 계산기 기능
    def add(self, *data):
        result = data[0]
        for i in data[1:]:
            result += i
        return result

    def sub(self, *data):
        result = data[0]
        for i in data[1:]:
            result -= i
        return result

    def mul(self, *data):
        result = data[0]
        for i in data[1:]:
            result *= i
        return result

    def div(self, *data):
        result = data[0]
        for i in data[1:]:
            result /= i
        return result

#------------------------------------------------------------------------------------------
calcApp = Carculator('sharp', 'Pink', None)    # 계산기 객체가 생긴 것임

while True:
    calcApp.showUI()
    select = input('메뉴 선택 : ')

    if select == '1':
        print(calcApp.add(1,2,3))

    elif select == '2':
        print(calcApp.sub(100,42,6,3))

    elif select == '3':
        print(calcApp.mul(3,10,2))

    elif select == '4':
        print(calcApp.div(240,12,2,5))

