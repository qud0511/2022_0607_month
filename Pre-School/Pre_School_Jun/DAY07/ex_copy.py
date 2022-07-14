# ------------------------------------------------------------------------------------
# 변수 복사 실습
# ------------------------------------------------------------------------------------
a=[1,2,3,[11,22]]
b=a

print(f'a의 id : {id(a)}\nb의 id : {id(b)}')

a[0]='A'
print(a, b)
print(a is b)

# -----------------
print(10 is 10.0)
# is는 타입을 봄. 10 is 10.0은 각각 int, float 타입이라 False
print(10 == 10.0)  # True라고 나옴.
# -----------------

# 복사하는 방법 (1) 슬라이싱을 이용
# 주소가 다름. 즉, 각각 수정해야함.
c=a[:]
print(f'a의 id : {id(a)}\nb의 id : {id(b)}\nc의 id : {id(c)}')
print(f'a is c => {a is c}')    # False 나옴.

a[3][0]=2022
print(a,b,c)  # 깊은 복사가 아닐 경우 모든 변수에 값이 변경되버림.
print(f'a is b => {a is b}')
print(f'a is c => {a is c}')
# 슬라이싱을 이용한 복사를 얕은 복사라고 함. 처음만 복사해줘서, 뒤에 리스트 추가한 것까지 딸려옴.



# 깊은 복사 기능을 가진 모듈을 추가
# 메모리 문제로 기본 기능 X, 기능을 파이썬에서 불러와야함.
# import
import copy
d=copy.deepcopy(a)
print(f'a is d => {a is d}')
print(f'a의 id : {id(a)}\nb의 id : {id(b)}\nc의 id : {id(c)}\nd의 id : {id(d)}')
print(a,b,c,d)


















