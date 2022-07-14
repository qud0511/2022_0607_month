# ---------------------------------
# 계산기 프로그램
# 필수 조건 : 계산기 클래스
# ---------------------------
class Calculator:

    # 인스턴스 생성자
    def __init__(self, maker, color, start = 0):
        self.maker = maker
        self.color = color
        self.start = start

    # getter / setter 메서드
    def getStart(self): return self.start

    def getPlus(self, data):
        self.start += sum(data)
        print(self.start)

    def getMinus(self, data):
        self.start -= sum(data)
        print(self.start)

    def getMultiply(self, data):
        for i in data:
            self.start = self.start * i
        print(self.start)

    def getDivide(self, data):
        for i in data:
            self.start = self.start / i
        print(self.start)

    # 내가 원하는 계산기 기능
    def plus(self):
        data = []
        while True:
            wow = input('더하고 싶은거 다 입력하고 그만하고 싶으면 x 눌러 ㅇㅇ')
            if wow == 'x':
                return data
            else:
                wow = int(wow)
                data.append(wow)

    def minus(self):
        data = []
        while True:
            wow = input('빼고 싶은거 다 입력하고 그만하고 싶으면 x 눌러 ㅇㅇ')
            if wow == 'x':
                return data
            else:
                wow = int(wow)
                data.append(wow)

    def multiply(self):
        data = []
        while True:
            wow = input('곱하고 싶은거 다 입력하고 그만하고 싶으면 x 눌러 ㅇㅇ')
            if wow == 'x':
                return data
            else:
                wow = int(wow)
                data.append(wow)

    def divide(self):
        data = []
        while True:
            wow = input('나누고 싶은거 다 입력하고 그만하고 싶으면 x 눌러 ㅇㅇ')
            if wow == 'x':
                return data
            else:
                wow = int(wow)
                data.append(wow)

    # 사용자 인터페이스(CUI) 기능 메서드
    def showUI(self):
        print('***** 계산기 *****')
        print('1. 덧셈')
        print('2. 뺄셈')
        print('3. 곱셈')
        print('4. 나눗셈')
        print('5. 초기화')
        print('6. 종료')
        print('*****************')

# -------------------------------------
calcApp = Calculator('sharp', 'pink')

while True:
    calcApp.showUI()
    select = input('선 택')

    if select == '1':
        data = calcApp.plus()
        calcApp.getPlus(data)

    elif select == '2':
        data = calcApp.minus()
        calcApp.getMinus(data)

    elif select == '3':
        data = calcApp.multiply()
        calcApp.getMultiply(data)

    elif select == '4':
        data = calcApp.divide()
        calcApp.getDivide(data)

    elif select == '5':
        calcApp.start = 0
        print(calcApp.start)

    elif select == '6': break

    else: print('잘못된 접근입니다.')

