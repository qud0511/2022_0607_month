# -------------------------------------------------------------------------
# 반복문 while 조건식
# -------------------------------------------------------------------------
print('================ up-counting =================')

count=0

while count<10:
    print(count)    # print(a) 입력하면 무한반복?
    count=count+1


print('============== down-counting ================')

while count>0:
    print(count)
    count=count-1

print('='*40)
# -------------------------------------------------------------------------
# 리스트 데이터의 요소를 모두 출력
# -------------------------------------------------------------------------
# 1 ~ 50 범위에서 3의 배수로 구성된 데이터
nums=range(3,51,3)

# print(nums[0],nums[1],nums[2]) 일일이 입력하기 어려움.

idx=0
total=len(nums)
while idx<total:
    print(nums[idx])
    idx=idx+1

print('\n')

for num in nums:
    print(num)

print('='*40)

# tuple 데이터로 구성된 list
a=[[1,11],[2,22],[3,33]]
# a의 0번 요소의 타입은 tuple, 0번 요소의 0번은 int
print('----LIST 원소----')
for i in a: print(i, i[0] + i[1])

for (f,s) in a: print(f+s)

for f,s in a: print(f+s)      # unpacking

for [f, s] in a: print(f+s)

print('='*40)

# 학생 점수 출력
jumsus=[87,67,87,100,42,91]
no=1
for jumsu in jumsus:
    print('%d번째 학생 점수 : %d' %(no,jumsu))
    print('{}번째 학생 점수 : {}'.format(no,jumsu))            # 3가지 출력방법
    print(f'{no}번째 학생 점수 : {jumsu}')
    no=no+1

print('\n')
# 요소와 인덱스를 함께 제공하는 내장함수 ==> enumerate() 나열하다
print('===== enumerate =====')
for idx, jumsu in enumerate(jumsus):
    print('%d번째 학생 점수 : %d' %(idx,jumsu))
