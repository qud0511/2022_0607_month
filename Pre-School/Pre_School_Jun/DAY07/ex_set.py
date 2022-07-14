# ----------------------------------------------------
# 집합 자료형(set)
# 중복 데이터 제거 후 저장
# 인덱스 X, 키 X, 순서 X
# 생성 : set()      {1,54,2}
# set 자료형은 가장 늦게 만들어져서 비어있는 set을 set()로 표현함.
# ----------------------------------------------------

# 집합 자료형 생성
sData1={1,2,4}
sData2=set()
sData3=set([1,1,4,7,3,2,7,7])
sData4=set('  Good happy  ')
# sData5=set(1) ==>  set은 여러개의 데이터를 저장하는 타입이기 때문에 하나만 저장하면 오류 발생함.
sData6=set([1]) # 리스트 형은 가능, 단순히 1이 아니라 1이 빠져도 []가 남아서?
sData7=set((1,))  # 튜플 형도 가능

print(f' sData1 타입 : {type(sData1)}  갯수 : {len(sData1)}  데이터 : {sData1} ')
print(f' sData2 타입 : {type(sData2)}  갯수 : {len(sData2)}  데이터 : {sData2} ')
print(f' sData3 타입 : {type(sData3)}  갯수 : {len(sData3)}  데이터 : {sData3} ')
print(f' sData4 타입 : {type(sData4)}  갯수 : {len(sData4)}  데이터 : {sData4} ')
print(f' sData6 타입 : {type(sData6)}  갯수 : {len(sData6)}  데이터 : {sData6} ')
print(f' sData7 타입 : {type(sData7)}  갯수 : {len(sData7)}  데이터 : {sData7} ')



