for i in range(1,7):
    if i % 2 == 0:
        for j in range(1,7):
            if j % 2 == 0:
                if i == j:
                    print(i,j,"무승부입니다")
                else:
                    print(i,j,"승부")
    else:
        for j in range(1,7):
            if j % 2 != 0:
                if i == j:
                    print(i,j,"무승부입니다")
                else:
                    print(i,j,"승부")





n1 = int(input("1번 주사위: "))
n2 = int(input("2번 주사위: "))

if n1 or n2 >6 or n1 or n2 < 1:
    print('잘못된 데이터입니다.')

elif n1 == n2:
    print('두 주사위는 동일한 숫자가 나왔습니다.')

elif n1 % 2 == 0 and n2 % 2 == 0:
    print("두 주사위 모두 짝수입니다")
    if n1 == n2:
        print("무승부 입니다")
    elif n1 > n2:
        print("1번 주사위가 이겼습니다")
    elif n1 < n2:
        print("2번 주사위가 이겼습니다")
elif n1 % 2 == 1 and n2 % 2 == 1:
    print("두 주사위 모두 홀수입니다")
    if n1 == n2:
        print("무승부 입니다")
    elif n1 > n2:
        print("1번 주사위가 이겼습니다")
    elif n1 < n2:
        print("2번 주사위가 이겼습니다")
elif n1 % 2 == 0 and n2 % 2 == 1:
    print("1번 주사위는 짝수, 2번 주사위는 홀수입니다")
    if n1 > n2:
        print("1번 주사위가 이겼습니다")
    elif n1 < n2:
        print("2번 주사위가 이겼습니다")
elif n1 % 2 == 1 and n2 % 2 == 0:
    print("1번 주사위는 홀수, 2번 주사위는 짝수입니다")
    if n1 > n2:
        print("1번 주사위가 이겼습니다")
    elif n1 < n2:
        print("2번 주사위가 이겼습니다")

