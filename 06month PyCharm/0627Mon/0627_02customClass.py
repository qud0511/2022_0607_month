# --------------------------------------------------------
# 사용자 정의 클래스 => 학생을 표현하는 데이터 타입
# --------------------------------------------------------
# 특징/성질/외형 => 변수 --- 필드/속성(Field/Attribute)
#                 교복, 급식, 학교, 담임, 성적, 학년, 반, 학번, 이름
# 역할/기능      => 함수 --- 메서드(클래스 안의 함수를 Method라고 함)
#                 공부한다, 학교에 간다, 시험친다.
# --------------------------------------------------------
# 클래스명 => student
# 속   성 => 학번, 학교, 학년, 석차
# 역   할 => 공부하다, 시험친다.
# --------------------------------------------------------
class student:
    # 클래스 변수 ---> 모든 인스턴스가 함께 사용 함.
    school = '대구중학교'
    # 인스턴스(객체) 생성 시 초기화 메서드
    def __init__(self, stdNum, yearNum, grade):
        self.strNum = stdNum
        self.grade = grade
        self.yearNum = yearNum

    # student의 클래스 역할/기능
    # ㅇㅇㅇ은 ㅇㅇ과목을 공부한다. -----------------------
    def study(self, subject):
        print(f'{self.strNum}은 {subject}과목을 공부한다.')

    # ㅇㅇㅇ이 ㅇㅇㅇ시험을 친다. ----------------------



# -----------------------------------
# 현대 자동차를 표헌하는 데이터 타입, 즉 class 생성
# 클래스명 : car
#           클래스 변수 :
# 속성 /특징 : 제조사, 차번호, 차종류, 책상
#             -> 클래스  변수 :
#             -> 인스턴스  변수 :
# 역할 / 기능 : 이동한다, 정지한다, 차정보 출력한다.
#           -> 이동한다 => ㅇㅇㅇ 자동차가 XX에서 XX로 간다
#           -> 정지한다 => ㅇㅇㅇ 자동차가 XXX에 정지한다.
#           -> 차 정보 출력한다. => 제조자, 차종류, 차번호

# 숫자 10개 저장하기

class car:

    # 클래스 변수
    brand = '현대'

    # 인스턴스 객체 생성 및 초기화 함수
    def __init__(self, carNum, carType, carColor):
        self.carNum = carNum
        self.carType = carType
        self.carColor = carColor

    # car 클래스 기능 및 역할 메서드
    def move(self, start, end):
        print(f'{self.carNum}자동차가 {start}에서 {end}로 이동한다.')

    def stop(self, target):
        print(f'{self.carNum}자동차가 {target}에서 정지한다.')

    def displayInfo(self):
        print(f'번호 : {self.carNum}')
        print(f'종류 : {self.carType}')
        print(f'색상 : {self.carColor}')
        print(f'제조사 : {car.brand}')

# 자동차 데이터 저장 => 자동차 인스턴스 생성 => 클래스명() -- __init__()
myCar=car(1234,'suv','hotpink')
myCar.move('경북대학교', '경주')
myCar.displayInfo()

# 정수 10개 => car 데이터 10개 저장
nums=[]
for n in range(10): nums.append(n*10)

cars=[]
# for n in range(10):
#     cars.append( cars( n*1111, 'suv', 'black'))

for car in cars:
    print(f'{car.carNum}')
    car.displayInfo()