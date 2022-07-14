# 계산기 프로그램 만들기
# 필수조건 계산기 class
class Calc:

    # instance -------------------------------------------------------------------------
    def __init__(self, maker, color):
        self._maker = maker
        self._color = color
        self.total = 0  # 총계


    # getter/setter method --------------------------------------------------------------
    def getMaker(self):
        return self._maker

    def getClolr(self):
        return self._color


    # user method ------------------------------------------------------------------------
    # 함수명 : plus
    # 파라미터 : datas
    # 기능 : 입력받은 숫자리스트를 숫자가 하나면 total에 더하고, 두개이상이면 전부 더하고 total에 더할지 물어보고 실행
    # 결과값 : none
    def plus(self, datas):
        try:
            add = 0
            for d in datas:
                add = add + d
            if len(datas) == 1:  # 입력값이 한개일때 총계에 바로 더함
                self.total = self.total + add
            else:  # 입력값이 여러개일때 일단 계산값 보여준 후 반영할지 여부물어봄
                print(f'현재 결과는 {add} 입니다.')
                r = input('총계에 반영하시겠습니까?(y/n): ')
                if r == 'y':
                    self.total = self.total + add
        except Exception:
            print('올바른 숫자를 입력해 주세요.')


    # -------------------------------------------------------------
    # 함수명 : minus
    # 파라미터 : datas
    # 기능 : 입력받은 숫자리스트를 숫자가 하나면 total에서 빼고, 두개이상이면 순서대로 빼고 total에서 뺄지 물어보고 실행
    # 결과값 : none
    def minus(self, datas):
        try:
            minus = datas[0]
            for d in datas[1:]:
                minus = minus - d
            if len(datas) == 1:
                self.total = self.total - minus
            else:
                print(f'현재 결과는 {minus} 입니다.')
                r = input('총계에 반영하시겠습니까?(y/n): ')
                if r == 'y':
                    self.total = self.total - minus
        except Exception:
            print('올바른 숫자를 입력해 주세요.')


    # -------------------------------------------------------------
    # 함수명 : div
    # 파라미터 : datas
    # 기능 : 입력받은 숫자리스트를 숫자가 하나면 total에 곱하고, 두개이상이면 전부 곱하고 total에 곱할지 물어보고 실행
    # 결과값 : none
    def div(self, datas):
        try:
            div = datas[0]
            for d in datas[1:]:
                div = div / d
            if len(datas) == 1:
                self.total = self.total / div
            else:
                print(f'현재 결과는 {div} 입니다.')
                r = input('총계에 반영하시겠습니까?(y/n): ')
                if r == 'y':
                    self.total = self.total / div

        except ZeroDivisionError:
            print('0으로 나눌수 없습니다.')

        except Exception:
            print('올바른 숫자를 입력해 주세요.')


    # -------------------------------------------------------------
    # 함수명 : multi
    # 파라미터 : datas
    # 기능 : 입력받은 숫자리스트를 숫자가 하나면 total을 나누고, 두개이상이면 순서대로 나누고 total을 나눌지 물어보고 실행
    # 결과값 : none
    def multi(self, datas):
        try:
            multi = 1
            for d in datas:
                multi = multi * d
            if len(datas) == 1:
                self.total = self.total * multi
            else:
                print(f'현재 결과는 {multi} 입니다.')
                r = input('총계에 반영하시겠습니까?(y/n): ')
                if r == 'y':
                    self.total = self.total * multi

        except Exception:
            print('올바른 숫자를 입력해 주세요.')


    # -------------------------------------------------------------
    # 함수명 : reset
    # 파라미터 : none
    # 기능 : 총계 초기화
    # 결과값 : none
    def reset(self):
        self.total = 0
        print('초기화했습니다.', '\n')


    # character user interface ------------------------------------------------------------------------
    def showUI(self):
        print('***** 계산기 *****')
        print(f'* 총 계 : {self.total}')
        print('* 1. 덧  셈')
        print('* 2. 뺄  셈')
        print('* 3. 곱  셈')
        print('* 4. 나 눗 셈')
        print('* 5. 초 기 화 ')
        print('* 6. 종  료 ')
        print('*****************')


# ------------------------------------------------------------------------------------------
# 함수명 : settingData
# 기능 : str을 int list로 전환
# 파라미터 : msg
# 결과값 : list
def settingData(msg):
    try:
        datas = str(msg).split(',')
        datas = [int(i.strip()) for i in datas]
        return datas
    except Exception:
        datas = 'none'
        return datas


# --------------------------------------------------------------------------------------------
# 기능 구현

sonyCalc = Calc('sony','black')

while True:
    sonyCalc.showUI()
    SELC = input('매 뉴 선 택 : ')

    if SELC == '5':
        sonyCalc.reset()

    elif SELC == '1':
        msg = input('더할 숫자 혹은 숫자들 입력(1, ...): ')
        datas = settingData(msg)
        sonyCalc.plus(datas)
        print('\n')

    elif SELC == '2':
        msg = input('뺄 숫자 혹은 숫자들 순서대로 입력(10, ...): ')
        datas = settingData(msg)
        sonyCalc.minus(datas)
        print('\n')

    elif SELC == '3':
        msg = input('곱할 숫자 혹은 숫자들 입력(1, ...): ')
        datas = settingData(msg)
        sonyCalc.multi(datas)
        print('\n')

    elif SELC == '4':
        msg = input('나눌 숫자 혹은 숫자들 순서대로 입력(10, ...): ')
        datas = settingData(msg)
        sonyCalc.div(datas)
        print('\n')

    elif SELC == '6':
        break

    else:
        print('올바른 매뉴를 선택해 주세요.', '\n')

