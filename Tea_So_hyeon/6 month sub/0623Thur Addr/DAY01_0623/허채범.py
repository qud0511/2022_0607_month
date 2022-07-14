# 기본 화면 제목 ------------------------------------------------------

msg = '''
=== 나의 주소록 ===
  1. 전 체 보 기
  2. 검      색
  3. 추      가
  4. 종      료
================='''

# 저장 관련 ----------------------------------------------------------

DIR_PATH='./AddressBook/'       # 파일 저장 폴더
DATA_LIST=[]                    # 주소 파일 저장 리스트

# 기능별 함수 정의 ----------------------------------------------------

# 1. 전체보기
# 함수명 : allData
# 파라미터 : 없음
# 리턴값 : 없음

def allData():
    print('\n전체 보기')
    for addr in DATA_LIST:
        print(addr)

# ------------------------------------------------------------------

# 2. 검색 (검색하여 해당 데이터 출력)
# 함수명 : searchData
# 파라미터 : namePhone (name or phone)
# 리턴값 : 없음

def searchData(namePhone):
    for add in DATA_LIST:
        if namePhone in add:
            print(f'파일명 : {add}')

            with open(DIR_PATH+add+'.txt', mode = 'r', encoding='utf-8') as f:
                print(f'{f.read()}\n')

# ------------------------------------------------------------------

# 3. 추가 (파일 생성 및 주소록 추가 함수)
# 함수명 : addData
# 파라미터 : name, phone, loc, email
# 반환값 : 없음

def addData(name, phone, loc, email):
    filename = name+'_'+phone+'.txt'
    DATA_LIST.append(filename[:-4])

    with open(DIR_PATH + filename, mode='w', encoding='utf-8') as f:
        f.write(name+' '+phone+' '+loc+' '+email)

# ----------------------------------------------------------------------------------------------------------

# 4. 종료 : if구문으로 구현

#----------------------------------------------------------------------------------------------------------------------

while True:
    print(msg)
    number = int(input('메뉴 선택 : '))

    if number == 4: break

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