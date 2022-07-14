# 계산기 프로그램
# 필수조건: 계산기 클래스
# -------------------------
class Calculator:
    #인스턴스 생성자
    def __init__(self, maker, color, *data):    # data는 가변이니까 앞에 *
        self.maker=maker
        self.color = color
        self.data = data

    #getter, setter 메서드(선택)
    def getData(self): return self.data
    def setData(self, *data): self.data= data

    #내가 원하는 계산기 기능
    def plus(self):
        total =0
        for i in self.data:
           total += i
        return total

    def minus(self):
        result = self.data[0]
        for i in self.data[1:]:
            result -= i
        return result

    def multi(self):
        result = 1
        for i in self.data:
            result *= i
        return result

    def divi(self):
        try:
            result = self.data[0]
            for i in self.data[1:]:
                result /= i
            return result
        except Exception:
            print('0으로 나눌 수 없습니다.')




    #사용자와 인터페이스(CUI) 기능 메서드
    def showUI(self):
        print('****계산기***')
        print('1. 덧셈 ')
        print('2. 뺄셈 ')
        print('3. 곱셈 ')
        print('4. 나눗셈 ')
        print('5. 종료 ')
        print('************')

# --------------------------------------------------------
calcApp=Calculator('sharp', 'pink', None)
while True:
    calcApp.showUI()
    calcApp.setData(2,8,5)
    select =input('메뉴선택')
    if select == '5':break
    elif select == '1':
        print(calcApp.plus())
    elif select == '2':
        print(calcApp.minus())
    elif select == '3':
        print(calcApp.multi())
    elif select == '4':
        print(calcApp.divi())



