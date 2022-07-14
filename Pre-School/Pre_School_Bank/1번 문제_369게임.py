# https://the-dev.tistory.com/69

n= int(input('숫자를 입력하세요'))
for i in range(1,n+1):
    s=str(i)
    count=0
    for x in s :
        if (x=='3') or (x=='6') or (x=='9'):
            count+=1
    if count == 0:
        print(i, end=' ')
    else :
        print(count*'X', end=' ')


# https://www.youtube.com/watch?v=Q8BWB6lp7wM

a= int(input('숫자를 입력하시오'))

for a in range(1,a+1):
    c=str(a).count('3') + str(a).count('6') + str(a).count('9')
    if c == 0:
        print(a, end=' ')
    else:
        print('X'*c, end=' ')







a = int(input("숫자를 입력하세요:"))

for i in range(1, a + 1):
    s = str(i)
    count = 0
    for j in s:

        if (j == '3') or (j == '6') or (j == '9'):
            count += 1

    if count == 0:

        print(i, end=" ")
    else:

        i = '#' * count
        print(i, end=" ")

a = int(input("숫자를 입력하세요:"))

for i in range(1, a + 1):
    s = str(i)
    count = 0
    for j in s:

        if (j == '3') or (j == '6') or (j == '9'):
            count += 1

    if count == 0:

        print(i, end=" ")
    else:

        i = '#' * count
        print(i, end=" ")


# initialization