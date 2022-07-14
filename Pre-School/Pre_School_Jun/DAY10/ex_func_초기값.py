# ----------------------------------------------------------------------
def getAdd(num1=0, num2=0):
    return num1+num2

print(getAdd(1,54))
print(getAdd(1))
print(getAdd())

# 가변인자와 일반 변수를 함께 사용할 때는
# def getValue(*nums, data):
#    print(nums, data)
# getValue(1,3,4)
# 오류 남.
# (1) 일반 변수 (2) 가변 인자

def getValue(data,*nums,age=12):
    print(nums, age, data)
getValue(1,3,4, age=100)
# (1) 일반 변수, (2) 가변 인자 (3) 디폴트 변수(초기값)
# ----------------------------------------------------------------------



