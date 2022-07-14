# 사용자한테 데이터를 받는 함수는 추후 작성할 예정입니다..
# ------------------------------------------------
# 계산기 프로그램
# 필수 조건 : 계산기 클라스
# ---------------------------------------------------------
# 클래스명  => Calculator
# 속   성  => 상표, 색깔, 숫자(입력값 변동)
# 역   할  => 더하기, 뺴기, 곱하기, 나누기
# ------------------------------------------------
class Calculator:

    # 인스턴스 생성자
    def __init__(self, maker, color, *data):     # data는 가변변수이므로 *을 찍어줌 (튜플로 받음, *data=None)
        self.maker = maker
        self.color = color
        self.data = data

    # getter/setter 메서드 (선택)                         # 인스턴스에 저장된 속성(변수)값 읽어오는 메서드
    def getData(self):
        return self.data

    def setData(self, *data):                     # 인스턴스에 저장된 속성(변수)값 저장하는 메서드
        self.data = data

    # 내가 원하는 계산기 기능
    def plus(self):                             # 덧셈
        result = 0
        for i in self.data:
            result += i
        return result

    def minus(self):                             # 뺄셈
        result = self.data[0]
        for i in self.data[1:]:
            result -= i
        return result

    def mul(self):                             # 곱셈
        result = 1
        for i in self.data:
            result *= i
        return result

    def div(self):                             # 나눗셈
        try:
            result = self.data[0]
            for i in self.data[1:]:
                result /= i
            return result
        except Exception:
            print("0으로 나눌 수 없습니다.")

    # 사용자 인터페이스(CUI) 기능 메서드 (사용자한테 보여주는 기능)
    def showUI(self):
        print("***** 계산기 *****")
        print("1. 덧셈")
        print("2. 뺄셈")
        print("3. 곱셈")
        print("4. 나눗셈")
        print("5. 종료")
        print("*****************")


# -----------------------------------------------------------
calcApp=Calculator('shap', 'pink', None)

# 루틴 (5번 입력 되기 전까지 메뉴 계속 돌아가도록)
while True:
    calcApp.showUI()
    calcApp.setData(8,2,2)
    select=input("메뉴 선택 : ")

    if select == '5': break
    elif select == '1':                 # 덧셈
        print(calcApp.plus())
    elif select == '2':                 # 뺄셈
        print(calcApp.minus())
    elif select == '3':                 # 곱셈
        print(calcApp.mul())
    elif select == '4':                 # 나눗셈
        print(calcApp.div())
    else:
        print("없는 메뉴입니다. 다시 입력하세요.")


        # 첫 화면은 0 , 사칙연산할 숫자 받기(setData), 덧셈 메서드 부르기