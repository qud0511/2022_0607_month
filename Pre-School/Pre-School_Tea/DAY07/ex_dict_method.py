# -----------------------------------------------------------
# 딕셔너리 자료형 (dict) 전용 함수 => 메서드(Method) 실습하기
# -----------------------------------------------------------
# 사람 정보 => 이름, 나이, 성별, 전화번호, 주소
personInfo={"name":"마징가"}

personInfo["age"]=250
personInfo["gender"]="M"
personInfo["phone"]="010-2222-1111"
personInfo["addr"]="Daegu"

print(f'personInfo 타입 : {type(personInfo)}\n데이터 : {personInfo}\n갯수: {len(personInfo)}')


# dict 데이터에서 키(key)만 가져오는 메서드 => 변수명.keys()
myKeys=personInfo.keys()
print(f'myKeys => {myKeys}, type : {type(myKeys)}')
#print(myKeys[0], myKeys[-1])
for key in myKeys:
    print(key)

# dict 데이터에서 값(value)만 가져오는 메서드 => 변수명.values()
myValues=personInfo.values()
print(f'myValues => {myValues}')
# 읽기 방법 (1) for ~ in
for v in myValues:
    print(v)

# 읽기 방법 (2) list( 데이터 ) 형변환
myValues=list(myValues)

# dict 데이터에서 키와 값을 튜플로 묶을로 가져오는 메서드 => 변수명.items()
myItems=personInfo.items()
print(f'myItems => {myItems}')
for item in myItems:
    print(item)


# dict 데이터에서 key로 value를 가져오는 메서드 => 변수명.get(키)
# 해당 키가 dict 데이터안에 없으면 값이 없다 None 결과로 돌려줌
print( personInfo.get("name") , personInfo["name"] )
print( personInfo.get("email") )  #, personInfo["email"] )
print( personInfo.get("email", -1) )

# 여러개의 데이터를 dict에 추가하는 메서드 => update( dict 타입 )
personInfo.update({1:100, 2:200, 3:300})
print(personInfo, '\n', len(personInfo))

print(personInfo.pop(1))
print(personInfo, '\n', len(personInfo))

personInfo.clear()
print(personInfo, '\n', len(personInfo))

