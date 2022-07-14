import os

DIR_PATH='./AddressBook/'
# DATA_LIST=[]

# -------------------------------------------------------
# 함수 정의
# -------------------------------------------------------
# (0) 메뉴 출력 함수
# 함 수 명 : printMenu()
# 파라미터 : 없음
# 리 턴 값 : 없음
def printMenu():
    print('='*7 + 'ADDRESSBOOK' + '='*7)
    print(' '*7 + '1. 전체보기' + ' '*7)
    print(' '*7 + '2. 검   색' + ' '*7)
    print(' '*7 + '3. 추   가' + ' '*7)
    print(' '*7 + '4. 제   거' + ' '*7)
    print(' '*7 + '5. 종   료' + ' '*7)
    print('=' * 26)

# -------------------------------------------------------
# (1) 전체보기 함수
# 함 수 명 : showAddress()
# 파라미터 : 없음
# 리 턴 값 : 없음
def showAddress():
    print('현재까지 입력된 모든 주소록 정보입니다.')
    for addr in os.listdir(DIR_PATH):     # for addr in ADDR_LIST 기존에 빈 리스트에 정보를 채워넣는 것을 파일화함.
        print(addr[:-4])       # .txt를 끊어내기 위함

# -------------------------------------------------------
# (2) 등록된 주소록 검색 후 정보 출력하는 함수
# 함 수 명 : searchAddress()
# 파라미터 : name or phone_number => str data
# 리 턴 값 : 없음
def searchAddress(name_phone):

    # 파일명 리스트 안에서 해당 검색어의 존재 여부를 체크함.
    for add in os.listdir(DIR_PATH):
        if name_phone in add:
            print(f'파일명 => {add}')
            with open(DIR_PATH + add, mode='r', encoding='utf-8') as f:
                print(f'정보 : {f.read()}') # 정보를 읽어오고 보여줌.

# -------------------------------------------------------
# (3) 입력하여 주소록 추가하는 함수
# 함 수 명 : addhAddress()
# 파라미터 : 이름, 전화번호, 지역, 이메일
# 리 턴 값 : 없음
def addAddress(name, phone, location, email):
    filename = name + '_' + phone + '.txt'

    # AddressBook 폴더에 파일 생성
    with open(DIR_PATH + filename, mode='r', encoding='utf-8') as f:
        f.write(name + ' ' + phone + ' ' + location + ' ' + email)

# https://velog.io/@suasue/Python-%EA%B0%80%EB%B3%80%EC%9D%B8%EC%9E%90args%EC%99%80-%ED%82%A4%EC%9B%8C%EB%93%9C-%EA%B0%80%EB%B3%80%EC%9D%B8%EC%9E%90kwargs
# 패킹, 언패킹
# -------------------------------------------------------

# 프로그램 초기화하는 함수

def initializationApp():

    # 개인 주소록 저장 할 공간
    if not os.path.exists(DIR_PATH): os.mkdir(DIR_PATH)
    # DIR_PATH가 존재하는지 bool타입으로 검사하고, 없다면 만든다.




# -------------------------------------------------------
# 기능 구현
print('='*7 + '프로그램을 시작합니다' + '='*7 + '\n')

initializationApp()

while True:
    printMenu()

    userInput = input('-'*14 + '>'*7 + ' ' + '메뉴를 선택하시오.')

    if userInput == '5':
        print('프로그램을 종료합니다.')
        break

    elif userInput == '1':
        # pass # 전체보기
        showAddress()

    elif userInput == '2':
        # pass # 검색
        serchInput = input('이름 또는 전화번호 검색 : ')
        searchAddress(serchInput)

    elif userInput == '3':
        # pass # 추가
        search  = input('이름, 전화번호, 지역, 이메일 : 예시 - ㅇㅇㅇ,010-0000-0000,대구,abc@naver.com').split(',')
        addAddress(search[0], search[1], search[2], search[3])

    elif userInput == '4':
        pass # 제거, 구현 못했음.

    else:
        print(f'1 ~ 5 사이의 숫자를 입력해 주십시오.')




