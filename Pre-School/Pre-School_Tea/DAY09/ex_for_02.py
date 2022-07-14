# ---------------------------------------
# 구구단 전체 출력하는 프로그램
# ---------------------------------------
for dan in range(2,10):
    print(f'---{dan}단---')
    for num in range(1,10):
        print(f'{dan} * {num} = {dan * num}')

# ---------------------------------------
# 숫자 문자열의 합계 구하는 프로그램
# ---------------------------------------
money='123,456,789'
total=0
for m in money:
    if m == ',': continue
    total=total+int(m)
    print(m, total)

# ---------------------------------------
# 문자열에 대한 코드값 출력하는 프로그램
# 문   자-> 코드값 알려주는 내장함수 : ord(문자1개)
# 코드값 -> 문 자  알려주는 내장함수 : chr(숫자)
# ---------------------------------------
msg="2020 Happy Year~!"
codeMsg=''
for m in msg:
    print(m, ord(m), bin(ord(m)), hex(ord(m)))
    codeMsg = codeMsg+bin(ord(m))
print(codeMsg)
