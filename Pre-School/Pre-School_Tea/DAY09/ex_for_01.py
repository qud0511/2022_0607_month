# -- tuple 데이터로 구성된 List =========================
a=[(1,11), (2,22), (3,33)]
print('-----')
for i in a: print(i, i[0] + i[1])

print('-----')
for (f, s) in a: print(f+s)

print('-----')
for f, s in a: print(f+s)

# -- list 데이터로 구성된 List =========================
a=[[1,11], [2,22], [3,33]]
print('-- LIST 원소---')
for i in a: print(i, i[0] + i[1])

print('-----')
for [f, s] in a: print(f+s)

print('-----')
for f, s in a: print(f+s)


# 학생 점수 출력 ------------------------------------
jumsus=[87, 67, 87, 100, 42, 91]
no=1
for jumsu in jumsus:
    print('%d번째 학생 점수 : %d' %(no, jumsu))
    print('{}번째 학생 점수 : {}'.format(no, jumsu))
    print(f'{no}번째 학생 점수 : {jumsu}')
    no = no +1

# 요소와 인덱스를 함께 제공하는 내장함수 => enumerate()
print('-------enumerate() ')
for idx, jumsu in enumerate(jumsus):
    print('%d번째 학생 점수 : %d' % (idx+1, jumsu))
