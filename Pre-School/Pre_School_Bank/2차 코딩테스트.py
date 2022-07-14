# 1번
import operator

a_dic = {'메로나':[300, 20], '비비빅':[400, 3], '죠스바':[250, 100]}

sorted_a_dic=sorted(a_dic.items(), key=operator.itemgetter(1))

print(sorted_a_dic)


# 2번

a = list((input('입력 예시 => 홍길동:대구:hong@naver.com:010-111-2222').split(':'))for _ in range(2))

print(f'등록된 회원수: {int(len(a))}')

a.sort()

print(f'{a[0][0]},{a[1][0]}')




# 3번

for i in range(1,11):
    print(' '*(10-i), '*'*((i*2)-1))
for i in range(1,4):
    print(' '*(8), '***')

# 4번

a, b = input("주민번호를 입력하세요. : ").split("-")


if int(b[0]) % 2 == 0 :
    gender = "여자"
else:
    gender = "남자"

if int(a[:2]) > 22:
    age = (2022 - (1900 + int(a[:2])))
elif int(a[:2]) <= 22:
    age = 22 - int(a[:2])

if age > 22:
    year = str(19) + a[:2]
elif age <= 22:
    year = str(20) + a[:2]

month = a[2:4]
day = a[4:]

print(f'{age}세, {gender}, {year}년 {month}월 {day}일')


# 5번

# 5-1번
def dataSearch():
    search_1 = input('검색 : ')

    a_dic = {"홍길동 N20123":"합격", "이철수 N20124":"합격", "이나영 N20125":"불합격", "김민우 N20126":"대기", "박보민 N20127":"불합격", "이나영 N20128":"합격", "김지은 N20129":"대기" }

    print(f'검색 결과:  {a_dic[search_1]}')

dataSearch()

# 5-2번
def searchlist():

    s_2 = input("검색 : ")

    a_dic = {"홍길동 N20123":"합격", "이철수 N20124":"합격", "이나영 N20125":"불합격", "김민우 N20126":"대기", "박보민 N20127":"불합격", "이나영 N20128":"합격", "김지은 N20129":"대기" }

    b_dic = dict(map(reversed, a_dic.items()))

    print("검색결과 : ", b_dic[s_2])
searchlist()



# 5-2 개선안
def searchlist():

    s_2 = input("검색 : ")

    c_dic = {"홍길동(N20123) 이철수(N20124) 이나영(N20128)":"합격", "이나영(N20125) 박보민(N20127)":"불합격", "김민우(N20126) 김지은(N20129)":"대기"}

    b_dic = dict(map(reversed, c_dic.items()))

    print("검색결과 : ", b_dic[s_2])
searchlist()