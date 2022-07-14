#---------------------------------------------------------
# PROGRAM : AddressBook_APP
# DESCRIPTION : File I/O 처리, str 데이터 처리, Function 실습
# (1) AddressBook 폴더에 개인 파일 생성 -> 이름_전화번호.txt
# (2) 보기, 검색, 추가, 종료 기능 => 메뉴 출력
# (3) 종료 입력 전까지 무한 반복
# (4) File & dir 관련 모듈 적용
#---------------------------------------------------------
# 전역 변수 및 상수 선언 -------------------------------------
import os.path

DIR_PATH='./AddressBook/'                     # 파일 저장 폴더
                                              # 주소 파일 저장 리스트 / '.txt' 이거 붙이면 show 함수에서 떼주는 작업해야함
                                              # ADDR_LIST가 필요 없어지게 만들기 => 없애기!

# 함수 정의 -----------------------------------------------
# 메뉴 출력 함수 ------------------------------------------
# 함 수 명 : printMenu
# 파라미터 : 없음
# 리 턴 값: 없음
# -------------------------------------------------------
def printMenu():
    print('=' * 7 +'ADDRESSBOOK' + '=' * 7)
    print(' ' * 7 + '1. 전체보기')
    print(' ' * 7 + '2. 검   색')
    print(' ' * 7 + '3. 추   가')
    print(' ' * 7 + '4. 종   료')
    print('=' * 26)

# 전체 전화번호 출력 기능 함수-------------------------------
# 함 수 명 : showAddress
# 파라미터 : 없음
# 리 턴 값 : 없음                              => 내가 직접 뿌리면 되니까
# -------------------------------------------------------
def showAddress():
    print('현재 등록된 주소록 입니다.')
    for addr in os.listdir(DIR_PATH):
        print(addr[:-4])

# 등록된 주소 검색 후 정보 출력 함수-------------------------
# 함 수 명 : searchAddress
# 파라미터 : name or phone_number => str data
# 리 턴 값 : 없음
# -------------------------------------------------------
def searchAddress(name_phone):
    #파일명 리스트 안에서 해당 검색어 존재 여부 체크
    for add in os.listdir(DIR_PATH):
        if name_phone in add:
            print(f'파일명 : {add}')
            with open(DIR_PATH+add, mode='r', encoding='utf-8') as f:
                print(f'정보:{f.read()}')

# 주소록 파일 생성 및 추가 함수-------------------------
# 함 수 명 : addAddress
# 파라미터 : 이름, 전화번호, 지역, 이메일 (밖에서 입력받을 상황이면) / 입력받을 기능조차 함수 안에 넣으면 필요 없음
# 리 턴 값 : 없음
# -------------------------------------------------------
def addAddress(name, phone, loc, email):
    filename = name+'_'+phone+'.txt'

    # AddressBook 폴더에 파일 생성
    with open(DIR_PATH+filename, mode='w', encoding='utf-8') as f:
        f.write(name + ' ' + phone + ' ' + loc + ' ' + email)

# 프로그램 초기화 함수-------------------------------------
# ADDR_LIST에 AddressBook 안에 존재하는 파일 리스트 정보가 추가
# 함 수 명 : initApp
# 파라미터 : 없음
# 리 턴 값 : 없음
# -------------------------------------------------------
def initApp():
    # 개인 주소록 저장 할 공간
    if not os.path.exists(DIR_PATH): os.mkdir(DIR_PATH)

# 기능 구현 -----------------------------------------------
print('---------프로그램 시작합니다!')
initApp()
while True:
    printMenu()

    # 사용자로부터 메뉴 선택 받기
    select = input("메뉴 선택: ")
    if select == '4' : break
    elif select == '1':
        showAddress()
    elif select == '2':                         # 구현 전이면 pass로 일단 넘기고 실행 ㄱㄱ
        search = input("이름 또는 전화번호 검색 : ")
        searchAddress(search)
    elif select == '3':
        search = input("이름, 전화번호, 지역, 이메일 : (예: 이동혁, xxx-xxxx-xxxx, 서울, fullsun@daum.net)").split(',')  # input(str으로 들어와서).split(',') 가능
        addAddress(search[0],search[1],search[2],search[3])
    else:
        print('해당 메뉴는 존재하지 않습니다.')

print('---------프로그램 종료합니다.')


# UNPACK ------------------------------------------------------ (혜진 참고용) - 가독성 높아짐, 굳이 인덱스 안해도 됨
# name, phone, loc, email = input("이름, 전화번호, 지역, 메일 : ").split(',')
# print(name, phone, loc, email)