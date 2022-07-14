friends = ['이동혁_0606','나재민_0808','전동석_8282','박은태_4545']

select = 0
while select != 4:
    print(" === 나의 주소록 ===")
    print("1. 전체보기")
    print("2. 검   색")
    print("3. 추   가")
    print("4. 종   료")
    print("=================")
    select = int(input("메 뉴 선 택 : "))

    if select == 1:
        i = 0
        print("전체 보기")
        while i < len(friends):
            print(friends[i])
            i += 1

    elif select == 2:
        s_name = input("검색 단어 : ")
        friends = " ".join(friends)
        friends = friends.replace("_", " ").split()
        if s_name in friends:
            result = friends[friends.index(s_name) // 2]
            print(result)
            file = f'{result}.txt'
            with open(file, mode='r', encoding='utf-8') as file:
                print(file.read())
        else:
            print("검색 결과 없습니다.")

    elif select == 3:
        a_name = input("이름, 전화번호, 지역, 이메일 => ")
        txt = a_name.split(',')
        file_name = txt[0] + '_' + txt[1][-4:] + '.txt'
        friends.append(txt[0] + '_' + txt[1][-4:])
        with open('./AddressBook/' + file_name, mode='w', encoding='utf-8') as file:
            file.write(a_name)

    elif select == 4: break

    else: print("다른 번호를 입력하세요.")

