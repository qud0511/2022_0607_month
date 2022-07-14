def fibo(n):
    if n ==1 or n ==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

user=int(input('n번째 피보나치수열'))

print(f' {user}번째 피보나치수열은 {fibo(user)}입니다.')

# -----------------------------

n = int(input())
def fibo2(n):
    a = 1
    b = 1
    if n == 1 or n == 2:
        return 1
    for i in range(1, n):
        a, b = b, b + a
    return a

# --------------------------

num = int(input())


def fib(num):
    n1 = 1
    n2 = 1

    for i in range(2, num):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    return n1


print(fib(num))






