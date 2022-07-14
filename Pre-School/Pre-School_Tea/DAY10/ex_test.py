# --------------------------------------------------------
# 1. 2개 문자를 입력받아서 하나의 문자열로 반환하는 함수
#    입력 -> Good, Luck   출력 -> Good Luck
# 함 수 명 : joinStrs
# 파라미터 : str1  str2
# 반 환 값: 합쳐진 문자열
# --------------------------------------------------------
def joinStrs(str1, str2):
    return str1+" "+str2

# 함수 사용하기 -----------------
datas=input("문자열 2개 입력 : (예: A,B)")

# 데이터 전처리
datas=datas.split(',')    # ["A", "B"] <----- "A,B"
print(datas)

# datas[0]=datas[0].strip()
# datas[1]=datas[1].strip()
datas=[d.strip() for d in datas]
print(datas)

# - 함수 호출
print(joinStrs(datas[0], datas[1]))

# 입력된 데이터 공백 제거 => strip, lstrip, rstrip



# --------------------------------------------------------
# 2. 숫자 데이터 리스트를 입력 받아서
#     평균을 반환하는 함수
#     nums=[1,9,23,81,4]
#     출력 => 평균 XX.XXX
# 함 수 명 : getAverage
# 파라미터 : nums
# 반 환 값 : 평균값
# --------------------------------------------------------
def getAverage(nums):
    count=len(nums)
    total=0
    for num in nums: total = total+num
    return total/count if count>0 else "데이터가 없습니다."

datas=[1,9,23,81,4]

print(f'{datas} 평균 : {getAverage(datas)}')


# --------------------------------------------------------
# 3. 입력받은 정수의 code값을 16진수로 반환하는 함수
#     단, 입력되는 정수의 갯수는 유동적  --> 가변인자
#     입력 => 2, 3      출력 => 0x32,   0x33
#     입력 => 2         출력 => 0x32
#     입력 => 0         출력 =>
# 함 수 명 : getCode
# 파라미터 : *num
# 반 환 값 : 16진수
# --------------------------------------------------------
def getCode(*num):
    strMsg=''
    for n in num:
        # 문자 -> 코드값 반환 내장함수 ord(문자1개)
        code = ord(str(n))
        strMsg = strMsg + hex(code)+', '
    return strMsg[:-2]

# 함수 사용
print(f'3의 코드값 : {getCode(3,5,7)}')