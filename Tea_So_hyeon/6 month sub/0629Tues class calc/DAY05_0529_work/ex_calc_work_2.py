# ---------------------------------------------------------------------------
# 계산기 프로그램 만들기 - 2
# --------------------------------------------------------------------------
# 필수 조건 : 계산기 클래스 생성 후 사용
# --------------------------------------------------------------------------
# 클 래 스 명    : Calculator
# 속성/필드/변수 : 제조사, 색상
# 역할/기능     : 인스턴스 생성하는 생성자 메서드 => __init__(제조사, 색상)
#               연산 기능 메서드 => 사용자로부터 연산 데이터 전달 받아 사용
#                                더하기(데이터), 빼기(데이터), 곱하기(데이터), 나누기(데이터)
#               기타 기능 메서드 => 메뉴출력()
# -------------------------------------------------------------------------
class Calculator:
    # 인스턴스 생성자
    def __init__(self, maker, color):
        self.maker=maker
        self.color=color

    # getter/setter메서드 (선택)

    # 내가 원하는 계산기 기능 --------------------
    def puls(self, data):
        return sum(data)

    def minus(self,data):
        result=0
        for idx, num in enumerate(data):
           result= num  if idx==0 else result-num
        return result

    def multi(self, data):
        result = 1
        for num in data: result *= num
        return result

    def div(self, data):
        result=0
        for idx in range(len(data)-1):
            if data[idx+1] == 0: break
            result = data[idx] / data[idx+1] if idx == 0 else result / data[idx+1]
        return result

    # 사용자 인터페이스(CUI) 기능 메서드
    def showUI(self):
        print("***** 계산기 *****")
        print("1. 덧         셈")
        print("2. 뺄         셈")
        print("3. 곱         셈")
        print("4. 나     눗  셈")
        print("5. 종         료")
        print("*****************")

# 기능 관련 메서드 ---------------------------------------------------
# 연산에 사용할 숫자 데이터 입력 받는 함수
def getNumbers():
    nums = []
    while True:
        num = input('계산 할 숫자 입력(종료 Q/q) : ')
        if num in ['q', 'Q']: break
        nums.append(int(num))
    return nums

# 계산기 프로그램 구동하는 함수
def playApp():
    calcApp = Calculator('Shap', 'Pink')

    print('--------------START--------------')
    while True:
        calcApp.showUI()
        select = input("메뉴 선택 : ")

        if select == '5':
            break
        elif select == '1':
            print(f'덧  셈 결과 : {calcApp.puls(getNumbers())}')
        elif select == '2':
            print(f'뺄  셈 결과 : {calcApp.minus(getNumbers())}')
        elif select == '3':
            print(f'곱  셈 결과 : {calcApp.multi(getNumbers())}')
        elif select == '4':
            print(f'니눗셈 결과 : {calcApp.div(getNumbers())}')
    print('--------------END---------------')

# -------------------------------------------------------------
if __name__ == '__main__':
    playApp()