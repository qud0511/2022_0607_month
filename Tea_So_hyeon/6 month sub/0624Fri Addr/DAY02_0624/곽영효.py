# Global --------------------------
DIR_PATH = './AddressBook/'         # 파일 저장 폴더

import os
if not os.path.exists(DIR_PATH):    # AddressBook 폴더 존재 여부 체크 없으면 만들기
    os.makedirs(DIR_PATH)

fileList = os.listdir(DIR_PATH)     # 주소록 안 파일들의 이름 리스트

# 함수 세팅 -----------------------
def printMenu():                    # 초기 화면
    print(f'{"나의 주소록":=^16}\n1. 전체보기\n2. 검   색\n3. 추   가\n4. 종   료\n{"=" * 19}\n')

def showAddress():                  # 전체 출력
    print('등록된 주소를 전부 표시합니다.')
    for file in fileList:
        print(file[:-4])

def searchAddress(name_phone):      # 검색
    for file in fileList:
        if name_phone in file:
            print(f'파일명 : {file[:-4]}')
            with open(DIR_PATH+file, mode = 'r', encoding = 'utf-8') as f:
                print(f'정 보 : {f.read()}')

def addAddress(info):               # 추가
    info = info.replace(" ", "")    # 공백 제거
    info = info.split(',')          # 항목 별로 나누어서 리스트로 만들기

    filename = f'{"./AddressBook/" + info[0] + "_" + info[1][-4:] + ".txt"}'
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(f'{info}\n')
# 구현화 ----------------------------
print('프로그램이 시작되었습니다.')
while True:
    printMenu()

    select = int(input("메뉴 선택 : "))
    if select == 1: showAddress()

    elif select == 2:
        search = input("이름 또는 전화번호 마지막 4자리 숫자로 검색 (ex. 7807)")
        searchAddress(search)

    elif select == 3:
        info = input("이름, 전화번호, 지역, 이메일을 입력해주세요. (ex. AAA, 0104567890, 대구, aaa@aaa.aaa)\n")
        addAddress(info)

    elif select == 4:
        print("프로그램을 종료합니다.")
        break

    else: print("잘못된 접근입니다.")