class JSS:
    def __init__(self):  # 클래스를 선언하는 순간 실행되는 함수
        # __init__() 메서드를 통해 객체를 초기화 했습니다.
        print('JSS 클래스선언')
        self.name=input('이름 :')
        self.age=input('나이 :')

# a=JSS() -> __intit__ 함수 안의 내용 실행

    def show(self):
        print('show 함수 실행')
        print(f'이름은 {self.name}이고 나이는{self.age}')
    # __init__ 함수와는 달리 show를 시작했을 때 자동실행되는 것이 아니라
    # show로 실행해야하는 정상적인 함수

a=JSS()
a.show()
a.name
a.age

# ---------------------
# https://hyoje420.tistory.com/45
# if __name__ == '__main__':  => main namespace, 메인 함수의 선언/시작
# __name__이라는 변수의 값이 __main__이라면 아래의 코드를 실행하라

# import했을 때 그 모듈 안에 있는 모든 코드들이 그대로 실행되는 것을 막음.
# if __name__=="__main__"이라는 조건문을 넣어주고 그 아래는 직접 실행시켰을 때만 실행되길 원하는 코드들을 넣어주는 것


# ---------------------
class car:
    def on(self):
        print('차량의 시동을 켭니다')

ray=car()
ray.on()
# 출력 결과 -> 차량의 시동을 켭니다.


# car라는 클래스를 정의하고, on라는 메서드를 정의
# 클래스의 객체(Object)가 소프트웨어에 실체화되면 이제 그것을 인스턴스(instance)라고 부름
# ray는 객체
# ray 객체(Object)는 car클래스의 인스턴스
# 인스턴스라는 표현은 특정 객체가 어떤 클래스의 객체인지 관계를 중점으로 표현할 때 사용

# 메서드method 속성은 클래스 안에서 구현하는 함수
# 메서드의 첫 번째 매개변수 이름은 클래스의 인스턴스 자신, 따라서 관례적으로 self라는 이름으로 사용

# 생성자constructor --> __init__()
# 생성자는 객체가 생성되면 자동으로 호출되어 객체를 초기화시킨다.

# https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F6b8bN%2FbtrbtAdAbf3%2F0ZE4XcTsia3iBnrKMcrkTk%2Fimg.png