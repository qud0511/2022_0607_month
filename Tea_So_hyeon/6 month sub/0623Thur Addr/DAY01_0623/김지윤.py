list = ['마징가_111', '홍길동_1234']
while True:
    print('=== 나의 주소록 ===')
    print('    1.전체보기     ')
    print('    2.검   색     ')
    print('    3.추   가     ')
    print('    4.종   료     ')
    print('=================')
    num = input("메뉴 선택: ")
    if num == '4':
        break
    elif num =='1':
        print(list)
    elif num == '3':
        data = input('이름,전화번호,지역: ')
        filename = data.split(',')[0]+'_'+data.split(',')[1]
        f = open(filename+'.txt', 'w')
        f.write(data)
        f.close()
        list.append(filename)
    elif num == '2':
        data = input("검색단어: ")
        for i in list:
            if data in i:
                f=open(i+'.txt',mode='r', encoding='utf-8')
                print(f.read())
                f.close()
    else:
        print("숫자를 잘못 입력함")













