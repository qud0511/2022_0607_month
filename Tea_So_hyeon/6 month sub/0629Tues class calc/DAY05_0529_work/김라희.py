# ------------------------------------------------------------
# 클래스 기반 계산기 프로그램
# ------------------------------------------------------------
# 4칙연산을 기본으로 구현하는 계산기 데이터 타입
# 클래스이름 : Calc
# 특징/속성 : total
# 역할/기능 : __init__(total)       => 계산기 객체 생성
#           setTotal(new_total)    => total값 새로 변경
#           getTotal()             => 현재 total값 읽기
#           plus(n)                => 더하기
#           minus(n)               => 더하기
#           mul(n)                 => 곱하기
#           div(n)                 => 나누기 몫
#           divr(n)                => 나누기 결과
#           drawing()              => 터미널에 결과 출력
# ------------------------------------------------------------
class Calc:
    def __init__(self, total=0):
        if isinstance(total, (int, float)):
            self.total = total

    def setTotal(self, total=0):
        if isinstance(total, (int, float)):
            self.total = total

    def getTotal(self):
        return self.total

    def plus(self, n):
        self.total += n
        return self.total

    def minus(self, n):
        if not self.total:
            self.total += n
            return self.total
        self.total -= n
        return self.total

    def mul(self, n):
        if not self.total:
            self.total += n
            return self.total
        self.total *= n
        return self.total

    def div(self, n):
        if not n:
            try: self.total / n
            except ZeroDivisionError as e:
                print(e)
            else:
                self.total += n
                return self.total
        self.total /= n
        return self.total

    def divr(self, n):
        self.total %= n
        return self.total

    def drawing(self):
        print(
            f'\n{" 계산기 ":―^11}'
            f'\n  0. 종료'
            f'\n  1. 초기화'
            f'\n  2. 더하기'
            f'\n  3. 빼기'
            f'\n  4. 곱하기'
            f'\n  5. 나누기 몫'
            f'\n  6. 나누기 결과'
            f'\n{"―"*10}'
        )
# -------------------------------------------------------
if __name__ == '__main__':
    calcApp = Calc()
    while True:
        calcApp.drawing()
        select = input('select a menu ')
        if select == '0': break
        elif select == '1':
            calcApp.setTotal()
        elif select == '2':
            n = int(input('plus number '))
            print('total', calcApp.plus(n))
        elif select == '3':
            n = int(input('minus number '))
            print('total', calcApp.minus(n))
        elif select == '4':
            n = int(input('multipe number '))
            print('total', calcApp.mul(n))
        elif select == '5':
            n = int(input('divide number '))
            print('total', calcApp.div(n))
        elif select == '6':
            n = int(input('divide remainder number '))
            print('total', calcApp.divr(n))
        else: break
