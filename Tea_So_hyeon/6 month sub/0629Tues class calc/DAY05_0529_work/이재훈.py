# ---------------------------------------------------------------------------
# 계산기 클래스
# 클래스명
# 속성/특징 => 필드(Field) >>  색상, 제조사
# 역할/기능 == > 함수/메서드(mtehod)
# >> 계산시 인스턴스 계산 메서드 ==> __init__()
# >> 계산기 속성/특징 값 읽기 => getter method
# >> 계산기 속성/특징 값 변경 => setter method
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# 계산기 프로그램
# 필수 조건 : 계산기 클래스
# ---------------------------------------------------------------------------
class Calculator:
    # 인스턴스 생성자
    def __init__(self, maker, color, *data):
        self.maker=maker
        self.color=color
        self.data=data

    # getter/setter 메서드 (선택)
    def getData(self): return self.data
    def setData(self, *data): self.data=data

    # 내가 원하는 계산기 기능

    # ----------------------------------------------
    # 메소드명 : calcSum
    # 파라미터 : *data
    # 리턴값  : none
    # ----------------------------------------------
    def calcSum(self, express):
        list_data = list(express)                       # express 값을 리스트 값으로 변환
        total = 0                                       # 계산 결과 값
        num = ''                                        # 중간 숫자값
        for i in range(0, len(list_data)):              # data값으로 된 리스트를 모두 살펴보았을 때
            if list_data[i].isdigit() == True:          # 만약 i번째 요소가 숫자라면
                num = num + list_data[i]                # num 텍스트에 요소값을 기록해둠
            elif list_data[i] == '+':                   # 만약 + 기호가 왔을 때
                if list_data[i - 1] != list_data[i]:    # 앞에도 + 기호가 중복되지 않아야지
                    total += int(num)                   # num 값을 total에 더하고
                    num = ''                            # num 초기화
            elif list_data[i] == '=':                   # 만약 = 기호가 왔을 때
                if list_data[i - 1].isdigit() == True:  # = 기호 앞에 숫자값이 있다면
                    total += int(num)                   # num값을 더해준다
            else : i = i + 1                            # 그 외의 문자는 무시
        print(f'계산 결과 : {total}')                    # 계산값 보여줌

    def calcMinus(self, express):
        list_data = list(express)                          # data 값을 리스트 값으로 변환
        total = 0                                       # 계산 결과 값
        num = ''                                        # 중간 숫자값
        for i in range(0, len(list_data)):              # data값으로 된 리스트를 모두 살펴보았을 때
            if list_data[i].isdigit() == True:          # 만약 i번째 요소가 숫자라면
                num = num + list_data[i]                # num 텍스트에 요소값을 기록해둠
            elif list_data[i] == '-':                   # 만약 - 기호가 왔을 때
                if list_data[i - 1] != list_data[i]:    # 앞에도 - 기호가 중복되지 않은 상태에서
                    if list_data[0] != '-' and total == 0:              #
                        total += int(num)                   # num 값을 total에 더하고
                        num = ''                            # num 초기화
                    else :
                        total -= int(num)                   # num 값을 total에 빼고
                        num = ''                            # num 초기화
            elif list_data[i] == '=':                   # 만약 = 기호가 왔을 때
                if list_data[i - 1].isdigit() == True:  # = 기호 앞에 숫자값이 있다면
                    total -= int(num)                   # num값을 빼준다
            else : i = i + 1                            # 그 외의 문자는 무시
        print(f'계산 결과 : {total}')                    # 계산값 보여줌


    # 인데 문제는 맨 앞에 문자가 오면 오류가 뜬다
    # =로 안끝나도 계산값이 나올방법은 없나?


    # 사용자와 인터페이스
    def showUI(self):
        print("***** 계산기 ******")
        print("*    1. 덧셈     *")
        print("*    2. 뺄셈     *")
        # print("*    3. 곱셈     *")
        # print("*   4. 나눗셈     *")
        print("***** 5. 종료 *****")

calc01 = Calculator('sharp', 'black')

while True:
    calc01.showUI()
    select = input("메뉴 선택 : ")
    if select == '5':break
    elif select == '1':
        calc01.calcSum(express = input())
    elif select == '2':
        calc01.calcMinus(express = input())
    # elif select == '3' : calc01.calcMulti()
    # elif select == '4' : calc01.calcDivid()