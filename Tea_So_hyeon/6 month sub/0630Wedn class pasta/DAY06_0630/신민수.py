# -----------------------------------------------------------------------------
# 파스타 요리 프로그램
# 클래스명 : Pasta
# 변수 : 면, 소스, 채소, 육류, 해물
# 함수 : 재료 손질, 면 삶기, 볶기
# ------------------------------------------------------------------------------
class Pasta:

    def __init__(self,noodle,sauce,vegetable,meat,seafood):
        self.noodle=noodle
        self.sauce=sauce
        self.vegetable=vegetable
        self.meat=meat
        self.seafood=seafood

    def cut(self):
        print(f"{self.vegetable},{self.meat},{self.seafood}를 손질한다.")

    def boil(self):
        print(f"{self.noodle}을 8분간 삶는다.")

    def fry(self):
        print(f"삶던 {self.noodle}을 꺼내서 손질한 재료에 {self.sauce}를 얹어 볶는다.")

    def serving(self):
        print(f"손님에게 완성된 파스타를 서빙한다.")

print("--------- 파스타 만들기 ----------")
noodle_input=input("재료 입력(면): ")
sauce_input=input("재료 입력(소스): ")
meat_input=input("재료 입력(고기): ")
vegetable_input=input("재료 입력(야채): ")
seafood_input=input("재료 입력(해물): ")

print("---------- 요리 시작 -----------")
order = Pasta(noodle_input,sauce_input,meat_input,vegetable_input,seafood_input)
order.cut()
order.boil()
order.fry()

print("---------- 파스타 완성 -----------")
order.serving()
