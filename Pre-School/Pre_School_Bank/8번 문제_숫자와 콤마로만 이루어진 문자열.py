sum=0
a=input(' ')
b=a.split(',')
b=list(map(int,b))
for i in range(len(b)):
    sum=sum+b[i]
print(sum)


# https://homzzang.com/b/py-303

x = input().split(',')
def sum_all(a):
    sum = 0
    for i in range(len(a)):
        sum = sum + int(a[i])
    return sum
print(sum_all(x))



a = str(input())

result = 0

a = a.replace(',','')
list(a)
a = sorted(a)

for i in a:
    result += int(i)

print(result)

# -----------------------------

x = input()
x = x.replace(',','')
sum = 0
for i in range(len(x)):
    sum += int(x[i])
print(sum)

# ----------------------------

x = input()
x = x.replace(',','')
sum = 0
for i in range(len(x)):
    sum += int(x[i])
print(sum)

s=input('132,42,98,18').replace(',','')

sum = 0

for i in range(len(s)):
    sum += int(s[i])

print(sum)
