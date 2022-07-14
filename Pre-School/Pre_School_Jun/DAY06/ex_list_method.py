# -----------------------------------------------------------------------
# list 자료형 전용의 함수인 method
# list 변수명.메서드()
# -----------------------------------------------------------------------
# 점수 5개를 하나의 변수명으로 저장하기 ==> 리스트
jumsu=[90, 89, 70, 100, 56]
print(type(jumsu))

# 현재 리스트에 데이터 추가하는 메서드 2가지
# (1) 리스트의 제일 뒤에 추가하는 메서드 ==> append(데이터)
# 변수명.append(데이터)
jumsu.append(99)
print(jumsu, len(jumsu))

jumsu.append(93)
print(jumsu, len(jumsu))

# (2) 리스트이 특정위치에 데이터 삽입 ==> 변수명.insert(인덱스, 데이터)
jumsu.insert(0, 5)
print(jumsu, len(jumsu))

jumsu.insert(3, 33)
print(jumsu, len(jumsu))

print('\n')
# -----------------------------------------------------------------------

# 리스트의 요소 정렬하기(sort)
# 변수명.sort()
# 요소 값을 순서대로 나열
# 기준 : 오름차순(작 => 큰, 12345..) : 기본값
#       내림차순(큰 => 작, 98765..)

# 오름차순
jumsu.sort()
print('오름차순 정렬 후 : ', jumsu)

# 내림차순
jumsu.sort(reverse=True)
print('내림차순 정렬 후 : ', jumsu)


grade=['z','a','f','c','b']
grade.sort()
print('문자 오름차순 정렬 후 : ', grade)

grade=['z','a','f','c','b','Z','V','B','A']
print(grade, ord('A'), ord('a'))
grade.sort()
print('대소문자 오름차순 정렬 후 : ', grade)

grade.sort(reverse=True)
print('대소문자 내림차순 정렬 후 : ', grade)

# 현재 데이터를 역순으로 뒤집기 메서드 ==> 변수명.reverse()
# 요소 값을 비교한 정렬 X, 단순히 순서만 뒤집음.
jumsu=[91, 5, 28, 99, 34, 100]
print('전 : ', jumsu)
jumsu.reverse()
print('후 : ', jumsu)

# 요소값의 인덱스 찾아주는 메서드 => 변수명.index(값)
print(jumsu.index(5), jumsu.index(91))
# 리스트에서의 인덱스는 해당 값이 존재하지 않으면 오류 발생 시킴.
# print(jumsu.index(5), jumsu.index(91), index(88888))

# 요소 값을 제거하는 메서드 ==> 변수명.remove(값)
print(jumsu.remove(5), jumsu)

jumsu.append(5)
jumsu.append(5)
jumsu.insert(1,5)
print(jumsu)
print(jumsu.remove(5), jumsu)
# 하나만 지워짐.

# jumsu.clear()
# 다 지우기.

# 리스트 요소 끄집어내기 ==> 변수명.pop()
# 맨 마지막 요소 끄집어내기
a=[1, 2, 3]
a.pop()
print(a)

# 특정 요소 끄집어내기
a=[1, 2, 3]
a.pop(1)
print(a)

# 현재 리스트 확장하는 메서드 ==> extend(변수명)


# 리스트 + 리스트
a=[1,2,3]
b=['a','b']
a+=b # a=a+b  ==> 이것을 줄이면 a+=b ==> 복합연산자
print(a)

a=[1,2,3]
a*=9 #a=a*9
print(a)









