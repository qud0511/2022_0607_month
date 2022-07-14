# pastaApp 클래스 ------------------------------------------------------------
# 속성/특징 ==> 필드(Field) : 면, 소스, 고기
# 역할/기능 ==> 준비, 요리, 먹기
# -------------------------------------------------------------------------

# 파스타가 가지고있는 속성/특징

class pastaApp:
    def __init__(self, noodle, sauce, spicy, meat, food):
        self.noodle = noodle
        self.sauce = sauce
        self.spicy = spicy
        self.meat = meat
        self.food = food


# 파스타가 할 수 있는 역할/기능

    def ready(self):
        print(f'[ {self.sauce}{self.spicy}{self.meat}{self.noodle} ]주문이 접수되었습니다.')

    def cook(self):
        print(f'주문하신 음식이 조리중입니다.')
        print('♬')
        print('♩')
        print('♪')
        print('♬')

    def eat(self):
        food = ''
        for i in self.food:
            food+=i+', '
        food=food[:-2]
        print(f'{self.sauce}{self.spicy}{self.meat}{self.noodle}가 완성되었습니다. 맛있게드세요!')




# 기능관련 함수 --------------------------------------------------------------
def pasta():

        noodle1=input('[스파게티, 링귀니, 펜네, 라자냐] 면 선택: ')
        spicy1=input('[엄청매운, 매운, 보통, 안매운] 맵기 선택: ')
        sauce1=input('[토마토, 봉골레, 크림, 로제, 알리오올리오] 소스 선택: ')
        meat1=input('[돼지고기, 닭고기, 소고기, 생선] 고기를 선택해주세요: ')
        pastalist=[]

        while True:
            food1=input('[양송이, 새우, 브로콜리] \n (선택완료시 완료를 입력해주세요) \n 추가재료를 선택해주세요: ')
            if food1 in ['완료']: break
            else:
                pastalist += [food1]

        pasta1=pastaApp(noodle1,spicy1,sauce1,meat1,pastalist)
        pasta1.ready()
        pasta1.cook()
        pasta1.eat()

if __name__ == '__main__':
    pasta()

