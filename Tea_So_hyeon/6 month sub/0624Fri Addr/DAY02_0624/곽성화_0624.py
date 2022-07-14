# -----------------------------------------------
# PROGRAM : AddressBook_APP
# DESCRIPTION : File I/O 처리, str 데이터 처리, Function 실습
# (1) AddressBook 폴더에 개인 파일 생성 -> 이름_전화번호.txt
# (2) 보기, 검색, 추가, 종료 기능 => 메뉴 출력
# (3) 종료 입력 전까지 무한 반복
# Update
# (4) AddressBook 폴더 내의 파일리스트 정보 가져오기 ( 프로그램 초기화 기능 함수 - 선택사용)
# (5) 파일&폴도 관련 모듈 활용하여 파일명 저장 리스트 존재 여부 선택
# -----------------------------------------------

# 모듈 사용
import os.path as path
import os

# 전역변수 및 상수 ---------------------------------
DIR_PATH= './AddressBook'		  # 파일 저장 폴더
# ADDR_LIST=[]                                 # 주소 파일 저장 리스트

# 함수 정의 ---------------------------------------
# 메뉴 출력 함수 -----------------------------------
# 함 수 명 : printMenu
# 파라미터 : 없음
# 리 턴 값 : 없음
# -----------------------------------------------
def printMenu():
    print('=' * 7 + ' ADDRESSBOOK ' + '=' * 7)
    print(' ' * 7 + '1. 전체보기')
    print(' ' * 7 + '2. 검   색')
    print(' ' * 7 + '3. 추   가')
    print(' ' * 7 + '4. 종   료')
    print('=' * 25)

# 전체 전화번호 리스트 출력 함수 -----------------------------------
# 함 수 명 : showAddress
# 파라미터 : 없음
# 리 턴 값 : 없음    (데이터를 던져주는게 아니라 출력하고 끝!이므로 리턴값 없음)
# -----------------------------------------------
def showAddress():
    print('현재 등록된 주소록 정보')
    for addr in os.listdir(DIR_PATH):
        print(addr[:-4])        # .txt 제외

# 등록된 주소 검색 후 정보 출력 함수 -------------------------
# 함 수 명 : searchAddress
# 파라미터 : name or phone_number str data
# 리 턴 값 : 없음    (함수에서 검색하여 출력하므로)
# -----------------------------------------------
def searchAddress(name_phone):
    # 파일명 리스트 안에서 해당 검색어 존재 여부 체크
    for add in os.listdir(DIR_PATH):
        if name_phone in add:
            print(f'파일명 : {add}')
            with open(DIR_PATH+add+'.txt', mode='r', encoding='utf-8') as f:
                print(f'정  보 : {f.read()}')

# 주소록 파일 생성 및 추가 함수 -------------------------
# 함 수 명 : addAddress
# 파라미터 : 이름, 전화번호, 지역, 이메일
# 리 턴 값 : 없음        (파일 만들고 별도로 받을 데이터는 없으므로)
# -----------------------------------------------
def addAddress(name, phone, loc, email):
    filename=name+'_'+phone+'.txt'
    # # 파일명 리스트 추가
    # ADDR_LIST.append(filename[:-4])
    # AddressBook 폴더에 파일 생성
    with open(DIR_PATH+filename, mode='w', encoding='utf-8') as f:
        f.write(name + ' ' + phone + ' ' + loc + ' ' + email)

# 프로그램 초기화 기능 함수 ---------------------------------
# ADDR_LIST에 AddressBook 안에 존재하는 파일 리스트 정보가 추가
# 함 수 명 : initApp
# 파라미터 : 없음
# 리 턴 값 : 없음
# -----------------------------------------------
def initApp():
    # 개인주소록 저장할 공간
    # 파일 존재 여부 먼저 확인하고, 없으면 생성
    if not os.path.exists(DIR_PATH):
        os.mkdir(DIR_PATH)


# 기능 구현 ---------------------------------------

# printMenu()       # 함수가 잘 만들어졌는지 확인!

print('-----프로그램을 시작합니다.!!')
initApp()
while True:
    printMenu()

    # 사용자로부터 메뉴 선택 받기
    select = input("메뉴 선택 : ")
    if select == '4': break
    elif select == '1':
        showAddress()
    elif select == '2':
        search=input("이름 또는 전화번호 검색 : ")
        searchAddress(search)
    elif select == '3':
        name, phone, loc, email=input("이름, 전화번호, 지역, 이메일 : (예:홍길동,000-1111-2222,대구,self@naver.com)\n").split(',')
        addAddress(name, phone, loc, email)

        # search=input("이름, 전화번호, 지역, 이메일 : (예:홍길동,000-1111-2222,대구,self@naver.com").split(',')
        # addAddress(search[0], search[1], search[2], search[3])
    else:
        print('해당 메뉴는 존재 하지 않습니다.')

print('-----프로그램을 종료합니다.^^')

