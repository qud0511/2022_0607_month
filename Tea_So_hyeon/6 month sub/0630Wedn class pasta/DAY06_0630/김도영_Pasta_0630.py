# 클래스를 사용하여 스파게티 만들기
# 속성/필드/변수 : 면, 재료, 소스
# 역할/기능     : 면 삶기, 재료 손질하기, 볶기, 먹기
class Pasta:

    # 인스턴스 생성자
    def __init__(self,ingredient='',sauce='',noodle=''):
        self.noodle=noodle
        self.sauce=sauce
        self.ingredient=ingredient

    # getter/setter 메서드 (선택)
    def getIngredient(self): return self.ingredient
    def setIngredient(self,ingredient): self.ingredient=ingredient

    def getNoodle(self): return self.noodle
    def setNoodle(self,noodle): self.noodle=noodle

    def getSauce(self): return self.sauce
    def setSauce(self,sauce): self.sauce=sauce

# -------------------------------------------------------------------------
    # 면 삶기
    def water(self):
        print(f'{self.noodle}을 삶습니다')


    # 재료 손질하기
    def repair(self):
        print(f'{self.ingredient}를 깨끗이 손질합니다.')

    # 요리
    def cook(self):
        print(f'{self.ingredient}와 {self.noodle}, {self.sauce} 소스를 볶아 요리합니다.')

    # 먹기
    def eat(self):
        print(f'완성된 {self.sauce} 파스타를 맛있게 먹습니다.')

# -------------------------------------------------------------------------

def Info():
    print('**********스파게티**********')
    print('      1. 면  삶  기')
    print('      2. 재료 손질하기')
    print('      3. 요 리 하 기')
    print('      4. 먹      기')
    print('      5. 종      료')
    print('**************************')


# 기능 관련 함수

def getIngredient():
    list = []
    print('넣을 재료를 모두 골라주세요!\n1.마늘     2.베이컨     3.양파     4.파프리카\n5.새우     6.고추     7.종료')
    while True:
        a = input('몇 번 하시겠습니까? ')
        if a == '1': list.append(str('마늘'))
        elif a == '2': list.append('베이컨')
        elif a == '3': list.append('양파')
        elif a == '4': list.append('파프리카')
        elif a == '5': list.append('새우')
        elif a == '6': list.append('고추')
        else: break
    return list

def getMun():
    while True:
        print('면의 굵기를 골라주세요!\n1.굵은 면     2.중간 면     3.얇은 면')
        a=input('몇 번 하시겠습니까? ')
        if a=='1': return '굵은 면'
        elif a=='2': return '중간 면'
        elif a=='3': return '얇은 면'
        else: break

def getSor():
    while True:
        print('소스를 골라주세요!\n1.크림     2.토마토     3.오일')
        a=input('몇 번 하시겠습니까? ')
        if a=='1': return '크림'
        elif a=='2': return '토마토'
        elif a=='3': return '오일'
        else: break

# 요리 시작하는 함수

def play():
    spa=Pasta()

    while True:
        Info()
        n=input('메뉴를 입력하세요: ')
        if n == '5': break
        elif n == '1':
            spa.setNoodle(getMun())
            spa.water()
        elif n == '2':
            spa.setIngredient(getIngredient())
            spa.repair()
        elif n == '3':
            spa.setSauce(getSor())
            spa.cook()
        elif n == '4':
            spa.eat()


play()