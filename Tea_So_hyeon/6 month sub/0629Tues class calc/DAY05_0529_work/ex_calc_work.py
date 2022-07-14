# ----------------------------------------
# 계산기 프로그램
# 필수 조건 : 계산기 클래스
# ----------------------------------------
class Calculator:
    # 인스턴스 생성자
    def __init__(self, maker, color, *data):
        self.maker=maker
        self.color=color
        self.data=data

    # getter/setter메서드 (선택)
    def getData(self): return self.data
    def setData(self, *data): self.data = data

    # 내가 원하는 계산기 기능 --------------------
    def puls(self):
        print(f'puls => {self.data}')

    # 사용자 인터페이스(CUI) 기능 메서드
    def showUI(self):
        print("***** 계산기 *****")
        print("1. 덧셈")
        print("2. 뺄셈")
        print("3. 종료")
        print("*****************")

# -------------------------------------------------------
calcApp=Calculator('Shap','Pink', None)

while True:
    calcApp.showUI()
    select= input("메뉴 선택")

    if select == '3': break

    elif select == '1':
        calcApp.puls()