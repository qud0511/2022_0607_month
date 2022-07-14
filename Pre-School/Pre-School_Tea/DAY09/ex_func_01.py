# ---------------------------------------------------
# 사용자 정의 함수
# ---------------------------------------------------
#---------------------------------------------------
# 목적/기능 : 2개 정수 덧셈 후 결과 반환
# 함 수 명 : addTow
# 파라미터 : num1  num2
# 결 과 물 : 덧셈값
# --------------------------------------------------
def addTwo(num1, num2):
    value=num1+num2
    return value

def addThree(num1, num2, num3):
    value=num1+num2+num3
    return value

def addfive(num1, num2, num3, num4, num5):
    value=num1+num2+num3+num4+num5
    return value

#---------------------------------------------------
# 목적/기능 : 0개 ~ N개 정수 덧셈 후 결과 반환
# 함 수 명 : addNum
# 파라미터 :  *nums   <== 가변인자
# 결 과 물 : 덧셈값
# --------------------------------------------------
def addNum(*nums):
    value=0
    for num in nums:
        value = value+num
    return value

addNum()
addNum(1,5,2,3,7,3)
addNum(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
addNum(1)
#---------------------------------------------------
# 목적/기능 : 2개 정수 뺄셈 후 결과 반환
# 함 수 명 : minusTwo
# 파라미터 :  num1  num2
# 결 과 물 : 뺄셈값
# --------------------------------------------------
def minusTow(num1, num2):
    value=num1-num2
    return value

#---------------------------------------------------
# 목적/기능 : 정수 리스트 데이터의 합계 반환
# 함 수 명 :  getTotalList
# 파라미터 :  nums
# 결 과 물 : 합계 값
# --------------------------------------------------
def getTotalList(nums):
    total=0
    for num in nums:
        total = total + num

    return total

# -----------------------------------------------------
# 함수 사용하기 => 함수 호출
# -----------------------------------------------------
print( addTwo(10, 3) )
print()
print( addTwo(3,2) )

datas=[5,2,8,1]
print(getTotalList(datas))
print(getTotalList([ 1,2,3,4,5,6,7,8,9,10] ))



