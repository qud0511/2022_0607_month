#계산기 클래스
'''
*클래스명: Calculator
*속성/특징=>필드
 -색상, 제조사, 데이터
*역할/기능=>메서드/함수
 -계산시 인스턴스 생성 메서드
 -계산기 속성/특징 값 읽기
 -계산기 속성/특징 값 변경
 -사칙연산 기능 메서드=>plus,minus,mui,div
'''
class Calculator:
    #인스턴스 생성자
    def __init__(self,maker,color,*data): #*data는 튜플 형식
        self.maker=maker
        self.color=color
        self.data=data

    #getter/setter 메서드
    def getData(self): return self.data
    def setData(self,*data): self.data=data

    #내가 원하는 계산기 기능
    def plus(self,a,i):
        print(f"{a} + {self.data[i+1]} = {a+self.data[i+1]}")
        return a+self.data[i+1]

    def minus(self,a,i):
        print(f"{a} - {self.data[i+1]} = {a - self.data[i + 1]}")
        return a - self.data[i + 1]

    def mul(self,a,i):
        print(f"{a} * {self.data[i+1]} = {a * self.data[i + 1]}")
        return a * self.data[i + 1]

    def div(self,a,i):
        print(f"{a} / {self.data[i+1]} = {a / self.data[i + 1]}")
        return a / self.data[i + 1]

    #사용자 인터페이스(CUI) 기능 메서드
    def showUI(self):
        print('*****  계산기  *****')
        print('1. 덧셈')
        print('2. 뺄셈')
        print('3. 곱하기')
        print('4. 나누셈')
        print('5. 종료')
        print('*******************')

def resu(a):
    result = a.data[0]
    l=len(a.data)
    gijun=0
    for i in range(l-1):
        a.showUI()
        print(f"{result}과(와) {a.data[i + 1]} 계산을 시작합니다.")
        select = input(f"원하는 사칙연산의 숫자를 입력하세요 >>> ")
        if select == '1':
            result=a.plus(result,i)
        elif select == '2':
            result=a.minus(result,i)
        elif select == '3':
            result=a.mul(result,i)
        elif select == '4':
            result=a.div(result,i)
        elif select == '5':
            break
        else:
            print(f"연산을 할 수 없습니다. 다시 시도해주세요!!!")
            gijun=1
            break
    if gijun==0:
        print(f"최종 결과는 {result}입니다.")

calcApp1=Calculator('cacio','black',*(tuple(map(int,input('숫자 입력').split()))))
resu(calcApp1)

calcApp2=Calculator('cacio','black',*(map(int,input('숫자 입력').split())))
resu(calcApp2)

calcApp3=Calculator('cacio','black',1,2,3,4,5,6,7)
resu(calcApp3)