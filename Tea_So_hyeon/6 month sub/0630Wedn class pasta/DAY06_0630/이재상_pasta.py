#=====================================================
# 파스타 주문에 따른 레시피 출력 프로그램
# 클래스명 : Pasta
# 변수 : 면, 소스, 부재료
# 함수 : 레시피 함수
#=====================================================

# 클래스 생성

class Pasta():

    # 인스턴스 생성자
    def __init__(self,noodle,source,ingred):
        self.noodle=noodle
        self.source=source
        self.ingred=ingred

    # 레시피 함수
    def recipe(self):
        print(f'{self.noodle}을 삶으시오. '
              f'\n{self.ingred}(을)를 손질하시오. '
              f'\n{self.noodle}, {self.source}, {self.ingred}(을)를 볶으시오.')

    # 사용자 인터페이스 (CUI) 기능 메서드
    def typePasta():
        print('*****  메  뉴  판  *****')
        print('     1. 봉골레 파스타   ')
        print('     2. 까르보나라      ')
        print('     3. 토마토 파스타   ')
        print('     4. 로제 파스타     ')
        print('     5. 종  료         ')
        print('***********************')

pasta1=Pasta('일반면', '올리브유', '마늘, 양파, 바지락')
pasta2=Pasta('일반면','크림 소스','후추')
pasta3=Pasta('두꺼운면', '토마토 소스', '마늘,양파,버섯,다진고기')
pasta4=Pasta('두꺼운면', '로제 소스', '마늘,양파,버섯,새우')

# 기능 구현

p=Pasta.typePasta()
select=input('메뉴 선택 : ')
if select == '1':
    pasta1.recipe()
elif select == '2':
    pasta2.recipe()
elif select == '3':
    pasta3.recipe()
elif select == '4':
    pasta4.recipe()
