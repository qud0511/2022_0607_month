# DAY06 내용 확인
# 1) 데이터를 입력받아서 하나의 변수에 저장
#    5개의 데이터를 입력
#    5개의 데이터는 하나의 변수명에 저장
# -> List : 수정, 삭제, 추가
# -> Tuple : 수정 X, 삭제 X, 변경 X, 추가 X, 읽기만 가능 -> 바꾸고 싶으면 list로 바꿔야함.

# 5개의 데이터를 저장할 수 있는 빈 저장소
# datas=( )  # 비어있는 튜플
datas=[ ]  # 비어있는 리스트

# 키보드로 입력받기 -> input("요청메시지")
data=input("저장하고 싶은 데이터 입력 : ")
datas.append(data)     # 입력받은 데이터 저장하기

data=input("저장하고 싶은 데이터 입력 : ")
datas.insert(0, data)

data=input("저장하고 싶은 데이터 입력 : ")
datas.append(data)

data=input("저장하고 싶은 데이터 입력 : ")
datas.insert(0, data)

data=input("저장하고 싶은 데이터 입력 : ")
datas.append(data)


# 리스트에 저장된 모든 데이터 출력하기
print('-'*25)
print(f'갯수 : {len(datas)}, 데이터 : {datas}')
print('-'*25)

# input으로 출력한 것은 str타입으로 나옴.






















