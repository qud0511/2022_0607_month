databaseList = []
while True:
    print('\n')
    print('==== 나의 주소록 ====')
    print('     1.전체보기     ')
    print('     2.검   색     ')
    print('     3.추   가     ')
    print('     4.종   료     ')
    print('===================')
    num = input("======== 메뉴 선택 ========>")

    if num in '1' :
        print(databaseList)

    elif num in '2' :
        data = input("검색하십시오")
        for i in databaseList:
            if data in i:
                f=open(i+'.txt',mode='r', encoding='utf-8')
                print(f.read())
                f.close()

    elif num in '3' :
        data = input('이름,전화번호,지역: ')
        filename = data.split(',')[0]+'_'+data.split(',')[1]
        f = open(filename+'.txt', mode='a', encoding='utf-8')
        f.write(data)
        f.close()
        databaseList.append(filename)

    elif num in '4' :
        break

    else :
        print("잘못된 데이터입니다.")





