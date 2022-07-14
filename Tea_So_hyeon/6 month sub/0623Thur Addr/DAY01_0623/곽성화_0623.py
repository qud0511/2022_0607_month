# -----------------------------------------------------
# 아직 2번 기능 작성 중입니다...ㅜㅜㅜ
# -----------------------------------------------------
'''
1. 목차 계속 출력
2. 1~4 외에 눌렀을 때, 없는 메뉴 입니다 출력 후 목차 다시 제공
3. 4 입력 시, 목차 종료
4. 추가 만들기, 파일로도 만들기
5. 전체보기
6. 검색
'''
# -----------------------------------------------------

# import os           # 멤버추가 후 users가 누적되지 않아 폴더 목록에서 파일명을 가져오는 방법을 찾았는데, users변수를 while 밖으로 배치하면서 해결하였습니다.

# 입력받은 값을 개인별 파일에 기록하는 함수
def fileAdd(filename):
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write('이름 : ' + user[0] + '\n')
        f.write(f'전화번호 : {user[1]}\n')
        f.write(f'지역 : {user[2]}\n')

menu="""
=== 나의 주소록 ===
   1. 전체보기
   2. 검   색
   3. 추   가
   4. 종   료
=================
"""
users=[]
# users=['hwa_7594', 'mama_7547', 'papa_9330', 'bro_5181', 'hwa_1234']

while True:
    print(menu)
    choose=input('메뉴 선택 : ')

    # 1 입력했을 경우 => 전체 주소록 보기
    if choose in ['1']:
        print('전체 보기')
        for i in range(0, len(users)):
            print(users[i])

    # 2 입력 했을 경우 => 검색 단어 들어간 파일명 모두 출력
    elif choose in ['2']:
        word=input('검색 단어 : ')
        # print(word, type(word))
        # print(users, type(users))
        r=[s for s in users if word in s]
        for i in range(0, len(r)):
            print(f'파일명 : {r[i]}')
            with open(filename, mode='r', encoding='utf-8') as f:
                data = f.read()  # 파일 전체 데이터 가져오기
                print(data)

        # for a in users:
        #     if word in a:
        #         print(f'파일명 : {users.index(word)}')
        #     else:
        #         print('해당 검색 단어가 없습니다.')

    # 3 입력했을 경우 => 이름_전화번호.txt. 파일 생성
    elif choose in ['3']:
        # 자료 입력 받기
        user=list(input('이름 전화번호 지역 : ').split())
        print(f'입력된 값 : {user}', type(user))

        # 파일 생성
        filename=f'{user[0]}_{user[1]}.txt'
        print(f'생성된 파일명 : {filename}')
        fileAdd(filename)

        # 생성된 user 리스트에 담기
        users.append(f'{user[0]}_{user[1]}')
        print(f'저장된 주소록 : {users}')

    # 4 입력했을 경우 => 종료
    elif choose in ['4']:
        break

    # 1~4 외의 값을 입력했을 경우
    else:
        print('없는 메뉴입니다. 다시 입력하세요.')




#
# path = "./"
# file_list = os.listdir(path)
#
# # 확장자명 입력
# file_list_txt = [file for file in file_list if file.endswith(".txt")]

# print(file_list_txt, type(file_list_txt))
# print(file_list_txt[0], type(file_list_txt[0]))
# print(file_list_txt[0][:file_list_txt[0].index(".")])

# for i in
# print(file_list_txt[0][:file_list_txt[0].index(".")])
