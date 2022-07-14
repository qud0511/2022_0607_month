# ------------------------------------------------------
# 리트스 자료형 전용의 함수를 메서드(method)
# => 리스트 변수명.메서드()
# ------------------------------------------------------
# 점수 5개를 하나의 변수명으로 저장하기 => 리스트
jumsu=[98, 89, 70, 100, 56]

print(type(jumsu))

# 현재 리스트에 데이터 추가하는 메서드 => 2가지
# (1) 리스트의 제일 뒤에 추가하는 메서드 => append(데이터)
jumsu.append(99)
jumsu.append(91)
print(jumsu, len(jumsu))
jumsu.append(100)
print(jumsu, len(jumsu))

# (2) 리스트의 특정위치에 데이터 삽입 => insert(인덱스, 데이터)
jumsu.insert(0, 5)
print(jumsu, len(jumsu))

jumsu.insert(6, 15)
print(jumsu, len(jumsu))

# 리스트의 요소 정렬하기(sort) ------------------------------
# 요소 값을 순서대로 나열
# 기준 : 오름차순(작 => 큰, 1,2,3,.... )  : 기본
#       내림차순(큰 => 작, 10,9,8,..... )
# --------------------------------------------------------
jumsu.sort()
print("정렬후 : ", jumsu)

jumsu.sort(reverse=True)
print("정렬후 : ", jumsu)

grade=['Z','a','f','c','B']
print(grade, ord('A'), ord('a'))
grade.sort()
print("정렬후 : ", grade)

grade.sort(reverse=True)
print("정렬후 : ", grade)

# 현재 데이터를 역순으로 뒤집기 메서드 => reverse()
# 요소 값 비교 하는 정렬 X
jumsu=[91, 5, 28, 99, 34, 100]
print('전 : ', jumsu)
jumsu.reverse()
print('후 : ', jumsu)

# 요소값의 인덱스 찾아주는 메서드 => index(값)
# 해당 값이 존재하지 않으면 오류 발생 시킴
print(jumsu.index(5), jumsu.index(91))

# 요소값을 제거하는 메서드 => remove(값)
print(jumsu.remove(5), jumsu)

jumsu.append(5)
jumsu.append(5)
jumsu.insert(1, 5)
print(jumsu)
#print(jumsu.remove(15), jumsu)
#jumsu.clear()
print(jumsu)

# 현재 리스트 확장하는 메서드 => extend(리스트)
jumsu.extend(['a','b','c'])
print(jumsu)

# 리스트 + 리스트
a=[1,2,3]
b=['a','b']
a+=b  # a=a+b
print(a)

a=[1,2,3]
a*=3  #a=a*3
print(a)