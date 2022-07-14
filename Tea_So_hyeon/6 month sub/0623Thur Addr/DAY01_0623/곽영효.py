# --------------------------
import os
fileList = os.listdir('AddressBook')

while True:
    select = int(input(f'{"나의 주소록":=^16}\n1. 전체보기\n2. 검   색\n3. 추   가\n4. 종   료\n{"=" * 19}\n'))

    if select == 1:
        print("메뉴 선택 : 1")

        for file in fileList:
            file = file.split('.')[0]
            print(file)

    elif select == 2:
        print("메뉴 선택 : 2\n")
        search = input("검색 단어\n")

        for file in fileList:
            x = open(f'{"./AddressBook/" + file}', mode = 'r', encoding='utf-8')
            data = x.read()
            if search in data:
                print(file[:-4])
                print(data)

    elif select == 3:
        print("메뉴 선택 : 3")
        info = input("이름, 전화번호, 지역, 이메일을 입력해주세요. (ex. AAA, 0104567890, 대구, aaa@aaa.aaa)\n")
        info = info.replace(" ", "")
        info = info.split(',')

        filename = f'{"./AddressBook/" + info[0] + "_" + info[1][-4:] + ".txt"}'
        with open(filename, mode = 'w', encoding= 'utf-8') as file:
            file.write(f'{info}\n')

    elif select == 4:
        print("메뉴 선택 : 4")
        break

    else : print("잘못된 접근입니다. 다시 선택해주세요.")