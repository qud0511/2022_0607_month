# ------------------------------------------------------------
# 스파게티 클래스
# 면, 소스, 채소, 기타 재료
# 면 삶기, 재료 손질하기, 볶기, 먹기
class spaghetti:
    def __init__(self, noodle, source, vegetable):
        self.noodle=noodle
        self.source=source
        self.vegetable=vegetable

    # 재료 손질하기
    def cook_vegetable(self):
        print(f'{self.vegetable} 손질중...')

    # 면 삶기
    def cook_noodle(self):
        print(f'{self.noodle}면 삶는중...')

    # 볶기
    def cook_all(self):
        print(f'{self.noodle}면, {self.source}소스, {self.vegetable} 볶는중...')

    # 완성
    def finish(self):
        print('요리 완성!')

    # 먹기
    def eat(self):
        print('냠냠')
# 여기 있는(클래스 안에 있는) 메서드들은 객체 생성 안하면 못씀

# -------------------------------------------------------------

# 메뉴 보여주기
def showMenu():
    print('---메뉴를 선택하세요---')
    print('1. 토마토 스파게티')
    print('2. 로제 스파게티')
    print('3. 크림 스파게티')
    print('4. 종료')

# 준비
def cook(dinner):
    dinner.cook_vegetable()
    dinner.cook_noodle()
    dinner.cook_all()
    dinner.finish()
    dinner.eat()

# 요리
def dish():
    while True:
        showMenu()
        dishName=input("메뉴의 번호를 입력하세요 : ")
        if dishName=='4': break
        elif dishName=='1':
            dinner = spaghetti('thin', 'tomato', 'onion')
            cook(dinner)
        elif dishName=='2':
            dinner=spaghetti('middle', 'rose', 'broccoli')
            cook(dinner)
        elif dishName=='3':
            dinner=spaghetti('ribbon', 'cream', 'mushroom')
            cook(dinner)

dish()



