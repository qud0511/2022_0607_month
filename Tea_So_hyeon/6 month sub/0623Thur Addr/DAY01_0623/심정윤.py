# 3.추가
# 기    능 : 주소록 추가
# 함 수 명 : addInfo
# 파라미터 : name, phNum, address
# 리 턴 값 : 없음

def addInfo(name, phNum, address):
    fileName=f'{name}_{phNum}.txt'
    file=open(fileName, mode='a', encoding='utf-8')
    file.write(f'''이름 : {name}\n전화번호 : {phNum}\n지역 : {address}\n\n''')      # ''' ''' 했을때 엔터 확인
    file.close()

    # 파일명 정리용
    file=open('주소록 목록', mode='a', encoding='utf-8')                # 코드실행 종료 시 txt만 남아있고 list만 사라지는 것을 방지하기 위해 파일로 저장하였습니다.
    file.write(f'{name}_{phNum}\n')                                             # 이렇게 여러번 open해도 되는건가
    file=open('주소록 목록', mode='r', encoding='utf-8')
    addSet=set(file.readlines())
    addLst=list(addSet)
    addLst.sort()
    file=open('주소록 목록', mode='w', encoding='utf-8')                          # set과 mode='w'는 조금 위험한 선택일지도..
    for l in addLst:
        file.write(l)


# 1.전체보기
# 기    능 : 주소록 전체보기
# 함 수 명 : seeAll
# 파라미터 : 없읍
# 리 턴 값 : 전체 주소록
def seeAll():
    addall=open('주소록 목록', mode='r', encoding='utf-8')
    print(addall.read())

# 2.검색
# 기    능 : 입력받은 정보의 주소록 검색하기
# 함 수 명 : srcInfo
# 파라미터 : src (문자열)
# 리 턴 값 : 파일명, 주소록 정보
def srcInfo(src):
    file=open('주소록 목록', mode='r', encoding='utf-8')
    addlst=file.readlines()
    for lst in addlst:
        if src in lst:
            print(f'파일명 : {lst}')
            Filename=lst[:-1]+'.txt'                            # 왜 [:-1]인지 확인하기
            info=open(Filename,mode='r',encoding='utf-8')
            print(info.read())


# ----------------------------------------------------------

menu = '''=== 나의 주소록 ===
1. 전체보기
2. 검   색
3. 추   가
4. 종   료
===============
'''
namelst = []

while True:
    print('\n'+menu)
    select = input('메뉴를 선택하세요. : ')   #int(input())했을떄 숫자 문자열이 아닐 경우 오류
    # 전체보기
    if select == '1':
        seeAll()
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





