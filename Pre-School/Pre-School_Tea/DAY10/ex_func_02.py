# -------------------------------------------------
# 함수 반환값 => return 결과
# ** return 키워드
# - 함수, 조건문, 반복문 함께 사용됨
# - 원래 있던 곳으로 다시 돌아가는 기능
# -------------------------------------------------
def getAdd(num1=5, num2=10):
    return num1+num2

def noData():
    print('noData입니다.')
    return

# ---------------------------------------------------
# 기    능 : 4칙 연산 수행 결과 반환하는 함수
# 함 수 명 : calcFour
# 파라미터 : num1, num2
# 반 환 값 : 덧셈결과, 뺄셈결과, 곱셈결과, 나눗셈결과
# ---------------------------------------------------
def calcFour(num1, num2):
    return num1+num2, num1-num2, num1*num2, num1/num2 if num2>0 else None

print(getAdd(1,2))
print(getAdd(1))
print(getAdd())
# print(noData())
# print('[4칙연산 결과 ]', calcFour(1,3))
# print('[4칙연산 결과 ]', calcFour(23,0))

def getValue(data,*nums,age=12):
    print(nums, age, data)

getValue(1,3,4, age=100)