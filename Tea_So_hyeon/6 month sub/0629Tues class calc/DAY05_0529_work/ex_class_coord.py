# ---------------------------------------------------------
# 클래스 기반 좌표 프로그램
# --------------------------------------------------------
# 2차원 좌표를 표현하는 데이터 타입 ---------------------------
# 클래스 명 : Coord
# 특징/속성 : width, height, cell
# 역할/기능 : __init__(width, height)    => 좌표 객체 생성
#            setWidth(new_width)        => width 속성 새로운 값으로 변경
#            setHeight(new_height)      => height 속성 새로운 값으로 변경
#            getWidth()                 => 현재 width 속성 값 읽기
#            getHeight()                => 현재 height 속성 값 읽기
#            displayPoint() => 현재 점 정보 출력
# --------------------------------------------------------
class Cell:
    def __init__(self, value="", x=0, y=0):
        self.value=value
        self.x=x
        self.y=y

    def setValue(self,value):
        self.value=value

    def getValue(self):
        return self.value

    def setXY(self, x, y):
        self.x=x
        self.y=y

class Coord:
    def __init__(self,width, height):
        self.width=width
        self.height=height
        self.cells=[]
        for w in range(width):
            for h in range(height):
                self.cells.append(Cell(value=' □ ', x=w, y=h))

    def showCells(self):
        for idx, cell in enumerate(self.cells):
            if idx !=0 and idx%self.width == 0 : print()
            print(cell.value, end='')
        print()

    def drawCoord(self):
        print('-'*10)

        for idx, cell in enumerate( self.cells):
            print(f'cell.y : {cell.y}, cell.x : {cell.x}')
            if idx == self.width: print()
            print(' ' * cell.y + cell.value, end='')

        print('-' * 10)

    def setCell(self, value, x, y):
        idx=x*self.width+y
        self.cells[idx].value=value

# -------------------------------------------------------
twoCoord= Coord(10,10)
twoCoord.showCells()
print()
import random as rd

points=set()
while True:
    if len(points) >=5: break
    x=rd.randint(0, 9)
    y=rd.randint(0, 5)
    print(x, y)
    if (x,y) not in points:
        points.add((x,y))
        twoCoord.setCell(' ■ ', x, y)
print('Drawing coorinate -----------')
twoCoord.showCells()


