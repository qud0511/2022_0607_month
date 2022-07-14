# ----------------------------------
class spaghetti:

    def __init__(self, sauce, water, dish, pasta, bowl =['양파', '돼지고기', '피망', '버섯']):
        self.pasta = pasta
        self.water = water
        self.bowl = bowl
        self.sauce = sauce
        self.dish = dish

    def order(self):
        menu = input("1. 토마토소스 / 2. 크림소스")
        if menu == '1':
            self.sauce = '토마토소스'
            self.pasta = input('파스타면을 적어 ㅇㅇ')
        elif menu == '2':
            self.sauce = '크림소스'
            self.pasta = input('파스타면을 적어 ㅇㅇ')

    def ready(self, bowl):
        a = []
        for f in self.bowl:
            f = '손질한 ' + f
            a.append(f)
        return a

    def putPasta(self, pasta):
        self.pasta = '적절히 익힌 ' + self.pasta

    def stirfry(self, sauce, bowl, pasta):
        self.pasta = self.pasta.split(' ')
        print(self.pasta)
        self.dish = self.sauce + ' ' + self.pasta[2]

    def cook(self):
        self.order()
        self.bowl = self.ready(self.bowl)
        print(self.bowl)
        self.putPasta(self.pasta)
        print(self.pasta)
        self.stirfry(self.bowl, self.sauce, self.pasta)
        print(self.dish)

App = spaghetti(None, None, None, None)

App.cook()