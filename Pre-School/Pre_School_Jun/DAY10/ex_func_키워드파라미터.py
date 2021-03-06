# -----------------------------------------------------------------------
# 키워드파라미터 함수
# 키=값       형태의 가변인자를 받아서 처리하는 함수
# 선언형태  ==>  def 함수명(**변수명):
# 호출형태  ==>  함수명(문자열키='값', 문자열키=20)
# -----------------------------------------------------------------------





# -----------------------------------------------------------------------
# 기    능 : 회원가입 시 입력되는 사람마다 다른 정보를 저장하는 함수
# 함 수 명 : saveInfo
# 매개변수 : 가변이고 키와 값의 형태 **infos
# 반 환 값 : 없음
# -----------------------------------------------------------------------
def saveInfo(**infos):                          # 딕셔너리
    keys=infos.keys()
    for key in keys:
        print(key, infos.get(key))

    for item in infos.items():                 #  세 가지 방법 모두 결과 같음.
        print(item[0], item[1])

    for k,v in infos.items():
        print(k,v)                             # 언팩킹

# 함수 사용
a=saveInfo(name='Hong', job='student', age=12)
b=saveInfo(email='abc@naver.com')
# 가변인자 일 때 사용 못함. 숫자 하나? saveInfo(1='JJAA')
print(a,b)


