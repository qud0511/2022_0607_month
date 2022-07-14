# 상속inheritance
# 클래스 확장 및 기존 클래스 재사용 & 기능 확장
# 부모 클래스가 가진 것을 모두 자식 클래스에서 사용
# 부모 클래스로부터 상속받은 함수를 재정의 가능, Overriding오버라이딩
# 형식 -> class 자식클래스명 ( 부모클래스명 )

class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def displayInfo(self):
        print(f'A => {self.x}, {self.y}')

class B(A):
    def calc(self):
        print(self.x * self.y)

b=B(5,3)
b.displayInfo()
b.calc()

# 할아버지, 증조할아버지... 다 물려받음.
class C(B):
    def add(self):
        print(self.x + self.y)

# 오버라이딩, 오버라이딩한 것을 우선 함.
    def mult(self):
        print(self.x * self.y, self.x - self.y, self.x + self.y )

c=C(4,5)
c.calc()

