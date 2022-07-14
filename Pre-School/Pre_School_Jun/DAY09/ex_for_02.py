# ----------------------------------------------------------
# 구구단 전체 출력하는 프로그램
# ----------------------------------------------------------

for dan in range(2,10):
    print(f'----- {dan}단 -----')
    print(f'{dan} * 1 = {dan * 1}')
    print(f'{dan} * 2 = {dan * 2}')
    print(f'{dan} * 3 = {dan * 3}')
    print(f'{dan} * 4 = {dan * 4}')
    print(f'{dan} * 5 = {dan * 5}')
    print(f'{dan} * 6 = {dan * 6}')
    print(f'{dan} * 7 = {dan * 7}')
    print(f'{dan} * 8 = {dan * 8}')
    print(f'{dan} * 9 = {dan * 9}')

print('='*50)

for dan in range(2,10):
    print(f'----- {dan}단 -----')
    for num in range(1,10):
        print(f'{dan} * {num} = {dan * num}')

print('=' * 50)
# ----------------------------------------------------------
# 숫자 문자열의 합계 구하는 프로그램
# ----------------------------------------------------------

money='123,456,789'
total=0
for m in money:
    print(m, type(m))                   # 쪼개기
    if m==',': continue                 # ',' 걸러내기
    total=total+int(m)
    print(m, total)

print('=' * 50)
# ----------------------------------------------------------
# 문자열에 대한 코드값 출력하는 프로그램
# 문자 ----> 코드    문자의 코드값 알려주는 내장함수 ==> ord(문자 1개)
# 코드 ----> 문자    코드값을 주면 문자를 알려주는 내장함수 ==> chr(숫자)
# bin => binary 2진수로 변환
# ----------------------------------------------------------
msg='2022 Happy New Year~!'
codeMsg=''
for m in msg:
    print(m, ord(m), bin(ord(m)), hex(ord(m)))
    codeMsg = codeMsg + bin(ord(m))
print(codeMsg)






