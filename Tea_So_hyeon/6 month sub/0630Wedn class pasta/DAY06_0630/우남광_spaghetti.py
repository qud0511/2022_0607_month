import time
class Pasta:
    def __init__(self, name):
        self.name = name
    def boil(self, who):
        print(f"파스타를 {who}가 삶습니다.")
    def cook(self, who, who2):
        if self.name == "1":   # 알리오 올리오
            print(f'{who}가 팬에 올리브유를 4~5큰술 넣어줍니다.')
            time.sleep(0.8)
            print(f'{who}가 편마늘과 다진마늘, 페퍼론치노를 같이 넣고 섞습니다.')
            time.sleep(0.8)
            print(f'{who2}님을 위한 파스타가 준비되고 있습니다. 잠시만 기다려주세요')
            time.sleep(0.8)
            print(f'{who}가 alio_olio 파스타를 {who2}에게 주었습니다.')
        if self.name == '2':   # 로제 파스타
            print(f'{who}가 양파와 베이컨을 잘게 썹니다.')
            time.sleep(0.8)
            print(f'{who}가 팬에 올리브오일을 넉넉히 두르고 양파 베이컨 다진마늘 새우 등을 넣고 달달 볶습니다.')
            time.sleep(0.8)
            print(f'{who}가 생크림+우유를 넣고 소금 후추 치킨스톡으로 간을 합니다.')
            time.sleep(0.8)
            print(f'{who}가 토마토소스를 3Ts를 넣고 소스를 졸입니다.')
            time.sleep(0.8)
            print(f'{who2}님을 위한 파스타가 준비되고 있습니다. 잠시만 기다려주세요')
            time.sleep(0.8)
            print(f'{who}가 rose 파스타를 {who2}에게 주었습니다.')
    def eat(self, who):
        print(f"파스타를 {who}가 맛있게 먹습니다.")
def menu():
    print("***** 파스타 레스토랑 *****")   # 아직 레스토랑 규모가 작아서 하나씩 메뉴가 나옵니다.
    print("1. alio_olio")
    print("2. rose")
    print("다른 메뉴도 개설 준비중입니다. (나가기:Q)")
    print("*****************")

class Person:
    def __init__(self, name="홍길동"):
        self.name = name

def simulator():
    chef = Person()
    name = input("손님 이름을 입력해주세요: ")
    customer = Person(name)
    while True:
        menu()
        select= input("먹고싶은 파스타를 하나 선택해주세요: ")
        if select in ['1', '2']:
            pasta = Pasta(select)
            pasta.boil(chef.name)
            pasta.cook(chef.name, customer.name)
            pasta.eat(customer.name)
        elif select == 'Q':
            print("손님이 나갑니다. 안녕히 가세요.")
            quit()
        else:
            print("손님을 쫓아냅니다.")
            quit()


simulator()