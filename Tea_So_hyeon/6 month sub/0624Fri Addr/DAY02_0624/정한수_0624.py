# 모듈 불러오기 ------------------------------------------
import os

# 전역 변수 ---------------------------------------------
DIR_PATH = './AddressBook/'

# history-----------------------------------------------
# 0623 : 기능 구현
#        삭제 기능 추가, 검색 종류 선택 기능 추가
# 0624 : os 모듈 사용
#           - 폴더 여부 확인 후 없으면 생성
#           - 파일 이름을 저장하던 number_list 변수 제거, DIRlist 함수로 폴더 안에 파일리스트 가져오기
#        입력 기능에서 이름, 전화번호가 같은 자료를 입력할 경우 덮어 씌울지 여부를 묻고 진행

# 함수 설명 ----------------------------------------------
# 1. 전체보기
#   함수명 : showAll

# 2. 검색
#   함수명 : search
#       검색 종류, 검색 단어 입력받고 탐색

# 3. 추가
#   함수명 : addData
#       파일 생성

# 4. 삭제
#   함수명 : removeData
#       파일 제거

# AddressBook 폴더에 있는 문서 리스트 가져오기
#   함수명: DIRlist
#   반환값 : 폴더 이름 리스트

# 메뉴 출력 및 메뉴 입력 받기
#   함수명 : print_menu
#   반환값 : menu_num
# ------------------------------------------------------


def showAll():
    print('\n===  전체 보기  ===')
    for file_name in DIRlist():
        print(file_name)
    print('=================')


def search():
    search_menu = '''
===  검색 종류  ===
\t1. 이름 검색
\t2. 번호 검색
\t3. 지역 검색
\t4. 이메일 검색
================='''
    print(search_menu)

    search_menu = int(input('검색 종류 : '))
    search_word = input('검색 단어 : ')

    success = False
    for file_name in DIRlist():
        with open(DIR_PATH + file_name + '.txt', 'r', encoding='utf-8') as f:
            data = f.read().split('\t')
        if search_word in data[search_menu-1]:
            success = True
            print('')
            print('파일명 : ' + file_name)
            print('=================')
            for i in range(len(data_list)):
                print('{}: {}'.format(data_list[i], data[i]))
            print('=================')

    if not success :
        print('검색 결과가 없습니다.')


def addData():
    data = input("이름, 전화번호, 지역, 이메일 순서대로 입력해 주세요 \n: ")
    data = [x.strip().strip(',') for x in data.split(' ')]

    file_name = data[0]+'_'+data[1]
    if file_name in DIRlist():
        flag = 'y'
        while True:
            flag = input('해당 주소가 존재 합니다. 새로운 정보로 변환 하시겠습니까? \n ( y / n ) : ')
            if flag == 'y':
                with open(DIR_PATH+file_name+'.txt', 'w', encoding='utf-8') as f:
                    for d in data:
                        f.write(d+'\t')
                break
            elif flag == 'n':
                break
            else:
                print('y 또는 n 을 입력해 주세요!\n')



def removeData():
    name = input('지우려는 목록 (성명_전화번호)를 입력해 주세요 \n: ')
    os.remove(DIR_PATH+name+'.txt')


def print_menu():
    menu = '''
=== 나의 주소록 ===
\t1. 전제보기
\t2. 검 색
\t3. 추 가
\t4. 제 거
\t5. 종 료
================='''

    print(menu)
    try:
        menu_num = int(input('메뉴 선택: '))
    except:
        print('메뉴 숫자를 입력해 주세요!')
        menu_num = 0
    return menu_num

def DIRlist():
    # '.txt' 제거 하고 정렬 해서 가져 오도록
    number_list = sorted([x.strip('.txt') for x in os.listdir(DIR_PATH)])
    return number_list

if __name__ == '__main__':
    data_list = ['이름', '전화번호', '지역', '이메일']

    # './AddressBook' 폴더가 존재하지 않는다면 생성
    if not os.path.exists(DIR_PATH.rstrip('/')):
        os.mkdir(DIR_PATH.rstrip('/'))

    while True:
        menu_num = print_menu()
        if menu_num == 1:
            showAll()
        elif menu_num == 2:
            search()
        elif menu_num == 3:
            addData()
        elif menu_num == 4:
            removeData()
        elif menu_num == 5:
            break
        else:
            if not menu_num == 0:
                print('1 ~ 5 사이의 값을 입력해 주세요 !')
