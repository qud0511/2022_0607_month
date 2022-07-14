class pasta():

    def __init__(self, ingredient, noodle, pastSauce):
        self.ingredient=ingredient
        self.noodle=noodle
        self.pastSauce=pastSauce

    # 원하는 기능/메서드

    def boil(self):
        print("물을 끓이는 중...")

    def boilNoodle(self, noodle):
        print(f"{noodle}을 삶는 중...")

    def prepareIngredient(self, ingredient):
        print(f"{ingredient}를 손질 하는 중...")

    def stirFry(self, pastSauce):
        print(f"{pastSauce}로 볶는 중...")

    def plating(self):
        print("완성.")

    def showMenu(self):
        print('오늘의 메뉴')
        print('1. 알리올리오')
        print('2. 까르보나라')
        print('3. 투움바')

alio = pasta('알리오 면', '알리오 재료', '알리오 소스')

alio.boil()
alio.boilNoodle("부가티니 면")
alio.prepareIngredient("할라피뇨, 마늘")
alio.stirFry("올리브 오일")
alio.plating()

# --------------
# 함수 : 기능 코드 묶음, 클래스와 상관없음
# 기능 구현에 사용되는 재료 - 매개변수(파라미터), 전역변수

num=12          # -> 전역변수, 파라미터됨
    # 파라미터
def ok(name):
    print(f'{num}입니다.')
    print(f'{name}입니다.')

def ok(name):
    global  num
    print(f'{num}입니다.')
    print(f'{name}입니다.')
# ---------------
# 메서드 : 클래스 안에 존재하는 함수
# 객체(인스턴스)에 존재하는 데이터
# 매개변수(파라미터)
# 객체 생성 없이 사용 불가

class Point:

    # 속성/특징 : 필드
    # x, y

    # 역할/기능 : 메서드
    def showPoint(self):
        print(f'{self.x}, {self.y}좌표(위치)에 Point')

    def drawPoint(self, color):
        print(f'{self.x},{self.y}위치에 {color}색상으로 Point 그리기')

# ---------------



