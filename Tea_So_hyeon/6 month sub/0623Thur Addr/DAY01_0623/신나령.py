#- 프로젝트 내의 AddressBook 폴더에 개인별 파일 생성
#- 개인별 파일명 => 이름_전화번호.txt
data=['홍길동_1234','마징가_1111','홍길동_8888','배트맨_2323']
while True:
    num=int(input('=== 나의 주소록 ===\n'
                  '    1.전체보기\n'
                  '    2.검   색\n'
                  '    3.추   가\n'
                  '    4.종   료\n'
                  '=================\n'
                  '메뉴 선택: '))
    if num==4: break
    elif num==1:
        i=0
        print('\n전체 보기')
        while i<len(data):
            print(data[i])
            i+=1
        print('\n',end='')
    elif num==3:
        inform=input('이름, 전화번호, 지역, 이메일 => ')
        txt=inform.split(',')
        filename=txt[0]+'_'+txt[1][-4:]+'.txt'
        data.append(txt[0]+'_'+txt[1][-4:])
        with open('./AddressBook/'+filename, mode='w',encoding='utf-8') as file:
            file.write(inform)
    elif num==2:
        i=0
        word=input('검색 단어: ')
        while i<len(data):
            if word in data[i]:
                print(f'파일명: {data[i]}')
                filename='./AddressBook/'+data[i]+'.txt'
                with open(filename, mode='r', encoding='utf-8') as file:
                    while True:
                        inform=file.read()
                        if not inform: break
                        print(inform)
            i+=1
        print('\n', end='')
    else: print('없는 메뉴입니다.')