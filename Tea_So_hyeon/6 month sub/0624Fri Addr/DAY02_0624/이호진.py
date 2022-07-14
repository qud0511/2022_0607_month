DIR_PATH='./AddressBook/'  # 파일 저장 폴더
import os

fileList = os.listdir(DIR_PATH)

def printMenu():
    print('='*7+'ADDRESSBOOK'+'=' * 7)
    print(' '*7 +'1. 전체보기')
    print(' '*7 +'2. 검   색')
    print(' '*7 +'3. 추   가')
    print(' '*7 +'4. 종   료')
    print('=' * 26)

def showAddress():
    print('현재 등록된 주소록 정보')
    for addr in os.mkdir(DIR_PATH):
        print(addr[:-4])

def showAddress():                  # 전체 출력
    print('등록된 주소를 전부 표시합니다.')
    for file in fileList:
        print(file[:-4])

def searchAddress(name_phone):
    # 파일명 리스트 안에서 해당 검색어 존재 여부 체크
    for add in os.listdir(DIR_PATH):
        if name_phone in add:
            print(f'파일명 : {add}')
            with open(DIR_PATH+add, mode='r', encoding='utf-8') as f:
                print(f'정  보 : {f.read()}')

def addAddress(name, phone, loc, email):
    filename=name+'_'+phone[3:7]+'.txt'

    #ADDR_LIST.append(filename[:-4])

    with open(DIR_PATH+filename, mode='w', encoding='utf-8') as f:
        f.write(name + ' ' + phone + ' ' + loc + ' ' + email )

def initApp():
    if not os.path.exists(DIR_PATH):
        os.mkdir(DIR_PATH)

print('----- 프로그램 시작합니다.!!')
initApp()
while True:
    printMenu()

    select = input("메뉴 선택 : ")
    if select == '4': break
    elif select == '1':
        showAddress()
    elif select == '2':
        search=input("이름 또는 전화번호 검색: ")
        searchAddress(search)
    elif select == '3':
        search=input("이름, 전화번호, 지역, 이메일 : (예:000,xxx-xxxx-xxxx, 대구, a@0000.000").split(',')
        addAddress(search[0], search[1], search[2], search[3])
    else:
        print('해당 메뉴는 존재하지 않습니다.')

print('----- 프로그램 종료합니다. -----')