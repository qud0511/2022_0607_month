# 함수 구현
#=========================================================================
# 메뉴 출력 함수
# 함수명 : printMenu
# 파라미터 : 없음
# 반환값 : 없음
def printMenu():
    print('='*4+'나의 주소록'+'='*4)
    print(' '*4+'1. 전체보기')
    print(' '*4+'2. 검   색')
    print(' '*4+'3. 추   가')
    print(' '*4+'4. 종   료')
    print('='*17)
#=========================================================================
# 전체 전화번호 리스트 출력 함수
# 함수명 : allAddr
# 파라미터 : 없음
# 반환값 : 없음
def allAddr():
    datalist = os.listdir('./AddressBook')
    for i in datalist:
        print(i[:-4])
#=========================================================================
# 주소록 파일 생성 및 추가 함수
# 함수명 : addAddr
# 파라미터 : name, phone_number, state, e-mail
# 반환값 : 없음
def addAddr(name, pn, state, email):
    filename=name+'_'+pn+'.txt'
    # AddressBook 폴더에 파일 생성
    with open(DIR_PATH+filename, mode='w', encoding='utf-8') as f:
        f.write(name+' '+pn+' '+state+' '+email)
#=========================================================================
# 프로그램 초기화 함수
# ADDR_LIST에 AddressBook 안에 존재하는 파일 리스트 정보가 추가
# 함수명 : initApp
# 파라미터 : 없음
# 반환값 : 없음
def initApp():
    # AddressBook 폴더 존재 여부 체크
    DIR_PATH='./AddressBook'
    if not path.exists(DIR_PATH):
        os.makedirs(DIR_PATH)
        # txt 파일 존재 여부 체크
        DIR_PATH2 = './AddressBook/.txt'
        if not path.exists(DIR_PATH2):
            name, pn, state, email = input(f'이름,전화번호,지역,이메일 순으로 입력하세요.').split(',')
            addAddr(name, pn, state, email)

#=========================================================================
# 등록된 주소 검색 후 정보 출력 함수
# 함수명 : searchAddr
# 파라미터 : name or phone_number str data
# 반환값 : 없음
def searchAddr(word):
    # 파일명 리스트 안에서 해당 검색어 존재 여부 체크
    datalist = os.listdir('./AddressBook')
    for addr in datalist:
       if word in addr:
           print(f'파일명 : {addr[:-4]}')
           with open(DIR_PATH+addr, mode='r', encoding='utf-8') as f:
               info=f.readlines()
               print(f'정보 : {info[0]}')
#=========================================================================

# 기능 구현
print('프로그램 시작')

DIR_PATH='./AddressBook/'
import os.path as path
import os

# AddressBook 폴더 및 txt 파일 존재 여부 확인
initApp()

while True:
    printMenu()
    # 사용자로부터 메뉴 선택 받기
    select = input('메뉴 선택 : ')

    if select=='4': break
    elif select=='1':
        allAddr()
    elif select=='2':
        searchAddr(input(f'검색 단어 : '))
    elif select == '3':
        name, pn, state, email = input(f'이름,전화번호,지역,이메일 순으로 입력하세요.').split(',')
        addAddr(name, pn, state, email)
    else:
        print("!!! 잘못 입력했습니다. 다시 입력하세요. !!!")