a="GooD"
a.swapcase()

# .lower()
# .upper()
# .swapcase()
# .title()    --> 첫 문자만 대문자로


user=input('문자를 입력하세요')
if user.islower():
    print(user.upper())
else: print(user.lower())