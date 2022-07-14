# ------------------------------------------------------
# 튜플(Tuple) - Read Only List
# - 여러개의 데이터를 저장하는 타입
# - 수정,삭제 안됨.
# - 오직 저장된 요소 읽기만 가능
# - 형태 : (값1, 값2,..., 값n)  또는 값1, 값2,..., 값n
# - 요소 : 인덱스 읽기
# -----------------------------------------------------
data=('F', 123, 9.023, True)

print(type(data), data, len(data))
print(data[0], data[-1], data[1:-1])

# 튜플 타입은 값 변경, 요소 삭제 불가 ---
#data[0]='M'
#del data[0]

# 꼭 변경해야하는 경우  ==> list 형변환
data=list(data)
data[0]='여자'

data=tuple(data)
print(data)

print(data.count(True))
print(data.index(True))

#-------------------------------------------------
mydata=('110101-1234567',)
print(mydata, type(mydata))

mydata2=10,
print(mydata2, type(mydata2))