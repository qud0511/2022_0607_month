# 파스타 요리 프로그램
# 파라미터 : 메뉴, 면, 소스, 채소, 추가 재료
# 기   능 : 물 끓이기, 면 삶기, 재료 손질하기, 볶기, 먹기

class Pasta:
    # 인스턴스 생성자
    def __init__(self, menu, pasta_type, sauce, *add):  # 가변인자를 두개를 받을 수는 없는듯
        self.menu=menu
        self.pasta_type=pasta_type
        self.sauce=sauce
        self.add=add

    # Getter
    def getMenu(self): return self.menu
    def getIngridient(self): return self.pasta_type, self.sauce, self.add
    def getPasta_type(self): return self.pasta_type
    def getSauce(self): return self.sauce
    def getAdd(self): return self.add

    # Setter
    def setMenu(self, menu): self.menu=menu
    def setPasta_type(self, pasta_type): self.pasta_type=pasta_type
    def setSauce(self, sauce): self.sauce=sauce
    def setAdd(self, add): self.add=add

    # 재료 추가
    def addMore(self, addmore):
            ing=list(self.add)
            for i in addmore:
                ing+=i                          # add가 어떻게 찍히는지 확인 -> tuple
            self.add=tuple(ing)

# 메뉴
def selectStep():
    print('===PASTA===')
    print('1. 재료 준비')
    print('2. 요리 시작')
    print('3. 재료 추가')
    print('4. 종    료')



####################################################################

BasilPasta=Pasta('BasilPasta_1', '펜네', '바질페스토', '양파', '돼지고기')

while True:
    selectStep()
    select=input('메뉴를 선택해주세요. : ')
    if select=='4':
        print('<종료합니다.>')
        break
    elif select=='1':
        print(f'필요한 재료는 {BasilPasta.getIngridient()}입니다.')
        try:
            ready = input('준비가 다 되었다면 \'Enter\'를 눌러주세요.')
            print('')
        except Exception:pass
    elif select=='2':
        step1 = input('재료를 모두 손질한 후 \'Enter\'를 눌러주세요.')
        step2 = input('물을 끓인 후 면을 넣고 \'Enter\'를 눌러주세요.')
        step3 = BasilPasta.getAdd()
        for i in step3:
            ing = input(f'{i}를 손질한 후 \'Enter\'를 눌러주세요.')
        step4 = input(f'모든 재료와 {BasilPasta.getSauce()} 소스를 넣고 볶아준 후 \'Enter\'를 눌러주세요.')
        step5 = input('플레이팅한 후 \'Enter\'를 눌러주세요.')
        print('< 맛있게 드세요!>\n')
    elif select=='3':
        more = []
        while True:
            user = input('추가할 재료를 입력하거나 0를 눌러 입력한 재료를 레시피에 추가하세요. : ')
            if user == '0':
                break
            else:
                more = more+[user]
        BasilPasta.addMore(more)




