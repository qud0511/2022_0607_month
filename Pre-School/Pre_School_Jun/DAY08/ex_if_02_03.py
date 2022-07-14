# 문제2) 숫자를 입력 받아 양수 & 음수 구별하는 프로그램
runNumber=1
if runNumber == 1:
    num = input('숫자 입력 : ')
    num = int(num)

    # 양수 : 0보다 큰 수                   음수 : 0보다 작은 수
    if num > 0:
        print("양수")
        print('0보다 큰 수')
    else:
        print("음수")
        print('0보다 작은 수')
    print('== The End ==')


# 문제3) 숫자를 입력받아
# 조건 1 --- 0보다 큰  수
# 조건 2 --- 0보다 작은 수
# 조건 2개이상 되는 조건문 ==> 다중 조건문
# 형식 => if 조건1 :
#           실행코드
#        elif 조건2 :
#           실행코드
#        elif 조건3 :
#           실행코드
#        elif 조건4 :
#           실행코드
#        else:
#           실행코드
runNumber=3
if runNumber==3:
    num=input('숫자 입력 : ')         # num은 키보드로 입력 받아서 str 타입 => 예) '3'
    num=int(num)                    # str 타입 num ==> int 타입 num ----- 형변환

    if num>0:
        print(f'{num}은 양수')
    elif num<0:
        print(f'{num}은 음수')
    else:
        print(f'{num}은 0')
    print('== The End ==')
