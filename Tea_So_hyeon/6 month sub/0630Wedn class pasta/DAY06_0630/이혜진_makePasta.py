# ------------- 파스타 만들기 프로그램 만들기 -------------------------
# 클래스명 : Pasta
# 속성/특징/변수 : 면, 소스, 채소, *기타
# 역할/기능/함수
#     - 계산기 인스턴스 생성 메서드 ==> __init__()
#     - 계산기 속성/특징 값 읽기 => getter, setter
#     - 기능 메서드 => 재료손질, 물끓이기, 면삶기, 볶기, 먹기
# ---------------------------------------------------------
class Pasta():
    # 인스턴스 생성자
    def __init__(self,noodle,sauce,vegetable):
        self.noodle=noodle
        self.sauce=sauce
        self.vegetable=vegetable

    # 내가 원하는 파스타 만드는 기능

    # 재료손질
    def material(self):
        vegetable=['onion','tomato']
        print(f'{vegetable}가 들어간 {self.noodle} {self.sauce} 파스타를 준비중')

    def boil(self):
        print("면을 끓인다")

    def fry(self):
        print("소스랑 볶는다")

    def eat(self):
        print("맛있게 먹는다")


pasta=Pasta('basic','tomato','onion')          #객체생성인거임?
pasta.material()
pasta.boil()
pasta.fry()
pasta.eat()


