# ------------------------------------------------------------------------------------
# input, 교재 168쪽
# 키보드로 입력받기 함수 ==> input("입력받고 싶은 메시지")
# 키보드로 입력 후 엔터키(Enter) 입력하면 컴퓨터로 전달됨.
# 변수에 입력받은 데이터를 저장해야함. 사라지니까
#-------------------------------------------------------------------------------------
# age=input("나이를 입력하세요.")
# print(f'당신은 {age}살이군요. type : {type(age)}')

nums=input("숫자 2개 입력하세요")
print(f'nums => {nums}, type : {type(nums)}')

# 입력받은 문자열 덩어리 분리하기 ==> split(구분문자)
nums=nums.split()
print(f'nums => {nums}, type : {type(nums)}')

nums[0]=int(nums[0])
nums[1]=int(nums[1])
print(f'nums => {nums}, type : {type(nums)}')
# ?? 기본적으로 str 타입으로 나옴. 그래서 숫자로 형변환할 수도 있음.



