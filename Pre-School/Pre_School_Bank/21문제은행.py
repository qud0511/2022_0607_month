# 1번
n=int(input('369게임 숫자입력하시오'))

for n in range(1,n+1):
    s=str(n).count('3')+str(n).count('6')+str(n).count('9')
    if s == 0:
        print(n, end=' ')

    else:
        print('X'*s, end=' ')


print('\n')

n=int(input('369게임'))

for i in range(1,n+1):
    count=0
    s=str(i)
    for x in s:
        if x == '3' or x == '6' or  x =='9':
            count+=1

    if count == 0:
        print(i, end=' ')

    else:
        print('X'*count, end=' ')

# -----------------------------

#2번
print('\n')

n=int(input('공을 몇번 떨어뜨릴 것인지 입력하시오'))

h=100
for i in range(1,n+1):
    h=h*0.6
    print(f'{i}번째, {round(h, 4)}높이')

# -----------------------------

# 3번

money=int(input('가지고 있는 금액 입력'))
cost=int(input('제품 가격'))
change=money-cost

c_50000= change // 50000
c_10000= (change % 50000) // 10000
c_5000= (change % 10000) // 5000
c_1000= (change % 5000) // 1000

print(f'50000원권 지폐는 {c_50000}장입니다.')
print(f'10000원권 지폐는 {c_10000}장입니다.')
print(f'5000원권 지폐는 {c_5000}장입니다.')
print(f'1000원권 지폐는 {c_1000}장입니다.')

# -----------------------------

# 4번





# -----------------------------

# 5번
import calendar

mon=int(input('월(month)를 입력해주세요'))

if mon ==12 or mon ==1 or mon ==2:
    print('winter')

elif mon ==3 or mon ==4 or mon ==5:
    print('spring')

elif mon ==6 or mon == 7 or mon==8:
    print('spring')

elif mon ==9 or mon ==10 or mon ==11:
    print('fall')

if mon >=1 or mon <=12:
    print(calendar.month_name[mon], end=' ')

else:
    print('잘못된 데이터입니다.')

# -----------------------------

# 6번
a = int(input())
li=[]

for n in range(2,a+1):
    check=True
    for i in range(2,n):
        if n%i == 0:
            check= False

    if check:
        li.append(n)

print(li)

# -------

a=int(input('숫자 입력'))
for i in range(2, a+1):
    is_prime = True
    for j in range(2, i):
        if i%j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=" ")



# -----------------------------

# 7번
for i in range(1,6):
    print(' '*(5-i), '*'*i)

# -----------------------------

# 8번

# 1 + 3 + 2 + 4 + ... +8
s=input('132,42,98,18').replace(',','')

sum = 0

for i in range(len(s)):
    sum += int(s[i])

print(sum)

# 132 + 42 + 98 + 18
s=input('132,42,98,18').split(',')

sum = 0

for i in range(len(s)):
    sum += int(s[i])

print(sum)

# -----------------------------

# 9번

msg= input('문자열을 입력하시오')

if msg == msg[::-1]:
    print(msg, '팰린드롬')
else:
    print('팰린드롬이아닙니다.')


# -----------------------------
# 10번

for i in range(1,11):
    print(' '*(11-i),'*'*((2*i)-1))
for i in range(1,4):
    print(' '*9, '*'*3)

# -----------------------------
# 11번
n=int(input('피보나치 n번째 수열'))

def fibo(n):
    if n==1 or n==2:
        return 1

    else:
        return fibo(n-1)+fibo(n-2)

print(f'{n}번째 수열은 {fibo(n)}입니다.')
# -----------------------------
# 12번

a,b,c=map(int, input('3개 정수를 입력하시오.  예시: 284,7,93').split(','))

print(f' 가장 큰수 : {max(a,b,c)}')
print(f' 가장 작은 수 : {min(a,b,c)}')

# -----------------------------
# 13번

msg=input('문자열 리스트를 입력하시오')

a= list(msg)
a.sort()

print(max(a), min(a))


# -----------------------------


# 14번
msg=input('대소문자가 섞인 아무 영어를 입력하시오')

print(msg.swapcase())

# -----------------------------

# 15번
import operator

a_dic = {"마징가":[187.5, 91], "베트맨":[174.9, 102.3], "홍길동":[192, 72], "가가멜":[167.2, 89.3]}

sorted_a_dic=sorted(a_dic.items(), key=operator.itemgetter(1))

print(sorted_a_dic)

# -----------------------------

# 16번

n= int(input('숫자 입력하시오'))

num_list=[]

for i in range(1,n+1):
    if n%i ==0:
        num_list.append(i)

print(sorted(num_list, reverse=True))








