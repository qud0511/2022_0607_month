def print_f():
    print("=== 나의 주소록 ===")
    print("1. 전체보기")
    print("2. 검   색")
    print("3. 추   가")
    print("4. 종   료")
    print("=================")
print_f()

filename = '이름_전화번호.txt'
with open(filename, mode='a', encoding='utf-8') as f:
    while True:
        sel = input("메뉴 선택 : ")

        if sel in '1':
            file = open(filename, mode='r', encoding='utf-8')
            data = file.read()
            print(f'전체 보기\n{data}')


        elif sel in '3':

            add = input('이름, 전화번호, 지역, 이메일 :')
            f.write(add + '\n')

        elif sel in '2':
            s = input("검색 단어 : ")
            file = open(filename, mode='r', encoding= 'utf - 8')
            data = file.readlines()

            for i in data:
                if s in i:
                    print(f'파일명 : {i[:i.rindex("")]}')
                    print(f'{" ".join(i.split(" "))}')
        elif sel in '4': break

        else:
            print("잘못된 값이 입력 되었습니다.")









