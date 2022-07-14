#-------------------------------------------------------------------------------
# 파이썬에서 미리 만들어서 제공하는 클래스
# int, float, bool, str, list, tuple, dict, set
#------------------------------------------------------------------------

num = 123
num2 = int(123) # 실제로는 int() 새성자 실행

print(num, num2)

name ='hong'
name2 = str('hong')

#------------------------------------------------------------------------
# 내가 만드는 클래스 -> 평면에 좌표값을 저장하는 데이터
# 클래스명 : Point
# 속성/특징/변수 : x, y
# 역할/기능/함수 : Point 클래스로 메모리에 존재하는 객체(인스턴스) 생성하는 메서드 __init__(self, x, y)
#               객체(인스턴스)에 값을 읽어주는 메서드 >> get속성명() --? 현재 속성값 반환
#               객체(인스턴스)에 값을 변경해주는 메서드 >> set속성명(새로운값)
#               _ << 클래스 숨기는 기능 - 보여주고 싶은 클래스만 쓰겠다 .
#
#----------------------------------------------------------------------------
class Point():
    # Point 인스턴스를 생성하는 메서드
    def __init__(self, x, y):
        self._x = x
        self.y = y

    # # Point 인스턴스에 저장된 속성(변수) 값 읽어오는 메서드 -> getter메서드
    # def getX(self): return self.x
    # def getY(self): return self.y
    # def getXY(self): return self.x, self.y
    #
    # # Point 인스턴스에 저장된 속성(변수)값 저장하는 메서드 => setter 메서드
    # def setX(self, x): self.x = x
    # def setY(self, y): self.y = y
    # def setXY(self, x, y):
    #     self.x = x
    #     self.y = y
    # 내가 원하는 기능의 메서드 -----------------------------------------------------------------
    # Point 인스턴스의 정보 출력하는 메서드(Method)
    def showPoint(self):
        print(f'현재 좌표값 {self._x}, {self.y}')

    # Point 인스턴스에 해당되는  좌표를 그리는 메서드
    # x 값은 가로로 이동, y 값 => 다음 줄 \n
    def drawPoint(self):
        print('\n'*self.y, end=" ")
        print('-'*self._x+' ★ ', end='')
#-------------------------------------------------------------------------------------
# Point 인스턴스 즉 객체 생성 하기
p1=Point(10, 5) # 객체 생성
p1.drawPoint()
# p1.setX(5)
# print(p1.getX(), p1.x)
#
nums = [1,4,5,2,2,5,2,8,3]

points=[Point(10,10), Point(3,4), Point(4,2), Point(0,0)]

points[3].showPoint()
points[1].showPoint()






# 주석 풀고 위에 주석 걸기
# class Point:
#     # Point 인스턴스를 생성하는 메서드
#     def __init__(self,x,y):
#         self.__x=x          # 언더바 _, __치면 밖에서 못봄. 숨김.
#         self.y=y            # getter(), setter() 함수같이 만들어줘야지 변경가능함. 그냥 _치면 아예 못바꿈.
#
# p1=Point(10,5)
# p1.y
# p1.z=100        # 함수 정의에는 z가 없는데
# p1.z            # 야매로 끌고 옴. 다른 객체지향 프로그램은 있을 수 없는 일