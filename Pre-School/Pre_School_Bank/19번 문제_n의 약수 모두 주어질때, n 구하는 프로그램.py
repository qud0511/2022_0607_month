# https://intrepidgeeks.com/tutorial/baijun-1037-mineral-water-python

n = int(input())
a = list(map(int, input().split()))

print(max(a) * min(a))



# ---------------------------------


N = int(input())

A = list(map(int, input().split()))

max_nbr = max(A)
min_nbr = min(A)

print(max_nbr * min_nbr)


# ---------------------------------


n = int(input("약수의 개수를 입력하시오: "))
a = list(map(int, input("1과 자기자신을 제외한 약수를 띄어서 입력하시오: ").split()))

print(max(a) * min(a))

