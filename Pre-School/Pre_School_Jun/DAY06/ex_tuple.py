# ------------------------------------------------------------------
# tuple 자료형 ==> 읽기 전용 리스트 lead only list
# 여러개의 데이터를 저장하는 타입
# 수정, 삭제 불가
# 오직 저장된 요소 읽기만 가능
# 소괄호() 사용하고 쉼표(,)로 구분
# 소괄호() 생략 가능
# 하나라도 쉼표(,) 사용해야함.
# 형태 : (값1, 값2, 값3, ..., 값n)
# 요소는 인덱스로 읽기
# ------------------------------------------------------------------
data=('F', 123, 9.823, True)
print(type(data), data, len(data))
print(data[0], data[-1], data[1:-1])

# tuple type은 값 변경, 요소 삭제 불가능... 하지만
# 꼭 변경해야하는 경우 ===> 리스트 형변환, 즉 list type casting
data=list(data)
data[0]='여자'
print(data)

# 다시 변경 못하도록 튜플로 변환
data=tuple(data)
print(data)

# tuple은 메서드가 2가지밖에 없음. count와 index
print(data.count(True))
print(data.index(True))

# 하나만 있을 때
mydata=('970311-1111111')
print(mydata, type(mydata)) # 타입이 str, int, float로 나옴.

mydata=mydata=('970311-1111111',) # 쉼표를 찍어야 tuple로 취급됨.
print(mydata, type(mydata))

# tuple 덧셈, 곱셈, 뺄셈 가능