# 기본 화면 제목 ------------------------------------------------------

msg = '''
=== 나의 주소록 ===
  1. 전 체 보 기
  2. 검      색
  3. 추      가
  4. 종      료
================='''

# 저장 및 모듈 관련 ----------------------------------------------------------

DIR_PATH='./AddressBook/'         # 파일 저장 폴더
# DATA_LIST=[]                    # 주소 파일명 저장 리스트 (제거)

import os
import os.path as path

dList = os.listdir(DIR_PATH)      # 해당 폴더에 있는 파일들을 리스트해서 받는 dList 선언

if not path.exists(DIR_PATH):     # AddressBook 폴더 존재 유무에 따른 생성
    os.mkdir(DIR_PATH)

# else:
#     for file in os.listdir(DIR_PATH):
#         os.remove(DIR_PATH+file)

# 기능별 함수 정의 ----------------------------------------------------

# 1. 전체보기
# 함수명 : allData
# 파라미터 : 없음
# 리턴값 : 없음

def allData():
    print('\n전체 보기')
    # # for addr in DATA_LIST:
    for addr in dList:      # 모듈을 활용하여 주소를 기록하던 리스트 제거
        print(addr[:-4])                   # .txt 는 제거

# ------------------------------------------------------------------

# 2. 검색 (검색하여 해당 데이터 출력)
# 함수명 : searchData
# 파라미터 : namePhone (name or phone)
# 리턴값 : 없음

def searchData(namePhone):
    for add in dList:
        if namePhone in add:
            print(f'파일명 : {add[:-4]}')                                     # .txt 제거

            with open(DIR_PATH+add, mode = 'r', encoding='utf-8') as f:      # add+'.txt' 부분에서 .txt 제거
                print(f'{f.read()}\n')

# ------------------------------------------------------------------

# 3. 추가 (파일 생성 및 주소록 추가 함수)
# 함수명 : addData
# 파라미터 : name, phone, loc, email
# 반환값 : 없음

def addData(name, phone, loc, email):
    filename = name+'_'+phone+'.txt'
    # DATA_LIST.append(filename[:-4])                                 # 모듈 사용으로 굳이 저장할 필요 없어짐

    with open(DIR_PATH + filename, mode='w', encoding='utf-8') as f:
        f.write(name+' '+phone+' '+loc+' '+email)

# ----------------------------------------------------------------------------------------------------------

# 4. 종료 : if구문으로 구현

#----------------------------------------------------------------------------------------------------------------------

# 5. 초기화 (AddressBook 폴더 안에 존재하는 파일 리스트 정보 제거하여 초기화)
# 함수명 : delFiles
# 파라미터 : DIR_PATH
# 반환값 : 없음

def removeFiles():
    if path.exists(DIR_PATH):
      for file in dList:
        os.remove(DIR_PATH+file)

#----------------------------------------------------------------------------------------------------------------------

# 기능 구현

removeFiles()                       # 적절한 위치인지 확인, 제대로 쓴건지 확인

while True:
    print(msg)
    number = int(input('메뉴 선택 : '))

    if number == 4:
        break

    elif number == 1:
        allData()

    elif number == 2:
        search = input("\n검색 단어 : ")
        searchData(search)

    elif number == 3:
        name, phone, loc, email = input('이름,전화번호,지역,이메일 : ex) 가나다,123-4567-8901,경주,asdf@naver.com ').split(',')
        addData(name, phone, loc, email)

    else:
        print('존재하지 않는 메뉴입니다. 다시 입력하세요.')

#----------------------------------------------------------------------------------------------------------------------