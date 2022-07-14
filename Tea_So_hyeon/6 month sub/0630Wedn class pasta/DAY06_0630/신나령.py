# 스파게티 클래스
# 면, 소스, 채소, 기타재료
# 물 끓이기, 면 삶기, 재료 손질하기, 볶기, 먹기

import time as t

class Spaghetti:
    def __init__(self,noodle,sauce,veggie,*etc):
        self.noodle=noodle
        self.sauce=sauce
        self.veggie=veggie
        self.etc=etc

    # 물 끓이기
    def heat(self):
        print('\n물 끓이는 중...')

    # 면 삶기
    def boil(self):
        print(f'{self.noodle} 삶는 중...')

    # 재료 손질하기
    def cut(self):
        print(f'{self.veggie}, {self.changeData()} 손질 중...')

    # 볶기
    def fri(self):
        print(f'프라이팬에 {self.noodle}, {self.sauce}, {self.veggie}, {self.changeData()} 넣고 볶는 중...')

    def changeData(self):
        i=0
        result=''
        data=list(self.etc)
        while i<=len(self.etc):
            if i==len(self.etc):
                result=result+data[0][i]
            else:
                result=result+data[0][i]+', '
            i+=1
        return result

    # 먹기
    def eat(self):
        print(f'{self.sauce}파스타가 완성되었습니다. 맛있게 드세요~')

def choose():
    custom=input('원하시는 면, 소스, 채소, 추가 재료를 입력해 주세요.(ex 스파게티, 토마토, 가지, 버섯, 파슬리) ')
    custom=custom.split(', ')
    ingredient=[]
    for i in custom:
        ingredient.append(i)

    cook=Spaghetti(ingredient[0],ingredient[1],ingredient[2],ingredient[3:])
    cook.heat()
    t.sleep(0.8)
    cook.boil()
    t.sleep(0.8)
    cook.cut()
    t.sleep(0.8)
    cook.fri()
    t.sleep(0.8)
    cook.eat()

choose()