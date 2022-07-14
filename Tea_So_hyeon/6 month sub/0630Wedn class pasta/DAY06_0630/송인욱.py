# 파스타 만드는 프로그램
# ---------------------------------------------------------------------
# class : PastaMaker
# instance : 면종류, 재료, 소스
# method : 면 고르기, 면 소분, 재료 손질, 소스 넣기
class PastaMaker():

    def __init__(self, noodle='', ingredient='', sauce='오일'):
        self.noodle = noodle
        self.ingredient = ingredient
        self.sauce = sauce
        self.pastaName = ''
        self.subIngre = ''


    # set method -------------------------------------
    def setNoodle(self, noodle):
        self.noodle = noodle
    def setIngredient(self, ingredient):
        self.ingredient = ingredient
    def setSauce(self, sauce):
        self.sauce = sauce


    # ------------------------------------------------
    # 함수명 : boilNoodle
    # 기능 : 면 이름 파스타 이름에 넣기
    # 파라미터 : none
    # 결과값 : none
    def boilNoodle(self):
        self.pastaName = self.pastaName + self.noodle


    # -------------------------------------------------
    # 함수명 : prepareIngre
    # 기능 : 재료 받은거 정리해서 메인은 이름에 넣고 서브는 서브재료에 넣기
    # 파라미터 : none
    # 결과값 : none
    def prepareIngre(self):
        ingrelist = self.ingredient.split(',')
        ingreList = [n.strip() for n in ingrelist]
        main = ingreList[0]
        sub = ingreList[1:]
        self.pastaName = self.pastaName + main
        self.subIngre = ','.join(sub)


    # -------------------------------------------------
    # 함수명 : sauceInput
    # 기능 : 소스 입력 받아서 이름에 넣기
    # 파라미터 : none
    # 결과값 : none
    def sauceInput(self):
        self.pastaName = self.pastaName + self.sauce


    # --------------------------------------------------
    # 함수명 : finishPasta
    # 기능 : 파스타 완성 메세지 보내기
    # 파라미터 : none
    # 결과값 : none
    def finishPasta(self):
        print(self.pastaName + '파스타가 완성되었습니다!!')
        print(self.subIngre + '를 곁들인')


    # showui method ------------------------------------
    def showUi(self):
        print('*** 무슨무슨파스타 ***')
        print('* 1. 면 고르기')
        print('* 2. 재료 고르기')
        print('* 3. 소스 고르기')
        print('* 4. 완 성 ~~~')


# ------------------------------------------------------------------------------
# 함수명 : open
# 기능 : 프로그램 실행
# 파라미터 : none
# 결과값 : none
def open():

    p1 = PastaMaker()

    while True:
        p1.showUi()
        SELC = input('순서대로 주문해주세요: ')

        if SELC == '1':
            print('ex)스파게티, 링귀네, 라비올리, 펜네 ...')
            msg1 = input('면 종류를 골라주세요: ')
            p1.setNoodle(msg1)
            p1.boilNoodle()
            print('\n')

        elif SELC == '2':
            print('주재료, 부재료 ...')
            msg2 = input('재료를 선택해주세요: ')
            p1.setIngredient(msg2)
            p1.prepareIngre()
            print('\n')

        elif SELC == '3':
            print('기본소스는 오일입니다.')
            msg3 = input('소스를 선택해 주세요: ')
            p1.setSauce(msg3)
            p1.sauceInput()
            print('\n')

        else:
            p1.finishPasta()
            break


# ---------------------------------------------------------------

open()
