#=====================================================
# 계산기 프로그램
# 클래스명 : Calc
# 변수 : 색상, 제조사, 데이터(가변)
# 함수 : 덧셈, 뺄셈, 곱셈, 나눗셈
#=====================================================

# 클래스 생성

class Calc():

    # 인스턴스 생성자
    def __init__(self,color,brand,*data):
        self.color=color
        self.brand=brand
        self.data=data

    # getter 메서드
    #def getData(self): return self.data

    # setter 메서드
    #def setData(self, *data): self.data=data

    # 덧셈 함수
    def plus(self,*data):
        data=data[0]
        result=0
        for i in data:
            i=int(i)
            result+=i
        return result

    # 뺄셈 함수
    def minus(self,*data):
        data=data[0]
        n=[]
        result=0
        for i in data:
            i=int(i)
            n.append(i)
            result-=i
            value=result+(n[0]*2)
        return value

    # 곱셈 함수
    def mult(self,*data):
        data=data[0]
        result=1
        for i in data:
            i=int(i)
            result*=i
        return result

    # 나눗셈 함수
    def div(self,*data):
        data=data[0]
        n=[]
        result=1
        for i in data:
            i=int(i)
            n.append(i)
            result/=i
            value=result*(n[0]*n[0])
        return value

    # 사용자 인터페이스 (CUI) 기능 메서드
    def showUI(self):
        print('*****  계  산  기  *****')
        print('*      1. 덧  셈       *')
        print('*      2. 뺄  셈       *')
        print('*      3. 곱  셈       *')
        print('*      4. 나눗셈       *')
        print('*      5. 종  료       *')
        print('***********************')
#=====================================================

# 기능 구현

calcAPP=Calc('black', 'sharp', None)
while True:
    calcAPP.showUI()
    select=input('메뉴 선택 : ')
    if select == '5':break
    elif select == '1':
        data=input('입력 (숫자 간 공백으로 구분) : ').split()
        print(calcAPP.plus(data))
    elif select == '2':
        data=input('입력 (숫자 간 공백으로 구분) : ').split()
        print(calcAPP.minus(data))
    elif select == '3':
        data=input('입력 (숫자 간 공백으로 구분) : ').split()
        print(calcAPP.mult(data))
    elif select == '4':
        data=input('입력 (숫자 간 공백으로 구분) : ').split()
        print(calcAPP.div(data))
    else : print('잘못 입력했습니다. 다시 입력하세요.')