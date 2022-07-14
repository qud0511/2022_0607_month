# 변수의 스코릎(Scope)
# - 지역변수 - 함수에서만 사용, 파라미터, 함수 안에 변수들
# - 전역변수 - 파이썬 파일 안에 있는 변수,
#             같은 파이썬 파일 안에 있는 함수에서 사용가능

isGame=False # 게임 진행 여부 저장 변수

# 게임 시작 알리는 함수
def startGame():
    global isGame # 읽기만 할 때는 상관없음. isGame=False로 변경하기 때문에
    print('*** 게 임 시 작 ****')
    isGame=True   # isGame=False => isGame=True

# 게임 화면을 그려주는 함수
# 게임 중 일때 => 게임판 그리고
# 게임 중 아닐 떼 => 준비 중 그려주기
def drawGame():
    if isGame :
        print('********************')
        print('*                  *')
        print('*                  *')
        print('*                  *')
        print('*                  *')
        print('********************')

    else:
        print('* 준  비  중 *')

# 테스트
drawGame()
startGame()
drawGame()


