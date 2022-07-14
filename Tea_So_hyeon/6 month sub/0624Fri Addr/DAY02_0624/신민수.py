# < 1.전역 변수 및 상수 선언 >
DIR_PATH='./AddAddressBook/'                                    # 파일 저장 폴더
import os
import os.path as path

# [ 메뉴 출력 함수 ]
def printMenu():
    print("=" * 7 + "ADDRESSBOOK" + "=" * 7)
    print(' ' * 7 +'1. 전체보기')
    print(' ' * 7 +'2. 검   색')
    print(' ' * 7 +'3. 추   가')
    print(' ' * 7 +'4. 종   료')
    print('=' * 26)

# [ 전체 전화번호 리스트 출력 함수 ]
def showAddress():
    print('현재 등록된 주소록 정보')
    datalist = os.listdir(DIR_PATH)
    for i in datalist:
        i=i[:-4]
        print(i)

# [ 등록된 주소 검색 후 정보 출력 함수 ]
def searchAddress(name_phone):
    for add in os.listdir(DIR_PATH):
        if name_phone in add:
            print(f'파일명 : {add[:-4]}')
            with open(DIR_PATH+add,'r',encoding='utf8') as f: # DIR_PATH:저장할 위치 선정, add:open할 파일 선정
                print(f'정  보 : {f.read()}')                  # read() 괄호를 달아줘야 정상 동작

# [ 주소록 파일 생성 및 추가 ]
def addAddress(name, phone, loc, email):
    filename=name+'_'+phone[4:8]+'.txt'                       # 저장될 파일명 선정
    if filename is not os.listdir(DIR_PATH):                  # 동일한 파일 존재 여부 파악하기
        with open(DIR_PATH+filename, 'w',encoding='utf8') as f:
            f.write(name + ' ' + phone + ' ' + loc + ' ' +email )

# [ 프로그램 초기화 함수 ]
def initApp():
    if not path.exists(DIR_PATH):                             # 폴더 없으면 생성
        os.makedirs(DIR_PATH)

# < 3.기능 구현 >---------------------------------------------------------------------------------------------------

initApp()
print('프로그램 시작합니다!')
while True:
    printMenu()
    #사용자로부터 메뉴 선택 받기
    select = input("메뉴 선택 : ")
    if select=='4' :break
    elif select=='1':
         showAddress()

    elif select=='2':
        search=input("이름 또는 전화번호 검색 : ")
        searchAddress(search)
        pass

    elif select=='3':
        # search=input("이름, 전화번호, 지역, 이메일 : (예:홀길동,xxx-xxxx-xxxx,대구,a@OOO.OOO").split(',')
        # addAddress(search[0],search[1],search[2],search[3])
        name, phone, loc, email = input('이름, 전화번호, 지역, 이메일:').split(',')
        addAddress(name, phone,loc, email)
    else :
        print(" 해당 메뉴는 존재하지 않습니다.")

print('프로그램 종료합니다!')