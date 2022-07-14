menu='''
=== 나의 주소록 ===
    1. 전체보기
     2. 검 색
     3. 추 가
     4. 종 료
==================
'''
names=[]

while True:
    print(menu)
    question=input("메뉴 선택 : ")
    if question in ('1', '2', '3', '4'):
        if question=='4': break
        else:
            if question=='1':
                print('전체보기')
                for name in names:
                    print(name)
            elif question=='3':
                data=input("이름, 전화번호, 지역 : ")
                data_split=data.split(',')
                result=[]
                for d in data_split:
                    result.append(d.strip())
                filename=str(result[0]+'_'+result[1])
                file_address=filename+'.txt'
                with open(file_address, mode='w', encoding='utf-8') as file:
                    file.write(data)
                names.append(filename)
            elif question=='2':
                sch=input("검색 단어 : ")
                for name in names:
                    if sch in name:
                        print(f'파일명 : {name}')
                        with open(name+'.txt', mode='r', encoding='utf-8') as file2:
                            read_file=file2.read()
                            print(read_file)


    else: print('1, 2, 3, 4 중에 선택하세요')