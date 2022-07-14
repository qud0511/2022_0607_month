Files=[]
while True:
    answer=input('''\n=== 나의 주소록 ===
1. 전체보기
2. 검   색
3. 추   가
4. 종   료
================= 
메뉴 선택 : ''')
    if answer=='1':
        print('\n전체 보기')
        for i in Files:
            print(i)

    elif answer=='2':
        print('\n검색')
        serch = input('검색 단어 : ')
        Files2 = " ".join(Files)
        Files2 = Files2.replace("_", " ").split()
        if serch in Files2:
            result=Files[Files2.index(serch) // 2]
            print(result)
            file=f'{result}.txt'
            with open(file,mode='r', encoding='utf-8') as file:
                print(file.read())
        else:
            print("검색 결과 없음")

    elif answer=='3':
        data=input("이름, 전화번호, 지역을 입력해 주세요. \n예) 홍길동 01012345678 대구")
        data1=data.split()
        newFile=f'{data1[0]}_{data1[1][-4:]}.txt'
        Files.append(f'{data1[0]}_{data1[1][-4:]}')
        with open(newFile,mode='w', encoding='utf-8') as newFile:
            newFile.write(data)

    elif answer=='4': break
    else: print('잘못된 입력입니다.')

print(Files)