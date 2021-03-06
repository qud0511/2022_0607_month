# ------------------------------------------------------------------------
# 리스트와 요소
# 요소란? 리스트 안에 들어있는 데이터
# 읽기 방법 : 변수명[인덱스]
# 저장 방법 : 변수명[인덱스]=값
# 삭제 방법 : del( 변수명[인덱스] )
#           del  변수명[인덱스]
# ------------------------------------------------------------------------
nums=[1, 7, 9, 'A', True, 30.23, "Good"]
print(nums)

print('요소 읽기 :', nums[3])

# 특정 요소 안에 데이터 넣기, 변경하기
nums[3]=21
print(nums)

nums[4]=1
print(nums)

nums[-1]=[1,2,3,4]
print(nums)

# 요소 삭제하기
del(nums[-1])
print(nums)

# 지정된 범위에 요소 값 변경하기(슬라이싱 활용)
# 1번 요소부터 3번요소까지 다른 값 넣기
nums[1:4]=[11,22,33]
# 슬라이싱을 사용하지 않을 경우 일일히 입력해야함. nums[1]=11, nums[2]=22, nums=[3]
print(nums)

nums[1:4]=[111,222,333,444,555,666,777,888]
print(nums)
# 더 많이 입력 가능

nums[1:4]=['a','b']
print(nums)
# 더 적게 입력 가능

nums[1:4]=[]
print(nums)
# 아무것도 넣지 않는 것도 가능함. 기존의 값이 사라짐. del과 같은 결과.

nums[:]=[]
print(nums)
# 요소 전부 지우기






