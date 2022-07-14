'''
adressbook.py에서 모듈을 추가하여 만든 프로그램
[1]프로그램 초기화 기능 함수
[2]파일 & 폴더 관련  모듈 활용
 -파일명 저장 리스트 존재 여부 선택
'''
import os.path as path
import os

#기본 함수
'''
메뉴 출력 함수
함수명:printMenu
파라미터: 없음
리턴값: 없음
'''
def printMenu():
    print('''=== 나의 주소록 ===
    1. 전체보기
    2. 검   색
    3. 추   가
    4. 종   료
    5. 초 기 화
    =================''')

#전체보기 함수
'''
함수명:showAddress
파라미터: 파일명 리스트(list)
리턴값:없음
'''
def showAdress(list):
    print(f"전체 보기")
    for dl in list:
        if 'txt' in dl:
            print(dl.split('.')[0])

#검색 함수
'''
함수명:searchAddress
파라미터:찾을 문자열(fin), 파일명 리스트(list)
리턴값:없음
'''
def searchAddress(fin,list):
    for dl in list:
        if fin in dl:
            print(f"파일명 : {dl.split('.')[0]}")
            with open(DIR_PATH+dl,mode='r',encoding='utf-8') as f:
                print(f"정보 : {f.read()}")
            print()

#추가 함수
'''
함수명:addAddress
파라미터:이름,전화번호,지역,이메일 or 함수 안에서 입력을 받으면 없어도 됨
리턴값:없음
'''
def addAddress(name,phone,loc,email):
    filename=name+'_'+phone+'.txt'
    with open(filename,mode='w',encoding='utf-8') as f:
        f.write(name+' '+phone+' '+loc+' '+email)

#초기화 함수
'''
함수명:initApp
파라미터:파일명 리스트(list)
리턴값:없음
'''
def initApp(list):
    list.clear()
    print(f"초기화 하였습니다.")

#폴더가 없을 경우 생성하는 함수
'''
함수명:checkFolder
파라미터:이름,전화번호,지역,이메일 or 함수 안에서 입력을 받으면 없어도 됨
리턴값:없음
'''
# DIR_PATH='./DATA'
# if not path.exists(DIR_PATH):
#     os.mkdir(DIR_PATH)

#프로그래밍 구현
DIR_PATH='../AddressBook/' #파일 저장 폴더
dirList = os.listdir(DIR_PATH.rstrip('/'))
dataList = []
for dl in dirList:
    if 'txt' in dl:
        dataList.append(dl)
while True:
    if not path.exists(DIR_PATH):
        os.mkdir(DIR_PATH)
    printMenu()
    select = input('메뉴 선택: ')
    if select=='1':
        showAdress(dataList)
    elif select=='2':
        sear = input('검색 단어 : ')
        for dl in dataList:
            if not sear in dl:
                print('다시 입력하세요')
                continue
        searchAddress(sear,dataList)
    elif select=='3':
        jungbo = input('이름,전화번호,지역,이메일 : ex:홍길동,xxx-xxxx,대구,a@000.000 ').split(',')
        addAddress(jungbo[0], jungbo[1], jungbo[2], jungbo[3])
        dataList.append(jungbo[0]+'_'+jungbo[1]+'.txt')
    elif select=='4':
        break
    elif select=='5':
        initApp(dataList)
    else:
        print(f'1~5가 아니므로 다시 입력하세요.')