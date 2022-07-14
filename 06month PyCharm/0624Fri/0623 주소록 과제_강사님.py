# -----------------------------------------------------
# PROGRAM : AddressBook_APP
# DESCRIPTION : File I/D 처리, str 데이터 처리, Function 실습
# (1) AddressBook 폴더에 개인 파일 생성 -> 이름_전화번호.txt
# (2) 보기, 검색, 추가, 종료 기능 => 메뉴 출력
# (3) 종료 입력 전까지 무한 반복
# -----------------------------------------------------

# 전역 변수 및 상수 선언 ---------------------------------
DIR_PATH= './AdressBook/'          # 파일저장 폴더
ADDR_LIST=['가_222', '가나다_111']                        # 주소 파일 저장 리스트
# -----------------------------------------------------


# 함수 정의 --------------------------------------------

# ()메뉴 출력 함수 --------------------------------------
# 함 수 명 : printMenu
# 파라미터 : 없음
# 리 턴 값 : 없음
def printMenu():
    print('='*6 + 'ADDRESSBOOK' + '='*6)
    print(' '*6 + '1. 전체보기')
    print(' '*6 + '2. 검   색')
    print(' '*6 + '3. 추   가')
    print(' '*6 + '4. 종   료')
    print('='*23)

# (1)전체 전화번호 리스트 출력 함수 --------------------------
# 함 수 명 : showAddress
# 파라미터 : 없음
# 리 턴 값 : 없음
def showAddress():
    print('현재 등록된 주소록 정보')
    for addr in ADDR_LIST:
        print(addr)

# (2) 등록된 주소 검색 후 정보 출력 함수 -------------------
# 함 수 명 : searchAddress
# 파라미터 : name or phone_number str data
# 리 턴 값 : 없음
def searchAddress(name_phone):

    # 파일명 리스트 안에서 해당 검색어 존재 여부 체크
    for add in ADDR_LIST:
        if name_phone in add:
            print(f'파일명 : {add}')
            with open(DIR_PATH + add + '.txt', mode='r', encoding='utf=8') as f:
                print(f'정  보 : {f.read()}')


# (3) 주소록 파일 생성 및 추가 함수 -------------------
# 함 수 명 : addAddress
# 파라미터 : 이름, 전화번호, 지역, 이메일
# 반 환 값 : 없음

def addAddress(name, phone, location, email):
    filename = name+' '+phone+'.txt'

    # 파일명 리스트 추가
    ADDR_LIST.append(filename[:-4])            # 끝에 .txt 빼고 추가하기 위해서 [:-4]

    # AddressBook 폴더에 파일 생성
    with open(DIR_PATH+filename, mode='w', encoding='utf-8') as f:
        f.write(name + ' ' + phone + ' ' + location + ' ' + email)


# ()프로그램 초기화 함수 ------------------------------------
# ADDR_LIST에 AddressBook 안에 존재하는 파일 리스트 정보가 추가
# 함 수 명 : initApp
# 파라미터 :
# 리 턴 값 :
# def initApp():



# ----------------------------------------------------

# 기능 구현 --------------------------------------------
print('-'*10 + '프로그램 시작합니다.')

while True:
    printMenu()

    # 사용자로부터 메뉴 선택받기
    select = input('메뉴 선택 : ')
    if select == '4':
        break

    #
    elif select == '1':
        showAddress()

    elif select == '2':
        search=input('이름 또는 전화번호 검색 :')
        searchAddress()

    elif select == '3':
        search = input('이름, 전화번호, 지역, 이메일 : (예: 홍길동,010-0000-0000,대구,abc@naver.com)').split(',')
        addAddress(search[0], search[1], search[2], search[3])

    else:
        print('해당 메뉴가 존재하지 않습니다.')

print('-'*10 + '프로그램 종료합니다.')






