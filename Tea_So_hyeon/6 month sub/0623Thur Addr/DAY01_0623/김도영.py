#----------------------------------
# === 나의 주소록 ===
# 1. 전체보기
# 2. 검    색
# 3. 추    가
# 4. 종    료
# ==================
# 메뉴 선택:
#-----------------------------------
list=[]                             #틀린 것이 많아요... 알려주시면 감사하겠습니다!
while True:
    print(" === 나의 주소록 === ")
    print("  1. 전체보기\n  2. 검   색\n  3. 추   가\n  4. 종   료")
    print(" ================= ")
    n=int(input("메뉴 선택:"))
    if n==1:                        #결과가 왜 안나오는 건가요?
        for i in list:
            i=i[:i.ridex(".")]
            print(i)

    elif n==2:               #이건 오류가 뜹니다.
        b=input("연락처 알려드립니다. 이름을 적어주세요: ")
        if i in list:
            if b in i:
                with open(i,'r',encoding='utf-8') as phone:
                    print(phone.line())

    elif n==3:                   #오류가 뜬 후에 txt파일이 생겨요.
        c=input("이름 전화번호를 적어 추가해 주세요: ")
        c1=c+'.txt'
        list.append(c1)
        with open(c1,'w',encoding='utf-8') as c2:
            print(c2.write(c))

    elif n==4:
        break

    else:
        print('잘못된 입력입니다. 다시 입력하세요.')