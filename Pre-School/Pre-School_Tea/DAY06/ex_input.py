# ------------------------------------------
# 키보드로 입력받기 함수 => input("입력 받고 싶은 메시지")
# 키보드로 입력 후 엔터키(Enter) 입력하면
# 컴퓨터로 전달됨
# 변수에 입력받은 데이터 저장
# ------------------------------------------
#age=input("나이를 입력하세요.")
#print(f'당신은 {age}살이군요. type : {type(age)}')

nums=input("숫자 2개 입력하세요.(예:10,2) ")
print(f'nums => {nums}, type : {type(nums)}')

# 입력받은 문자열 덩어리 분리 =>  split(구분문자)
nums=nums.split(',')
print(f'nums => {nums}, type : {type(nums)}')

nums[0]=int(nums[0])
nums[1]=int(nums[1])
print(f'nums => {nums}, type : {type(nums)}')