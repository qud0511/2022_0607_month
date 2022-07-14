

def get_divisor(n):
    n=int(n)
    divisors=[]
    for i in range(1,n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

print(get_divisor(34))



# ---------------------------------------
n = int(input())

for i in range(1, n+1):
    if n%i == 0:
        print(i, end=' ')



# -----------------------------
n= int(input('숫자 입력하시오'))

num_list=[]

for i in range(1,n+1):
    if n%i ==0:
        num_list.append(i)

print(sorted(num_list, reverse=True))





















