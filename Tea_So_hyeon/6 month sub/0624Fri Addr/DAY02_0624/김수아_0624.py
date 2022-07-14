menu='''
=== 나의 주소록 ===
    1. 전체보기
     2. 검 색
     3. 추 가
     4. 종 료
==================
'''
DIR_PATH='./AddressBook'
import os.path as path
import os

def initApp():
    if not path.exists(DIR_PATH):
        os.mkdir(DIR_PATH)

# ====================================
# 기능 : 현재 정보 출력
# 함수명 : printInfo
# 파라미터 : 없음
# 반환값 : 없음
def printInfo():
    dataList = os.listdir(DIR_PATH)
    for data in dataList:
        print(data[:-4])  # .txt 빼고
# ====================================


# ====================================
# 기능 : 정보 추가
# 함수명 : addInfo
# 파라미터 : str
# 반환값 : 없음
def addInfo(info):
    info_split = info.split(',')
    result = []
    # result에 strip한 이름, 전화번호, 지역 담기
    for i in info_split:
        result.append(i.strip())
    filename = result[0] + '_' + result[1]  # filename = 홍길동_1111
    with open(DIR_PATH + '/' + filename + '.txt', mode='w', encoding='utf-8') as file:
        file.write(info)
# =========================================================

# =========================================================
# 기능 : 검색
# 함수명 : searchInfo
# 파라미터 : str
# 반환값 : 없음
def searchInfo(sch):
    dataList = os.listdir(DIR_PATH)
    for data in dataList:
        if sch in data:
            print(f'파일명 : {data[:-4]}')
            with open(DIR_PATH+'/'+data, mode='r', encoding='utf-8') as f:
                print(f.read())
# =========================================================

print('----프로그램 시작----')
initApp()
while True:
    print(menu)
    question=input("메뉴 선택 : ")
    if question in ('1', '2', '3', '4'):
        if question=='4': break   # 4번 입력하면 종료
        else:
            if question=='1':   # 전체보기
                printInfo()

            elif question=='3':    # 정보 추가하기
                info = input("이름, 전화번호, 지역 : ")
                addInfo(info)

            elif question=='2':   # 검색하기
                sch=input("검색 단어 : ")
                searchInfo(sch)

    else: print('1, 2, 3, 4 중에 선택하세요')