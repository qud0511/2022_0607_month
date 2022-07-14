#---------------------------------------------------------------------------------------------
# 딕셔너리 자료형(dict) 전용 함수 ==> 메서드(method) 실습하기
#---------------------------------------------------------------------------------------------
# 사람 정보 => 이름, 나이, 성별, 전화번호, 주소
personInfo={'name':'박병준'}

personInfo['age']=26
personInfo['gender']='M'
personInfo['phone_num']='010-5241-0476'
personInfo['addr']='Daegu'

print(f' personInfo 타입 : {type(personInfo)}\n데이터 : {personInfo}\n갯수: {len(personInfo)}')

print('\n')

# dict 데이터에서 키(key)만 가져오는 메서드 => 변수명.keys()
mykeys=personInfo.keys()
print(f' mykeys => {mykeys}')

# dict 데이터에서 값(value)만 가져오는 메서드 => 변수명.value()
myValues=personInfo.values()
print(f' myValues => {myValues}')

# dict 데아터에서 키와 값을 튜플로 묶어서 가져오는 메서드 => 변수명.items()
myItems=personInfo.items()
print(f' myItems => {myItems}')

# 파이선 3.0 버전부터는 메모리 낭비 문제로 리스트로 주는 것이 아니라 객체로 준다.
# 리스트를 사용하는 것과 차이가 없지만, 리스트 고유의 append, insert, pop, remove, sort 함수는 수행할 수 없다.
# 그래도 사용하고 싶다면 리스트로 형변환해야한다.

# 읽기방법 (1) for ~ in
print(f' mykeys : {type(mykeys)}') # dict_keys 타입이라고 나옴.
for key in mykeys:
    print(key)

# 읽기방법 (2) list(데이터)   형변환
myValues=list(myValues)
print(myValues)



# dict 데이테에서 key로 value를 가져오는 메서드 => 변수명.get(키)
print(personInfo.get('name'), personInfo['name'])
print(personInfo.get('email')) # print(personInfo['email'])
# 해당 키가 dict 데이터 안에 없으면 값이 없다(None) 결과로 돌려줌. 대괄호로 사용했을 때는 오류 발생.

print(personInfo.get('email', '이메일 없음'))
print(personInfo.get('email', '0'))
print(personInfo.get('email', '-1'))

# pop은 가져오면서 값을 꺼내옴. 기존의 딕셔너리에는 삭제됨.
print(personInfo.pop('name'))

# 여러개의 데이터를 dict에 추가하는 메서드 => update(dict 타입)
personInfo.update({1:100, 2:200, 3:300})
print(personInfo, '\n', len(personInfo))

# 모든 데이터 삭제하는 메서드 => clear
personInfo.clear()
print(personInfo, '\n', len(personInfo))


