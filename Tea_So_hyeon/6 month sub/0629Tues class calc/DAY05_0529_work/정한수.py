
# 계산기 프로그램 with 계산기 클래스

class Calculator:

    def __init__(self, maker, color, *data):
        self.maker = maker
        self.color = color
        self.data = data


    def getData(self):
        return self.data

    def setData(self, *data):
        self.data = data

    # 사칙연산
    def plus(self):
        if len(self.data)>1:
            form = ' + '.join(self.data )
            print(form + f' = {eval(form)}')
        elif len(self.data) == 1:
            print(self.data)
        else:
            print('There Is No Data')
            s = self.input_list()
            self.setData(*s)
            self.plus()

    def minus(self):
        if len(self.data)>1:
            form = ' - '.join(self.data )
            print(form + f' = {eval(form)}')
        elif len(self.data) == 1:
            print(self.data)
        else:
            print('There Is No Data')
            s = self.input_list()
            self.setData(*s)
            self.minus()


    def multi(self):
        if len(self.data)>1:
            form = ' * '.join(self.data )
            print(form + f' = {eval(form)}')
        elif len(self.data) == 1:
            print(self.data)
        else:
            print('There Is No Data')
            s = self.input_list()
            self.setData(*s)
            self.multi()


    def div(self):
        if '0' in self.data[1:]:
            print('div error')
        elif len(self.data)>1 and  (self.data[1] != 0) :
            form = ' / '.join(self.data )
            print(form + f' = {eval(form)}')
        elif len(self.data) == 1:
            print(self.data)
        else:
            print('There Is No Data')
            s = self.input_list()
            self.setData(*s)
            self.div()


    # 사용자 인터페이스 CUI
    def showUI(self):
        print("******** 계 산 기 ********")
        print("        1.  덧  셈")
        print("        2.  뺄  셈")
        print("        3.  곱  셈")
        print("        4. 나 눗 셈")
        print("        5. 값 입 력")
        print("        6.  종  료")
        print("*************************")


    # 실제 계산기 처럼 동작 시키기
    def real_cal(self):
        self.result = 0
        self.formula_str = ''

        while True:
            print(self.result)
            input_data = input('숫자, 연산자 단위로 입력 : ')
            self.formula_str = self.formula_str + ' ' + input_data
            if input_data.isnumeric():
                formula_str = self.formula_str


            if input_data == '=':
                print(formula_str + ' = ' + str(eval(self.formula_str[:-2])))
                break

            try:
                self.result = eval(self.formula_str)
                self.formula_str = str(self.result)
            except:
                self.result = self.formula_str

    def input_list(self):
        s = []
        while True:
            g = input('한개 씩 값 입력 (중단 : x) : ')
            if g == 'x':
                break
            s.append(g)
        return s

if __name__ == '__main__':
    my_calc = Calculator('shaomi', 'black')

    while True:
        my_calc.showUI()
        choice = input('메뉴 선택 : ')

        if choice == '1':
            my_calc.plus()
        elif choice == '2':
            my_calc.minus()
        elif choice == '3':
            my_calc.multi()
        elif choice == '4':
            my_calc.div()
        elif choice == '5':
            s = my_calc.input_list()
            my_calc.setData(*s)
        elif choice == '6':
            break

    my_calc.real_cal()
