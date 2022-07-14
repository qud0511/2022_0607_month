# 클래스Class
# 특정 기능을 하기 위한 변수와 함수를 하나로 묶어둔 Type

# 글로벌 변수를 없애고, 모든 변수를 어떠한 스코프에 소속시킨다.
# 몇 번이고 재사용할 수 있다.
# 코드의 수정을 최소화한다.
# 함수 실행중에, 함수 자신을 다시 호출하는 처리 등이 가능하게 하다
# https://engineer-mole.tistory.com/190

# -------------------------------------------
# 파이썬에서 미리 만들어서 제공하는 클래스 => bulit-in class
# => 숫자, 문자 저장할 수 있는 class
# => int, float, str, bool, list, tuple, dcit, set
# -------------------------------------------
# 내 프로그램(프로젝트)에서 데이터를 표현하는 클래스
# 사용자 정의 클래스

# 생성방법
# class 클래스명:
#       변수      -> 클래스가 나타내는 속성, 특징, 성질,..., 외형
#       메서드    -> 클래스의 기능, 역할
# => 클래스를 생성한 것이지 메모리에 데이터를 저장 X.
# ------------------------------------------

# --------------------------------------------
# 계산기 프로그램을 만들고자 함
# => 계산기 데이터 타입 생성
#   -> 연산(4칙연산) ===> 기능 ===> 함수
#   -> 데이터       ===> 변수

# 클래스명  <- 어떤 데이터가 저장되는지 알 수 있도록 명명 calc
# 변수     <-                                     num1, num2
# 함수(메서드)  <-                                 plus(), minus(), nult(), div()

class calc:
    #변수
    num1=0
    num2=0

    # 객체 생성 constructor
    # 클래스명() -> 객체 생성 시 호출되는 메서드
    # 파이썬에서 클래스 생성 시에 자주 사용되는 기능의 메서드를 미리 만들어서 제공하는 것
    # 형태 def __메서드명__(self):
    # __init__(): 객체 생성 시 변수 초기화하는 경우 사용
    def __init__(self, num1=0, num2=0):
        print('__init__')
        self.num1 = num1
        self.num2 = num2

    # 클래스의 기능에 해당하는 메서드
    def plus(self, num1, num2):    # 메모리 낭비를 줄이기 위한 self 키워드
        print(num1 + num2)

    def minus(self, num1, num2):
        # print(self.num1 + self.num2)  # 지역변수 --> num1=0, num2=0
        print(num1 - num2)

    def mult(self, num1, num2):   # 여기 self는 전역변수? 밖에 주어지는 것을 사용?
        print(num1 * num2)

    def div(self, num1, num2):
        print(num1 / num2)

# 클래스 사용하기 ===> 메모리에 데이터를 저장 => 힙에 객체 생성
#              ===> 클래스명() -> 객체 생성
myCalc = calc()
print(f'myCalc type => {type(myCalc)}')   # calc 타입이라고 나옴.

# 클래스 안에 존재하는 변수, 함수 접근 --------------------------
# 객체변수명.변수, 객체변수명.함수명()

# myCalc(4,5)
# myCalc.plus(4,2)

# yourCalc = calc(2,9)
# yourCalc.div(12,3)

# ----
class dog(object):
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

    def newBorn(self):
        print('댕댕이 이름은', self.breed, '색은', self.color)

dog1=dog("골든 리트리버",'검정')
dog2=dog('치와와', '흰색')

dog.newBorn(dog1)





