# 코드가 아니고 설명을 남기고 싶은 경우에 사용함
# 샵을 주석이라고 함
# ------------------------------------------
# 메모리에 데이터 저장 실습
# 저장 문법 => 변수명 = 데이터
# 메모리에서 데이터 읽기 문법 =>  데이터 -> 변수명(Variable) / 오른쪽에서부터 읽음.
# a=20 / 20을 저장한 곳을 a라고 부르겠다.
# ------------------------------------------
# 컴퓨터(메모리)에 숫자 저장하는 법.
a=12
age=26
pw=486486
schoolnum=2016115882
height=171.8
# 숫자 앞자리에는 0 사용 못함.
# ------------------------------------------
# 컴퓨터(메모리)에 문자열 저장하는 법
name='박병준'
msg='Happy New Year'
comment="""좋은 하루 보내길!" \
        " 행복한 크리스마스 되길!"
        엔터 눌러도 여러 줄 하고 싶으면 시작과 끝 부분에 쌍따옴표 혹은 소따옴표 3개
        """
com='''긴 문장을 저장하고 싶다~~~
ㅇㅇ
ㅇㅇ
ㅇㅇ
'''
# ------------------------------------------
# 컴퓨터(메모리)에 저장된 데이터 읽어오기.
# 우클릭 -> RUN 스크립트 파일.py -> 결과를 사용자에게 보여주지 않음 -> print라고 명령해야함.
height
name
print(height)
print(comment)
# print(재료) / sum(재료) / add(재료1, 재료2) => '함수'라고 표현함.
# 기본적인 함수는 파이썬에 이미 내재되어있음. 이것을 빌트인함수, 내재함수라고 함.
# ------------------------------------------
# 실행되어야만 아는 것을 동적 타이핑이라고 함.
# 파이선은 변수명을 잃어버리면 데이터를 불러올 수 없음. 재부팅시 주소는 계속해서 변경됨.
# 파이썬은 데이터를 임의로 저장하고 그 주소와 연결해서 불러옴. 변수를 주소라고 생각할 수 있음.
# id(age) 140733039944896 => 객체의 유니크(메모리 주소) 값을 보여줌.
# 변수를 덮어씌우는 경우, 파이썬 시스템이 검사해서 사용하지 않는 데이터를 삭제함. 메모리를 효율적으로 사용하기 위함. 레퍼런스 카운트.
# 정적 타이핑 - int num = 3 / 예시) C언어 / 프로그래밍 언어별로 저장 방법, 문법 등 상이함.
id(age)
# ------------------------------------------
# type(변수)는 변수의 종류를 알려줌 -> int, float, str...
