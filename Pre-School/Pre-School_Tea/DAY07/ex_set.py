# ---------------------------------------------
# 집합 자료형(set)
# - 중복 데이터 제거 후 저장
# - 인덱스 X, 키 X, 순서 X
# - 생성 : set()   {1,54,2}
# --------------------------------------------

# 집합 자료형 생성 -----------------------------
sData1={1,2,4}
sData2=set()
sData3=set([1,1,4,7,3,2,7])
sData4=set("Good Happy")
sData5=set((1,))

print(f'sData1 타입 : {type(sData1)}  갯수 : {len(sData1)}  데이터 : {sData1}')
print(f'sData2 타입 : {type(sData2)}  갯수 : {len(sData2)}  데이터 : {sData2}')
print(f'sData3 타입 : {type(sData3)}  갯수 : {len(sData3)}  데이터 : {sData3}')
print(f'sData4 타입 : {type(sData4)}  갯수 : {len(sData4)}  데이터 : {sData4}')