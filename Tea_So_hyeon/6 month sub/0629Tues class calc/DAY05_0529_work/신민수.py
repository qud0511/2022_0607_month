class Calculator:
    # 인스턴스 생산자
    def __init__(self,color,brand,*data):
        self.color=color
        self.brand=brand
        self.data = data

    # getter/setter메서드 (선택)
    def setData(self, *data):
        self.data = data

    #  내가 원하는 계산기 가능
    def plus(self):
        total=0
        for num in self.data:
            total += num
        return total

    def mul(self):
        total=1
        for num in self.data:
            total=total*num
        return total

    def minus(self):
        total=10
        for num in self.data:
            total=total-num
        return total

    def div(self):
        total=10
        for num in self.data:
            total=total/num
        return total

    # 사용자 인터페이스(CUI) 기능 메서드
    def showUI(self):
        print("******* 계산기 *******")
        print("1. 덧셈(시작값:0)")
        print("2. 뺄셈(시작값:10)")
        print("3. 곱셈(시작값:1)")
        print("4. 나눗셈(시작값:10)")
        print("5. 종료")
        print("******* 계산기 *******")


calcAPP=Calculator('Shop','Pink', None)
calcAPP.setData(1,2,3,4,5)
while True:
    calcAPP.showUI()
    select = input("메뉴 선택: ")
    if select == " 5 ":
        break
    elif select == "1":
        print(f' 0 + {calcAPP.data}')
        print(f" plus => {calcAPP.plus()}")
    elif select == "2":
        print(f' 10 - {calcAPP.data}')
        print(f" minus => {calcAPP.minus()}")
    elif select == "3":
        print(f' 1 * {calcAPP.data}')
        print(f" multiple => {calcAPP.mul()}")
    elif select == "4":
        print(f' 10 / {calcAPP.data}')
        print(f" division => {calcAPP.div()}")
    else:
        print("1~5 중 다시 입력")


