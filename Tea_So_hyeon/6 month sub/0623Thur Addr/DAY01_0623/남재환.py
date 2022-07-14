while True:
    print('===나의 주소록===\n',' 1.전체보기\n',' 2.검   색\n',' 3.추   가\n',' 4.종   료\n','==============')
    num=input('숫자입력: ')
    num=int(num)

    a=({"배트맨":2222})
    b=({"홍길동":2425})
    c=({"강호동":5556})
    if num in [1] : print(f'1.전체보기\n{a}\n{b}\n{c}\n')
    if num in [2] :
        num2=input("입력")
        num2=str(num2)
        if num2 in ["a"] : print(a)
        elif num2 in ["b"] : print(b)
        elif num2 in ["c"] : print(c)
    if num in [3] : num3=input("추가")

    if num in [4] :break





