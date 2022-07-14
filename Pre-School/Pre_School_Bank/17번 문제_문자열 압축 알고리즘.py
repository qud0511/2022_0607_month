s = input()

result = s[0]
count  = 0

for st in s:
    if st == result[-1]:
        count += 1
    else:
        result += str(count) + st
        count = 1
result += str(count)

print(result)

# ---------------------------------------

def func():
    s = input("문자열을 입력해주세요: ")
    result = s[0]
    cnt = 0
    for i in s:
        if i == result[-1]:
            cnt = cnt + 1
        else:
            result = result + str(cnt) + i
            cnt = 1
    result = result + str(cnt)

    print(result)

func()