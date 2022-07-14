import time
import os


class Spaghetti:
    menu_list = {'알리오 올리오': {'noddle' : '스파게티 면', 'source' :'올리브 오일에 페퍼론치노', 'vege' : '파슬리', 'sub': '파마산 치즈, 후추' }}
    def __init__(self, order):
        self.spaghetti = order
        self.noddle = Spaghetti.menu_list[order]['noddle']
        self.source = Spaghetti.menu_list[order]['source']
        self.vege = Spaghetti.menu_list[order]['vege']
        self.sub = Spaghetti.menu_list[order]['sub']



    def makeSpaghetti(self):
        self.makeNoddle()
        self.makeSource()
        self.panVege()
        self.addSub()
        print(f'주문하신 {self.spaghetti} 나왔습니다.')

    # 면 삶기
    def makeNoddle(self):
        taking_str = f'{self.noddle} 삶는 중...'
        self.cookdelay(taking_str, 8)

    # 소스 준비하기
    def makeSource(self):
        taking_str = '마늘 볶는 중...'
        self.cookdelay(taking_str, 2)

    # 야채 볶기
    def panVege(self):
        taking_str = f'{self.vege} 볶는 중...'
        self.cookdelay(taking_str, 4)

    # 추가재료
    def addSub(self):
        taking_str = f'{self.sub} 뿌리는 중...'
        self.cookdelay(taking_str, 1)


    def cookdelay(self,taking_str, delaytime):
        for i in range(10):
            time.sleep(delaytime / 10)
            print(f'{taking_str} : [', end = '')
            for j in range(i):
                print('■', end = '')
            for j in range(10 - i):
                print(' ', end = '')
            print(f']{i * 10}%')
        print(f'{taking_str} : [■■■■■■■■■■]100%\n')


def getMenu():
    menu = '''
- han's kitchen ----------
    menu
        알리오 올리오
--------------------------
    '''
    print(menu)

    order = input('주문 입력 : ')
    return order

if __name__ == '__main__':
    while True:
        order = getMenu()
        if order == '안사요':
            break
        try:
            take = Spaghetti(order)

            take.makeSpaghetti()
        except:
            print('그런거 안 팔아요')

