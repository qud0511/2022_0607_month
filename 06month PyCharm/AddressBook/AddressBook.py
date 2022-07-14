#코드로 디렉토리 생성
import os

dataPath='./AddressBook/'
dataList=os.listdir(dataPath)#폴더 안에 파일 리스트를 가져오는 기능

def printMenu():
    print('='*7+'ADDRESSBOOK'+'='*7)
    print(' '*7+'1. 전체보기')
    print(' '*7+'2. 검   색')
    print(' '*7+'3. 추   가')
    print(' '*7+'4. 종   료')
    print('='*25)

def showAddr():#전체 파일 보여 주는 함수
    print('전체 보기')
    for addr in dataList:
        print(addr)
    print('\n', end='')

def searchInfo():#파일명 리스트 안에서 해당 검색어 존재 여부 체크
    i=0
    word=input('검색 단어: ')
    while i<len(dataList):
        if word in dataList[i]:#정보가 있을 때
            print(f'파일명: {dataList[i].replace(".txt","")}')
            filename=dataPath+dataList[i]
            with open(filename,mode='r',encoding='utf-8') as file:
                while True:
                    inform=file.read()
                    if not inform: break#정보가 없으면 벗어남
                    print(inform)
        i+=1
    print('\n',end='')

def addAddr():
    inform=input('이름, 전화번호, 지역, 이메일 (예: 홍길동,010-xxxx-xxxx,서울,xxx@xxx.xxx) => ')#추가할 정보들 입력
    txt=inform.split(',')
    filename=txt[0]+'_'+txt[1][-4:]+'.txt'
    dataList.append(txt[0]+'_'+txt[1][-4:]+'.txt')
    with open(dataPath+filename,mode='w',encoding='utf-8') as file:
        file.write(inform)

def initApp():#개인 주소록 저장 함수
    if not os.path.exists(dataPath): os.mkdir(dataPath)#폴더 존재 여부에 따른 생성
    print(dataList)

initApp()

while True:
    printMenu()#메뉴 출력
    select=int(input('메뉴 선택: '))#사용자로 부터 메뉴 선택 받기
    if select==4:break
    elif select==1: showAddr()
    elif select==2: searchInfo()
    elif select==3: addAddr()
    else: print('해당 메뉴는 존재하지 않습니다.')