#스파게티 요리사 프로그램
#----------------------------------------------
#클래스명 : spageti
#변   수 : 면, 소스, 채소, 기타재료
#속   성 : 재료손질, 면삶기, 볶기, 플레이팅, 먹기
#----------------------------------------------
class spageti:
    #생성자
    def __init__(self,myoen,source,materials,plating_mater):
        self.myoen=myoen
        self.source = source
        self.materials = materials
        self.plating_mater = plating_mater

    def cut(self):
        material_data = {'버섯': '2 개',
                         '양파': '반 개',
                         '마늘': '1 개',
                         '소고기': '300g',
                         '돼지고기': '400g'}
        materials_li=self.materials.split(',')
        for material in materials_li:
            for ma_da in material_data:
                if material==ma_da:
                    print(f"{material}재료 {material_data[ma_da]}을(를) 먹기 좋게 손질합니다.")

    def boil(self):
        print(f"""우선 1인분 기준 물을 550ml을 부어줍니다.
그 다음 물을 끓기 시작하면 {self.myoen}면을 넣고 삶아줍니다.""")

    def fry(self,oil):
        print(f"""{oil}오일에 손질한 재료를 넣고 볶아주세요.
재료가 어느 정도 읽으면 {self.source}와 함께 볶아주세요.
마지막으로 삶아 놓았던 {self.myoen}면과 함께 약한불에 볶아주세요.""")

    def plating(self):
        plat_mat_li = self.plating_mater.split(',')
        print("완성된 스파게티 위에 ",end='')
        for pl_ma in plat_mat_li:
            print(f'{pl_ma}|',end='')
        print(" 등을 스파게티 위에 이쁘게 장식을 해 주세요.")
        print(f"{self.source} 스파게티가 완성되었습니다.")
        print("맛있게 먹어보아요!!!!!")

def cook():
    my_spa=spageti(input('면 선택 : '),
                   input('소스 선택 : '),
                   input('''재료에는 버섯,양파,마늘,소고기,돼지고기가 있습니다.
예시)버섯,양파 로 콤마(,)을 이용하여 재료를 구분하여 주세요.(입력 순서는 상관없습니다.)
재료 선택 : ''')
                   ,input('장식 재료 선택 : '))
    my_spa.cut()
    my_spa.boil()
    my_spa.fry(input('오일 선택 : '))
    my_spa.plating()

cook()












