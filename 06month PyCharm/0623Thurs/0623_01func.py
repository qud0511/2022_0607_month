# https://wikidocs.net/64
# 람다 lambda 매개변수 : 표현식(결과)
# def 함수이름(매개변수):
#   return 결과
def add2(x,y):
    return x+y

lambda x,y: x+y

# map(함수, 리스트) => list(map(함수, 리스트))
print( list( map( lambda x: x**2, range(5))))

# reduce(함수, 시퀸스)
# 시퀸스(문자열, 리스트, 튜플)의 원소들을 누적으로 함수에 적용
from functools import reduce
print( reduce( lambda x,y: x+y, [0,1,2,3,4]))
print( reduce( lambda x,y: y+x, 'abcde'))   #????

# filter(함수, 리스트) => list(filter(함수, 리스트))
# 리스트에 들어있는 원소들을 함수에 적용시켜서 참인 값들로 새로운 리스트를 생성
print( list( filter( lambda x: x<5, range(10))))

print( list( filter( lambda x: x%2, range(10))))
# '참'=0, '거짓'=1
# 위 함수에서 0을 2로 나눈 나머지는 0 => 람다함수 결과값은 0 => 0은 '거짓'이니까 필터함수로 버려짐.
# 1을 2로 나눈 나머지는 1 => 람다함수 결과값은 1 => 1은 '참'이니까 통과 ==> 홀수만 출력

# -----------------------------------------------------------

# https://velog.io/@suasue/Python-%EA%B0%80%EB%B3%80%EC%9D%B8%EC%9E%90args%EC%99%80-%ED%82%A4%EC%9B%8C%EB%93%9C-%EA%B0%80%EB%B3%80%EC%9D%B8%EC%9E%90kwargs

# 패킹Packing은 여러 개의 데이터를 컬렉션으로 묶어 변수에 대입하는 것이다.
numbers=(1,2,3,4,5)
# 언패킹Unpacking은 컬렉션 속의 요소들을 여러 개의 변수에 나누어 대입하는 것이다.
a,b,c,d,e=numbers
# 언패킹 시 변수의 갯수와 요소의 갯수가 일치해야 한다. 불필요한 값을 언더바를 사용하여 생략할 수 있다.
a, _, _, d, e= numbers #필요 없는 요소를 _ 변수에 대입

# 남은요소 대입하기
# 언패킹 시, 좌변의 변수 중 하나에 아스타리크 기호(*)를 붙이면, 남은 요소 전체를 리스트에 담아 대입한다.
a, b, *rest = numbers # 1, 2를 제외한 나머지를 rest에 대입
print(a,b,rest) # 1 2 [3, 4, 5]

a, *rest, e = numbers # 1, 5를 제외한 나머지를 rest에 대입
print(rest) # [2, 3, 4]
# -----------------------------------------------------------
# -----------------------------------------------------------
# GUI(Graphic User Interface) -> 메모장 등
# 함수 사용하기 == 함수호출

def gugudan(m):
    for n in range(1,10):
        print(f' {m} * {n} = {m*n}')
gugudan(3)

def strAdd2(str1,str2):
    print(str1+str2)
strAdd2('안녕','하세요')

n=int(input('구구단 n단 출력'))
for i in range(1,10):
    print(f' {n} * {i} = {n*i}')

# 가변인자, page 162

# 인자 개수가 미정인 경우
# - 유사하거나 동일한 코드 부분, 그래도 인자(인수) 개수만 계속 변경 => 유동적
# *매개변수 ==> 0개 ~ n개 인자

def addNum(*nums):
    print(f'nums type : {type(nums)}')
    total = 0
    for num in nums:
        total += num
    return print(total)

addNum(1)
addNum(1,1,1,1,1,1,1,)
addNum(1,2,3,4,5,6,7,8,9,10,11,12,13,14)
addNum()

# 키워드 파라미터 형태, **매개변수

# 기능: 평균 구하는 함수
# 함수명: getAvg
# 파라미터: 과목명 - 점수 유동적 => **subjects
# 가변인자 함수 => 매개변수 0개 ~ n개
# 리턴값: 평균(float)

def getAvg(**subjects):
    print(f'subjects type : {type(subjects)}')
    values=subjects.values()
    total=0
    for value in values: total += value
    print(f'total => {total}')
    return total / len(values) if len(values)>0 else '잘못된 데이터입니다.'

print(getAvg(국어=12, 영어=98, 수학=88))
print(getAvg(영어=94, 수학=88))
print(getAvg())

# ---------------------------------------------------
# 함수의 데이터 타입

print(type(strAdd2), id(strAdd2))

list=[add2, getAvg]
print(list[0](1,2))
print(list[1](국어=12, 영어=98, 수학=88))




# 함수와 변수의 관계
# -----------------------------------------------------
# 변수 위치에 따른 분류

# 지역변수Local Value
# 함수 안에 존재하는 함수, 함수에서만 사용 가능, 함수 실행 후 메모리에서 사라짐

# 전역변수Global Value
# 함수 밖에 존재하는 함수, 프로그램 어디서나 사용 가능, 프로그램 종료 시 메모리에서 사라짐.
