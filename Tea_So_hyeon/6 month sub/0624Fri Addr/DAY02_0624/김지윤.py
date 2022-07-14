import os
DataList = os.listdir('./Address book')
Dir_Path = './Address book/'
if not os.path.exists(Dir_Path): os.mkdir(Dir_Path)
while True:
    print('=== 나의 주소록 ===')
    print('    1.전체보기     ')
    print('    2.검   색     ')
    print('    3.추   가     ')
    print('    4.종   료     ')
    print('=================')
    num = input("메뉴 선택: ")

    if num =='1':
        print(DataList)
    elif num == '3':
        data = input('이름,전화번호,지역: ')
        filename = data.split(',')[0]+'_'+data.split(',')[1]
        f = open(Dir_Path+filename+'.txt', mode='w', encoding='utf-8')
        f.write(data)
        f.close()
        DataList.append(filename)
    elif num == '2':
        data = input("검색단어: ")
        for i in DataList:
            if data in i:
                f=open(Dir_Path+i, mode='r', encoding='utf-8')
                print(f.read())
                f.close()
    elif num == '4':
        break
    else:
        print("메뉴를 잘못 입력함")