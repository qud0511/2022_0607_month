# 프로그램: address
# (1) AddressBook 폴더에 개인 파일 생성 -> 이름_전화번호.txt
# (2) 전체보기, 검색, 추가, 종료 기능 -> 메뉴 출력
# (3) 종료 입력 전까지 무한 반복
# 전역변수와 상수 선언
DIC_NAME = './AddressBook/'

# 임포트 사용
import os.path as path
import os

# 1. 프로그램 초기화 기능 함수
# AddressBook 폴더내의 파일리스트 정보 가져오기
# 2. 파일, 폴더 관련 모듈 활용
# 파일명 저장 리스트 존재 여부 선택(할지 말지)

# 메뉴 출력 함수
# 함수명: displayMenu
# 파라미터: 없음
# 리턴값: 없음
def displayMenu():
    print("="*7 +'ADDRESSBOOK' + '='*7)
    print('1. 전체보기')
    print('2. 검   색')
    print('3. 추   가')
    print('4. 종   료')
    print('='*25)


# 함수명: addressCreate
# 파라미터: 이름과 번호
# 반환값: 이름, 번호가 들어간 새 주소
def addressCreate(name, phone):
    return DIC_NAME + name + "_" + phone + ".txt"


# 함수명: bt1
# 기능: 이름 모두 보기
# 파라미터: 없음
# 반환값: 없음
def bt1():
    all_list = os.listdir('./AddressBook')
    if all_list == []:
        print("주소록이 비어있습니다, 3번을 이용해서 주소록을 추가할 수 있습니다.")
    else:
        print('-------주소록 목록-------')
        for i in all_list:
            print(i[:-4])


# 함수명: bt2
# 기능: 이름 또는 번호 서치해서 원하는 값 뜨게 하기
# 파라미터: 이름 또는 번호
# 반환값: 없음
def bt2(name_input):
    # 이름 또는 번호 조건을 탐색하고 있다면 파일을 엽니다.
    all_list = os.listdir(DIC_NAME)
    if all_list == []:
        print("주소록이 비어있습니다.")
    else:
        for i in all_list:
            if name_input in i:
                print(f"파일명: {i[:-4]}")
                with open(DIC_NAME+f'{i}', mode='r', encoding='utf-8') as chosenMember:
                    print(chosenMember.read())


# button 4->3->1->2 순으로 만들었습니다.

# 함수명: bt3
# 기능: 이름 전화번호 지역 이메일을 받아서 전화번호부에 추가
# 파라미터: name, phone, region, email
# 반환값: 없음
def bt3(name, phone, region, email):
    print(f'[{name}, {phone}, {region}, {email}] 가 주소록에 새로 저장됩니다.')
    # 이름과 전화번호가 들어간 txt파일을 생성합니다.
    with open(addressCreate(name, phone), mode='a', encoding='utf-8') as new_address:
        new_address.write(f"이름: {name} \n전화번호: {phone} \n지역: {region}\n이메일: {email}")


# 기능 구현( 입력할 때, 이름, 전화번호, 지역, 이메일 순서로 입력하면 됩니다.)
# AddressBook 폴더 없는 경우에 생성
if not path.exists(DIC_NAME):
    os.makedirs(DIC_NAME)

# 메뉴창을 띄웁니다.
displayMenu()

while True:
    button = int(input("메뉴 선택: "))
    if button == 1:
        bt1()
    elif button == 2:
        name_input = input("검색 단어(이름): ")
        bt2(name_input)
    elif button == 3:
        name, phone, region, email = input("이름, 전화번호, 지역, 이메일: ").split(", ")
        bt3(name, phone, region, email)
    elif button == 4:
        break
    else:
        print("잘못된 선택입니다.")

