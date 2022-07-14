# ---------------------------------------------------------------------------
# 계산기 프로그램 만들기 - 1
# --------------------------------------------------------------------------
# 필수 조건 : 계산기 클래스 생성 후 사용
# --------------------------------------------------------------------------
# 클 래 스 명    : Calculator
# 속성/필드/변수 : 제조사, 색상, 데이터
# 역할/기능     : 인스턴스 생성하는 생성자 메서드 => __init__(제조사, 색상, 데이터)
#               연산 기능 메서드 => Calculator 인스턴스에 저장된 데이터 사용 연산
#                                더하기(), 빼기(), 곱하기(), 나누기()
#               기타 기능 메서드 => 메뉴출력()
# -------------------------------------------------------------------------
class Calculator:
    # 인스턴스 생성자
    def __init__(self, maker, color, *data):
        self.maker=maker
        self.color=color
        self.data=data

    # getter/setter메서드 (선택)
    def getData(self): return self.data
    def setData(self, data): self.data = data

    # 내가 원하는 계산기 기능 --------------------
    def puls(self):
        return sum(self.data)

    def minus(self):
        result=0
        for idx, num in enumerate(self.data):
           result= num  if idx==0 else result-num
        return result

    def multi(self):
        result = 1
        for num in self.data: result *= num
        return result

    def div(self):
        result=0
        for idx in range(len(self.data)-1):
            if self.data[idx+1] == 0: break
            result = self.data[idx] / self.data[idx+1] if idx == 0 else result / self.data[idx+1]
        return result

    # 계산 데이터 입력 받는 메서드
    def inputData(self):
        nums = []
        while True:
            num = input('계산 할 숫자 입력(종료 Q/q) : ')
            if num in ['q', 'Q']: break
            nums.append(int(num))
        self.data=nums

    # 사용자 인터페이스(CUI) 기능 메서드
    def showUI(self):
        print("***** 계산기 *****")
        print("1. 덧         셈")
        print("2. 뺄         셈")
        print("3. 곱         셈")
        print("4. 나     눗  셈")
        print("5. 종         료")
        print("*****************")

# 기능 관련 함수 ---------------------------------------------------
# 연산에 사용할 숫자 데이터 입력 받는 함수
def getNumbers():
    nums = []
    while True:
        num = input('계산 할 숫자 입력(종료 Q/q) : ')
        if num in ['q', 'Q']: break
        nums.append(int(num))
    return nums

# 계산기 프로그램 구동하는 함수 ---------------------------------
def playApp():
    calcApp = Calculator('Shap', 'Pink')

    print('--------------START--------------')
    while True:
        calcApp.showUI()
        select = input("메뉴 선택 : ")
        if select == '5': break
        elif select == '1':
            calcApp.setData(getNumbers())
            print(f'덧  셈 결과 : {calcApp.puls()}')
        elif select == '2':
            calcApp.setData(getNumbers())
            print(f'뺄  셈 결과 : {calcApp.minus()}')
        elif select == '3':
            calcApp.setData(getNumbers())
            print(f'곱  셈 결과 : {calcApp.multi()}')
        elif select == '4':
            calcApp.setData(getNumbers())
            print(f'니눗셈 결과 : {calcApp.div()}')
    print('--------------END---------------')

# -------------------------------------------------------------
if __name__ == '__main__':
    playApp()