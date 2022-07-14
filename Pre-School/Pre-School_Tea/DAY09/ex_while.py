# --------------------------------------------
# 반복문 while 조건식:
# --------------------------------------------
count=0

print('---- UP COUNTING ----')
while count<10:
    print(count)
    count=count+1

print('---------------------')

print('---- DOWN COUNTING ----')
while count>0:
    print(count)
    count=count-1
print('---------------------')

#----------------------------------------------
# 리스트 데이터의 요소를 모두 출력
# ---------------------------------------------
# 1 ~ 50 범위에서 3의 배수로 구성된 데이터
nums=range(3, 51,3)

idx=0
total=len(nums)
while idx<total:
    print(nums[idx])
    idx=idx+1

for num in nums:
    print(num)





