class Calculator:
    
    def __init__(self, maker, color):
        self.maker = maker
        self.color = color
    
    
    def getData(self): return self.data
    def setData(self, data): self.data = data
    
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
    
    def multi(self, *data):
        multi = data[0]
        for i in range(1, len(data)):
            multi = multi * data[i]
        print(multi)
    
    def div(self, *data):
        div = data[0]
        for i in range(1, len(data)):
            div = div / data[i]
        print(div)
    
    def showUi(self):
        print('*******계산기*******')
        print('     1. 덧셈'        )
        print('     2. 뺄셈'        )
        print('     3. 곱셈'        )
        print('     4. 나눗셈'      )
        print('     5. 종료'        )
        print('********************')


myCal = Calculator('sharp', 'pink')
while True:
    myCal.showUi()
    select = input()
    if select == '5':
        break
    elif select == '1':
        myCal.plus(10, 4, 7, 6)
    elif select == '2':
        myCal.minus(15, 6, 2, 4)
    elif select == '3':
        myCal.multi(5, 5, 5, 7)
    elif select == '4':
        myCal.div(70, 3, 2, 3)