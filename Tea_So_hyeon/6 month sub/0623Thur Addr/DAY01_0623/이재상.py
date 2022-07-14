info=['홍길동_1234','홍길동 01012341234 대구','마징가_1111','마징가 01011111111 부산','배트맨_2323', '배트맨 01023232323 서울']
result=[]
number=0
while number !=4:
    print('===나의 주소록===\n1.전체보기\n2.검   색\n3.추   가\n4.종   료\n===============\n메뉴 선택 : ')
    number=int(input())
    if number<=0 or number>=5:
        print("잘못 입력했습니다. 다시 입력하세요.")
    elif number==1:
        print("홍길동_1234\n마징가_1111\n배트맨_2323")
    elif number==2:
        word=input(f'검색단어 : ')
        for i in info:
            if word in i:
                result.append(i)
        print(f'파일명 : {result[0]}\n{result[1]}')
    elif number==3:
        name = input(f'이름 : ')
        pn = input(f'전화번호 : ')
        state = input(f'지역 : ')
        email = input(f'이메일 : ')
        filename = f'{name}_{pn}.txt'
        file = open(filename, mode='a', encoding='utf-8')
        file.write(f'이름 : {name}''\n'f'전화번호 : {pn}''\n'f'지역 : {state}''\n'f'이메일 : {email}')
        file.close()
    else : break