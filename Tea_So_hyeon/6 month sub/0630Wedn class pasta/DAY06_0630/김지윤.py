# 클래스명: Pasta
# 속성: 소스, 면, 채소,물
# 기능: 재료 손질하기, 면 삶기, 재료볶기
import time as t
class Pasta:
    # 인스턴스 변수
    # def __init__(self):


    # 소스선택
    def SMenu(self):
        print('------------------')
        print('      토마토')
        print('       크림')
        print('       로제')
        print('       오일')
        print('------------------')
        s = input("소스를 선택해주세요: ")
        print(f'{s}가/이 선택되었습니다.')

    # 면 선택
    def nMenu(self):
        print('------------------')
        print('     얇은 면')
        print('     넓은 면')
        print('       펜네')
        print('      라자냐')
        print('------------------')
        n = input("면을 선택해주세요: ")
        print(f'{n}가/이 선택되었습니다.')


    #조리하기
    def cook(self):
        print(f'--- 면 삶는 중 ---')
        t.sleep(1)
        print(f'---재료 볶는 중---')
        t.sleep(1)
        print(f'---파스타가 완성되었습니다.---')


myPasta=Pasta()
myPasta.SMenu()
myPasta.nMenu()
myPasta.cook()




