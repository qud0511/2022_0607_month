# exception handling 예외처리
# 프로그램 실행 시 발행하는 오류error에 대한 처리
# 오류가 발생해도 프로그램 중단 되지 않기 위해
# ---------------------

try:
    num1, num2 = 10, 0

    print(f'{num1/num2} = {num1/num2}') # 에러 발생

    print('ENDING') # 위 에러 때문에 실행 안됨.

except Exception as ex:         # Exception 가장 상위의 에러
    print('에러 발생', ex)

# except ZeroDivisionError as e:    # 하위의 에러가 밑에 가면 안됨.
#     print('0로 나눌 수 없음')

finally:
    print('Ending')

# ---------------------

# try:
#     => 예외발생가능 코드

# except 오류:
#     => 예외발생 처리코드

# else:
#     => 예외 발생하지 않은 경우

# finally:
#     => 오류 발생 상관없이 무조건 실행코드

# ---------------------

try:
    file=open('agaga.jpe', mode='r')
    print(file.read())
    file.close()

except Exception as e:
    print(f'에러 발생 => {e}')



import os
if os.path.exists('agaga.jpg'):
    file=open('agaga.jpe', mode='r')
    print(file.read())
    file.close()

else:
    print('없는 파일입니다.')

# ---------------------
# ---------------------

# PPT 31
# 프로그램 기능 구현상 강제로 예외 벌생시키기
# =>    rasie 에러이름
# ex) 웹페이지 로그인 5번 이상 틀렸을 때 강제 오류

num=int(input('3의 배수 입력 =>'))

if num %3 != 0:
    print(f'{num}은 3의 배수가 아닙니다.')
# -----
num=int(input('3의 배수 입력 =>'))

if num %3 != 0:
    raise Exception('3의 배수 오류')

# except Exception:
print('ERROR 발생')

# -------------

class Bird:
    def fly(self):
        raise NotImplemented  # 아들아 반드시 고쳐줘라

class Eagle(Bird):
    def fly(self):
        print('DFDFDFDFDFDF')

# e=Eagle
# e.fly()



