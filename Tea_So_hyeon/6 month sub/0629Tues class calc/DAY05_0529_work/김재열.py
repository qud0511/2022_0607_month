#----------------
# 계산기 프로그램
# 필수 조건 : 계산기 클래스
#----------------------------
class calculator:

    # 인스턴스 생성자
    def __init__(self, maker, color, data=0):
        self.maker=maker
        self.color=color
        self.data=data


    # getter/setter 메서드(선택)
    def getDAta(self): return self.data
    def setData(self, *data): self.data = data


    # 내가원하는 계산기 기능 ---------------------------------
    def plus(self,num):
        self.data+=num
        print(f'plus=> {self.data}')

    def minus(self,num):
        self.data-=num
        print(f'plus=> {self.data}')

    def mult(self,num):
        self.data*=num
        print(f'plus=> {self.data}')

    def div(self,num):
        self.data/=num
        print(f'plus=> {self.data}')



    # 사용자 인터페이스(UI) 기능 메서드
    def showUI(self):
        print('***계산기***')
        print('1. 덧셈')
        print('2. 뺼셈')
        print('3. 곱셈')
        print('4. 나눗셈')
        print('5. 종료')
        print('************')

#----------------------------------------------
calcApp=calculator('sharp', 'pink')

num=int(input('시작값을 입력하세요:'))
while True:
    calcApp.showUI()
    select=input('메뉴선택 :')

    if select =='5' :break

    elif select=='1':
        num=int(input('숫자를 입력해주세요 :'))
        calcApp.plus(num)

    elif select=='2':
        num=int(input('숫자를 입력해주세요 :'))
        calcApp.minus(num)

    elif select=='3':
        num=int(input('숫자를 입력해주세요 :'))
        calcApp.mult(num)

    elif select=='4':
        num=int(input('숫자를 입력해주세요 :'))
        calcApp.div(num)
