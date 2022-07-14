# -------------------------------------------------------
#   속성/특징 => 필드(Field)
#       >> 색상, 제조사, 데이터
#   기능
#   >> 계산기 인스턴스 생성 메서드 ==>__init__()
#   >> 계산기 속성/특징 값 읽기 ==> getter method
#   >> 계산기 속성/특징 값 변경 ==> setter method
#   >> 4칙연산 기능 메서드 ==> plus, minus, mul, div
# -------------------------------------------------------
class Calc:

    a = 0
    data = []

    # 인스턴스 생성자
    def __init__(self, maker, color, *data): #*는 가변, data는 계속 바뀜
        self.maker = maker
        self.color = color
        self.data = data

    # getter/setter메서드 (선택)
    def getData(self): return self.data
    def setData(self, *data): self.data=data

    # 내가 원하는 계산기 기능 --------------------------
    def plus(self, *data):
        sum = data[0]
        for i in range(1, len(data)):
            sum = sum + data[i]
        print(sum)
    def minus(self, *data):
        minus = data[0]
        for i in range(1, len(data)):
            minus = minus - data[i]
        print(minus)
    def mul(self, *data):
        multi = data[0]
        for i in range(1, len(data)):
            multi = multi * data[i]
        print(multi)
    def div(self, *data):
        div = data[0]
        for i in range(1, len(data)):
            div = div / data[i]
        print(div)


    # 사용자 인터페이스(CUI) 기능 메서드
    def showUI(self):
        print("***** 계산기 *****")
        print("1. 덧셈")
        print("2. 뺄셈")
        print("3. 곱셈")
        print("4. 나눗셈")
        print("5. 종료")
        print("****************")

# ---------------------------------------------------------------
calcApp = Calc('Sharp', 'Pink', None)

while True:
    calcApp.showUI()
    select = input("메뉴 선택: ")
    if select == '5': break
    elif select == '1':
        calcApp.plus(1, 1, 1, 1)
    elif select == '2':
        calcApp.minus(2, 2, 2, 2)
    elif select == '3':
        calcApp.mul(3, 3, 3, 3)
    elif select == '4':
        calcApp.div(4, 4, 4, 4)
