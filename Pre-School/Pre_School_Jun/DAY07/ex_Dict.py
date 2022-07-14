# --------------------------------------------------------------------------------------------
# Dictionary 자료형 -> dict 자료형
# key와 Value를 쌍으로 구성
# key를 통해서 Value을 얻는 방식
# 연관 배열 또는 해시(Hash)
# 중괄호 {}로 묶고 key:value를 콤마(,)로 구분
# 순서가 의미 없음.
# 주의! key 중복, 중복시 하나의 키를 제외하고 나머지 무시함.
# 인덱스가 필요하지 않음.
# 변수명={'key1':'value1', 'key2':'value2', 'key3':'value3'}

# 딕셔너리 자료형(dict)
# 값의 의미를 함께 저장하는 방식
# 형식 : { 키1:값, 키2:값,...., 키n:값}
# 요소 읽는 방법 : 키로 값을 읽어옴.
# 요소 삭제하는 방법 : 키로 값으루 삭제함.
# 요소 값 변경 : 키로 접근이서 값을 변경
# --------------------------------------------------------------------------------------------

# dict 자효형
dNums=[]
print(f'dNums => 타입')

dNums={}
dNums1={1:100, 2:200, 3: 300}
dNums2={1:100, '2':200, 3: 300, 1:555}
dNums3={('홍길동', '대구'):100, '2':200, 3:300, ('홍길동', '부산'):555}

print(f'dNums => 타입 : {type(dNums)}, 갯수 {len(dNums)}, 데이터{dNums}')
print(f'dNums1 => 타입 : {type(dNums1)}, 갯수 {len(dNums1)}, 데이터{dNums1}')
print(f'dNums2 => 타입 : {type(dNums2)}, 갯수 {len(dNums2)}, 데이터{dNums2}')
print(f'dNums3 => 타입 : {type(dNums3)}, 갯수 {len(dNums3)}, 데이터{dNums3}')

# 키는 중복될 수 없고, 변경되어도 안된다.
print('\n')
# --------------------------------------------------------------------------------------------

# dict 자료형의 요소 읽기
# 인덱싱 없음 => 키(key)로 요소 읽기 ==> [key]
print(f'dNums1[1]=>{dNums1[1]}')
print(f'dNums2["2"]=>{dNums2["2"]}')
print(f'dNums3[("홍길동", "대구")]=>{dNums3[("홍길동", "대구")]}')
print(f'dNums3[("홍길동", "부산")]=>{dNums3[("홍길동", "부산")]}')

# dict 자료형의 요소 값 변경, 즉 새로 넣기 => [key]=새로운 값
dNums3[("홍길동", "부산")] = "053"
dNums3[3]='054'
print(f'dNums3 => 타입 : {type(dNums3)}, 갯수 {len(dNums3)}, 데이터{dNums3}')

print('\n')
# del 변수명[key] 또는 del(변수명[key])
del dNums3[3]
del(dNums3['2'])
print(f'dNums3 => 타입 : {type(dNums3)}, 갯수 {len(dNums3)}, 데이터{dNums3}')

# dict에 요소 추가하기 => 변수명[key] = 값
dNums3[1225]="메리"
print(f'dNums3 => 타입 : {type(dNums3)}, 갯수 {len(dNums3)}, 데이터{dNums3}')

dNums3[1225]="Christmas"
print(f'dNums3 => 타입 : {type(dNums3)}, 갯수 {len(dNums3)}, 데이터{dNums3}')

# 멤버연산자?
print('123' in dNums3, ('홍길동', '부산') in dNums3)
print('a' in 'abc', 'A' in 'abc')
print('a' in ('a','b',2), 'a' in [1,2])

















