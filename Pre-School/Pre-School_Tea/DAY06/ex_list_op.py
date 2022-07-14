# -----------------------------------------
# 연산(계산) -> 2가지 연산 즉 계산 가능
#           -> 덧셈 : 리스트 + 리스트
#           -> 곱셈 : 리스트 * 숫자
# ----------------------------------------
# 정수 7개 저장하는 변수
nums=[10, 20, 30, 40, 50, 60, 70]
data=['a','b','c']

numdata=nums+data
print(numdata, len(numdata))

numfive=nums*5
print(numfive, len(numfive))

#----------------------------------------
a=[1,2,3]
print(a, type(a), a[1], type(a[1]))

print(str(a[1])+"HI")
print(a[1]+int("100"))