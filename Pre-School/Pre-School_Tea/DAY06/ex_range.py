# -----------------------------------------------------------------
# 수의 범위 즉 어디서부터 어디까지 ( ~ ) 라는 범위를 설정하는 함수
# range(시작숫자, 끝숫자+1, 간격)
# -----------------------------------------------------------------
# 1~ 100까지 정수로 구성된 리스트를 생성하기
#nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,...,99, 100]
nums=range(1,101)
print(nums, type(nums), nums[0], nums[-1])

# 0 ~ 10
nums=list(range(11))
print(nums, type(nums), nums[0], nums[-1])

# 1 ~ 10
nums=list(range(1, 11))
print(nums, type(nums), nums[0], nums[-1])

# 1~10범위에서 2의 배수 만  --> 2,4,6,8,10
nums=list(range(2, 11, 2))
print(nums, type(nums), nums[0], nums[-1])

# 1~50범위에서 7의 배수 만  --> 7,14,21,28,35,....
nums=list(range(7, 51, 7))
print(nums, type(nums), nums[0], nums[-1])
