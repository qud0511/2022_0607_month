import time


class spagett():

    import time as t

    def __init__(self, kind, price, noodle, ingrd, sauce):
        self.kind = kind
        self.price = price
        self.noodle = noodle
        self.ingrd = ingrd
        self.sauce = sauce

    menuKind = {'1':'알프레도', '2':'볼로네제', '3':'아라비아타', '4':'로제', '5':'알리오 올리오'}
    menuPrice = {'1':'5000', '2':'5000','3':'5000','4':'5000','5':'5000'}
    # ------원하는 기능

    def munu_1(self):
        print("-----------------------")
        print("        메 뉴 판         ")
        print("   1. 알프레도   5000     ")
        print("   2. 볼로네제   6000     ")
        print("  3. 아라비아타   5000     ")
        print("   4. 로제     6000      ")
        print("   5. 알리오 올리오 5000    ")
        print("-----------------------")

    def menu_2(self, kind):
        print(f"{self.menuKind[kind]}를 선택하셨습니다.")
        print(f"{self.menuPrice[kind]}원 입니다.")
        print(f"{self.menuKind[kind]} 조리를 시작합니다.")
        time.sleep(1)

    def boil(self):
        print("물을 끓인다.")
        time.sleep(1)

    def sarmda(self, kind):
        print(f"{self.menuKind[kind]} 면을 삶는다.")
        time.sleep(1)

    def sonjil(self, kind):
        print(f"{self.menuKind[kind]} 재료를 손질한다.")
        time.sleep(1)

    def bokda(self, kind):
        print(f"{self.menuKind[kind]} 소스로 볶는다.")
        time.sleep(1)

    def meokda(self):
        print("먹는다.")

spag = spagett(' ', ' ', ' ', ' ', ' ')

while True:
    spag.munu_1()
    select = input("메뉴를 선택해주세요.: ")
    spag.menu_2(select)
    spag.boil()
    spag.sarmda(select)
    spag.sonjil(select)
    spag.bokda(select)
    spag.meokda()
    quit()
    