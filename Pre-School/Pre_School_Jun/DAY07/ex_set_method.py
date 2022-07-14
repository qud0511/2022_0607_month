# -----------------------------------------------------------
# 집합 자료형(set) 전용의 함수 => 메서드
# -----------------------------------------------------------
datas=set()
# 비어 있는 set 객체에 데이터 넣기 => add(데이터)
datas.add(10)
datas.add(4)
datas.add(4)
print(f'datas 갯수 : {len(datas)} 데이터 : {datas}')

# 여러개 데이터 한꺼번에 넣기 => update(여러개 데이터)
# set 자료형은 중복되는 건 모두 삭제함.
datas.update([10,1,5,2,4,8,4])
print(f'datas 갯수 : {len(datas)} 데이터 : {datas}')
datas.update('Good')
print(f'datas 갯수 : {len(datas)} 데이터 : {datas}')


# 요소 제거하는 메서드 => remove(요소데이터)
datas.remove('d')
datas.remove(10)
print(f'datas 갯수 : {len(datas)} 데이터 : {datas}')








