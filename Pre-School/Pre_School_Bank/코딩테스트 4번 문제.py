n = int(input('248게임, 정수를 입력하시오'))

for i in range(1, n+1):

    c = str(i)

    if c[-1] == '2' or c[-1] == '4' or c[-1] == '8':
        print('#', end="")
    else:
        print(i, end="")
    if i % 20 == 0:
        print("")
