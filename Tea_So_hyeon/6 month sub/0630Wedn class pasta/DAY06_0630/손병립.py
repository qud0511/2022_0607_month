# 스파게티 클래스

class Pasta:

    def __init__(self,noodle,sauce,food):
        self.noodle=noodle
        self.sauce=sauce
        self.food=food


    # 내가 원하는 기능

    def readyFood(self):
        food = ''
        for i in self.food:
            food+=i+', '
        food=food[:-2]
        print(f'{food}가 들어간 {self.sauce} {self.noodle} 파스타 준비중')

    def boilNoodle(self):
        print(f'{self.noodle} 삶는중')

    def cook(self):
        food = ''
        for i in self.food:
            food += i + ', '
        food = food[:-2]
        print(f'{food}가 들어간 {self.sauce} {self.noodle} 파스타 볶는중')

    def eat(self):
        print(f'{self.sauce} {self.noodle} 파스타 완성!\n맛있게 드세요.')

# 기능 구현 함수
def pasta():

    noodle1=input('스파게티, 마카로니, 펜네, 콘킬리에, 라자냐\n면을 선택해주세요:')
    sauce1=input('토마토, 크림, 로제, 알리오올리오\n소스를 선택해주세요:')
    foodlist=[]
    while True:
        food1=input('양송이, 베이컨, 새우, 마늘, 치즈\n종료(q/Q)\n추가재료를 선택해주세요:')
        if food1 in ['q','Q']: break
        else:
            foodlist+=[food1]
    pasta1=Pasta(noodle1,sauce1,foodlist)
    print('.')
    print('.')
    pasta1.readyFood()
    print('.')
    print('.')
    pasta1.boilNoodle()
    print('.')
    print('.')
    pasta1.cook()
    print('.')
    print('.')
    pasta1.eat()

# 기능 구현
if __name__ == '__main__':
    pasta()