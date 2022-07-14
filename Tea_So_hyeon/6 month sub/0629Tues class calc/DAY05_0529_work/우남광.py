# 계산기 프로그램
class Ca:
    # 인스턴스 생성자: # 색상, 제조사, 데이터
    def __init__(self, color, brand, *data):
        self.color = color
        self.brand = brand
        self.data = data
    # getter, setter 메서드는 선택
    def getData(self): return self.data
    def setData(self, *data): self.data = data
    # 내가 원하는 계산기 기능
    def plus(self, *data):
        result = 0
        if type(self.data) == int or type(self.data)== float:
            for i in data:
                result += i
            self.data = self.data + result
        else:
            for j in self.data:
                result += j
            for i in data:
                result += i
            self.data = result
    def minus(self, *data):
        result = 0
        if type(self.data) == int or type(self.data)== float:
            for i in data:
                result += i
            self.data = self.data - result
        else:
            for j in self.data:
                result += j
            for i in data:
                result -= i
            self.data = result

    def mul(self, *data):
        result = 1
        if type(self.data) == int or type(self.data) == float:
            for i in data:
                result *= i
            self.data *= result
        else:
            for j in self.data:
                result += j
            for i in data:
                result *= i
            self.data = result
    def divide(self, *data):
        result = 1
        if type(self.data) == int or type(self.data)== float:
            for i in data:
                result /= i
            self.data *= result
        else:
            for j in self.data:
                result += j
            for i in data:
                result /= i
            self.data = result


    # 사용자 인터페이스 (CUI) 기능 메서드
    def showUI(self):
        print("***** 계산기 *****")
        print("1. 덧셈")
        print("2. 뺄셈")
        print("3. 곱셈")
        print("4. 나눗셈")
        print("Q. 나가기")
        print("*****************")
    def listftn(self, select):
        ftnList = [self.plus, self.minus, self.mul, self.divide]
        ftnName = ['덧셈', '뺄셈', '곱셈', '나눗셈']
        num = input(f"{ftnName[int(select)-1]} 값을 입력하세요: ").split(',')
        print(num)
        print(type(select))
        for i in num:
            ftnList[int(select)-1](float(i))
        print(self.data)

ca = Ca("black","sharp", None)
def calPlay():
    ca.setData(0)
    while True:
        ca.showUI()
        select = input("메뉴 선택: ")
        if select == 'Q':
            print(f'계산 결과: {ca.data}')
            break
        elif select == '1':
            ca.listftn(select)
        elif select == '2':
            ca.listftn(select)
        elif select == '3':
            ca.listftn(select)
        elif select == '4':
            ca.listftn(select)
        else:
            print("잘못된 입력입니다.")


# 계산기 프로그램 생성

calPlay()