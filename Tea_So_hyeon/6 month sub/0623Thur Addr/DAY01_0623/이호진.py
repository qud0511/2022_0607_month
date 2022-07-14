friend1='이호진 01011112222 대구.txt'
friend2='홍길동 01022223333 서울.txt'
friend3='아아아 01055556666 경기도.txt'

list=[friend1,friend2,friend3]
while True:
    print("===================")
    print("1.전체보기")
    print("2.검 색")
    print("3.추 가")
    print("4.종 료")
    print("===================")
    myNum=input("메뉴 선택: ")
    if myNum=="1":
        print("전체보기")
        for i in list:
            i=i[:i.rindex(".")]
            print(i)

    elif myNum=="2":
        user=input("검색 단어: ")
        for i in list:
            if user in i:
                file=open(i,'r',encoding='utf-8')
                result=file.read()
                print(result)

    elif myNum=="3":
        user1=input("이름, 전화번호,지역을 입력: ")
        f=user1 + ".txt"

        file=open(f,'w',encoding="utf-8")
        file.write(user1)
        list.append(f)
    elif myNum=="4":
        print("종료")
        break
    else:
        print("잘못된 입력입니다.")