# 기본값 주소록 리스트 만들기
f1='나얼_1111.txt'
file=open(f1,'w',encoding='utf8')
file.write('나얼, 010-1111-2222, 대구')
file.close()

f2='박효신_2222.txt'
file=open(f2,'w',encoding='utf8')
file.write('박효신, 010-2222-3333, 대전')
file.close()

f3='김범수_3333.txt'
file=open(f3,'w',encoding='utf8')
file.write('김범수, 010-3333-4444, 서울')
file.close()

f4='김범수_4444.txt'
file=open(f4,'w',encoding='utf8')
file.write('김범수, 010-4444-5555, 부산')
file.close()

list=[f1,f2,f3,f4]
while True:
    print("=== 나의 주소록 ===")
    print("1.전체보기")
    print("2.검색하기")
    print("3.추가하기")
    print("4.종료하기")
    print("==============")
    commend=input("메뉴 선택: ")
    if commend=="1":
        print("전체보기")
        for i in list:
            i=i[:i.rindex(".")]  #파일명에서 .txt 지우기
            print(i)

    elif commend=="2":
        user=input("검색 단어: ")
        for i in list:
            if user in i:
                file=open(i,'r',encoding='utf8')
                result=file.read()
                print(result)
                file.close()

    elif commend=="3":
        user1=input("이름, 전화번호,지역을 입력(ex)나얼,010-4444-3333,대구 : ")
        user2=user1.split(",") # split으로 자동으로 list로 변환.

        f=user2[0]+"_"+user2[1][4:8]+".txt" # 저장될 파일명: 이름_전화번호 가운데 4자리.txt

        file=open(f,'w',encoding="utf8")
        file.write(user1)
        list.append(f)
    elif commend=="4": break
    else:
        print("1,2,3,4 중 하나를 입력해주세요.")