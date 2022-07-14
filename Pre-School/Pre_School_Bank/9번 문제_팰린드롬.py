def is_palindrome(word):
    return word == word[::-1]

# ------------------------

def is_palingdrome2(word):
    if word == word[::-1]:
        print(True)
    else:
        print(False)


print(is_palindrome('기러기'))
print(is_palindrome('abcd'))
is_palingdrome2('토마토')
is_palingdrome2('efgh')


# -----------------

n = input()
c = n[::-1]
if n == c:
    print(1)
else:
    print(0)

# ----------------------

word = input('아무 문자나 입력하시오')
if word == word[::-1]:
    print(1, '팰린드롬입니다.')
else:
    print(0, '팰린드롬이 아닙니다.')



# ---------------------
n = input()

for i in range(0, int(len(n) / 2)):

    chk = 0
    if n[i] == n[-1 - i]:
        chk = 1
print(chk)
