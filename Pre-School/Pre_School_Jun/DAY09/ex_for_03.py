# -------------------------------------------------------------------------
# 리스트 컨프리헨션(List Comprehension)
# list 안에 for 문이 포함되어 있는 구문
# 조건부표현식 포함되는 구문
# -------------------------------------------------------------------------
nums=[1,2,3,4,5]

# (1) nums 데이터 요소들에 3을 곱한 값을 저장하는 리스트 생성
nums2=[]
for num in nums:
    nums2.append(num*3)

# ==> list comprehension방식
nums22=[ num*3 for num in nums]

# (2) nums 데이터 중에서 2의 배수만 3을 곱해서 새로운 리스트 생성하기


# ==> list comprehension방식
nums22=[ num*3 for num in nums if num%2 == 0 ]

# (3) nums 데이터 중에서 2의 배수는 3을 곱하고 나머지는 원래 값 그대로 리스트에 담아서 생성하기


