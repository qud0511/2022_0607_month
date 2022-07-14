# PROGRAM : AddressBookAPP
# DESCRIPTION : File I/O 처리, str 데이터 처리, Function 실습
# (1) AddressBook 폴더에 개인 파일 생성 -> 이름_전화번호.txt
# (2) 보기, 검색, 추가, 종료 기능 => 메뉴 출력
# (3) 종료 입력 전까지 무한 반복
# (4) File & dir 관련 모듈 적용

# -------------------------------------------------------------------

# 전역 변수 및 상수 선언
ADD_PATH='./AddressBook/'

import os

# -------------------------------------------------------------------

# 함수 선언

# 3.추가
# 기    능 : 주소록 추가
# 함 수 명 : addInfo
# 파라미터 : name, phNum, address
# 리 턴 값 : 없음
def addInfo(name, phNum, address):
    fileName=f'{name}_{phNum}.txt'
    file=open(ADD_PATH+fileName, mode='a', encoding='utf-8')
    file.write(f'''이름 : {name}\n전화번호 : {phNum}\n지역 : {address}\n\n''')
    file.close()

# 1.전체보기
# 기    능 : 주소록 전체보기
# 함 수 명 : adrGetAll
# 파라미터 : 없읍
# 리 턴 값 : 전체 주소록 목록
def adrGetAll():
    adr_lst=os.listdir(ADD_PATH)
    for adr in adr_lst:
        print(adr[:-4])

# 2.검색
# 기    능 : 입력받은 정보의 주소록 검색하기
# 함 수 명 : srcInfo
# 파라미터 : src (문자열)
# 리 턴 값 : 파일명, 주소록 정보
def srcInfo(src):
    adr_lst = os.listdir(ADD_PATH)
    for add in adr_lst:
        if src in add:
            print(f'파일명 : {add[:-4]}')
            data=open(ADD_PATH+add, mode='r', encoding='utf-8')
            print(data.read())
        if not src in add:
            print('< 주소록에 없습니다. >')


##############################################################
# ----------------------------------------------------------

menu = '''=== 나의 주소록 ===
1. 전체보기
2. 검   색
3. 추   가
4. 종   료
===============
'''

# 주소록 저장 공간 존재 확인 및 생성
if not os.path.exists(ADD_PATH):
    os.mkdir(ADD_PATH)

# 메뉴 선택 및 실행
while True:
    print('\n'+menu)
    select = input('메뉴를 선택하세요. : ')
    # 전체보기
    if select == '1':
        adrGetAll()
    # 검색
    elif select == '2':
        src = input('검색 단어 : ')
        srcInfo(src)
    # 추가
    elif select == '3':
        print('주소록에 추가할 정보를 적어주세요.')
        name = input('이름 : ')
        phNum = input('전화번호 끝자리 : ')
        address = input('지역 : ')
        addInfo(name, phNum, address)
        print('< 저장되었습니다. >')
    # 종료
    elif select == '4':
        break
    else:
        print('< 해당 메뉴가 없습니다 >.')





