'''
구글 드라이브: https://drive.google.com/drive/folders/1CXBbMeTtQMqKflZFXNa8x4TPwLJze69W
파일명=이름_전호번호.txt

=== 나의 주소록 ===
1. 전체보기
2. 검   색
3. 추   가
4. 종   료
=================
메뉴 선택:

'''
na_tr_li=[]
while True:
    select=int(input('''=== 나의 주소록 ===
1. 전체보기
2. 검    색
3. 추    가
4. 종    료
=================
메뉴 선택: '''))
    print()
    if 0>=select or select>=5:
        print(f'잘못 숫자를 입력하셨습니다. 다시 입력하세요.')
        continue
    elif select==1:
        for fn in na_tr_li:
            print(f"파일명 : {fn}")
            with open(fn,mode='r',encoding='utf-8') as f:
                data=f.read()
                print(data)
    elif select==2:
        sear=input('검색 단어 : ')
        for l in na_tr_li:
            if sear in l:
                print(f"파일명 : {l}")
                with open(l,mode='r',encoding='utf-8') as f1:
                    data1=f1.read()
                    print(data1)
    elif select==3:
        jungbo=['이름','전화번호','지역','이메일']
        jungbo_va=[]
        for i in jungbo:
            val=input(f'{i} >>> ')
            jungbo_va.append(val)
        filenames=jungbo_va[0]+'_'+jungbo_va[1]+'.txt'
        na_tr_li.append(filenames)
        with open(filenames,mode='a',encoding='utf-8') as f:
            for i in range(len(jungbo_va)):
                f.write(f"{jungbo[i]} : {jungbo_va[i]}\n")
    elif select==4:
        break
