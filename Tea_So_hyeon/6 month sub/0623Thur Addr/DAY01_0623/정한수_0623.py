# ------------------------------------------------------
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

# 메뉴 출력
#   함수명 : run
#   반환값 : menu_num
# ------------------------------------------------------

import os
number_list = sorted([x.strip('.txt') for x in os.listdir('AddressBook')])
data_list = ['이름', '전화번호', '지역', '이메일']

def showAll():
    print('\n===  전체 보기  ===')
    for file_name in number_list:
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

    for file_name in number_list:
        with open('AddressBook/' + file_name + '.txt', 'r', encoding='utf-8') as f:
            data = f.read().split('\t')
        if search_word in data[search_menu-1]:
            print('')
            print('파일명 : ' + file_name)
            print('=================')
            for i in range(len(data_list)):
                print('{}: {}'.format(data_list[i], data[i]))
            print('=================')


def addData():
    data = input("이름, 전화번호, 지역, 이메일 순서대로 입력해 주세요 \n: ")
    data = [x.strip().strip(',') for x in data.split(' ')]

    file_name = data[0]+'_'+data[1]
    with open('AddressBook/'+file_name+'.txt', 'w', encoding='utf-8') as f:
        for d in data:
            f.write(d+'\t')
    global number_list

    number_list.append(file_name)
    number_list = sorted(number_list)

def removeData():
    name = input('지우려는 목록 (성명_전화번호)를 입력해 주세요 \n: ')
    global number_list
    number_list.remove(name)
    os.remove('AddressBook/'+name+'.txt')
    number_list = sorted(number_list)


def run():
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


if __name__ == '__main__':
    while True:
        menu_num = run()
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
