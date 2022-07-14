# 게임 프로그램 벽돌깨기
# - 메뉴를 선택하면 벽돌이 하늘에서 내려오면서 방향키를 움직여서 깨는 게임
# - 벽돌이 하늘에서 내려오는 속도를 조절해서 난이도 구성
# - 속도 => 1분 간격으로 속도를 1씩 즈악
# - 종료 => 5분 시간안에 벽돌 50 못깨면 탈락

# Player => 닉네임, 단계, 점수

# -----------------------
# 게임하는 사람의 정보를 저장하는 변수들
nickName=''
level=0
score=0
lanking=0
# nickName2='' ...3 ...4 계속해서 만들면 메모리 낭비
# level=0
# score2=0
# lanking2=0
player1=None
player2=None


# 게임하는 사람의 정보 입력 받기 --------------------
# 함 수 명 : setPlayer
# 파라미터 : 없음
# 반 환 값 : 없음

# def setPlayer():
#     nickName = input('닉네임 :')
#     level = 0
#     score = 0
#     lanking = 0

def setPlayer():
    global player1, player2
    nickname = input('닉네임 : ').split()
    if player1 == None:
        player1=player(nickname)


# 메뉴 출력하기 ------------------------------
# 함 수 명 : displayMenu
# 파라미터 : 없음
# 반 환 값 : 없음
def displayMenu():

    print('1. 회원가입')
    print('2. 게임 시작')
    print('3. 랭킹 보기')
    print('4. 종료')


# ----------------------
# 프로그램 코드
while True:
    displayMenu()
    select = input()

    if select == '4':
        # 그냥 break하면 안되고, 파일에 기록하고 종료해야 함. # 그때는 게임 시작을 해야함. 회원가입부터가 아니라
        break
    elif select == 1:
        setPlayer()

# -------------------------------------
class player:
    def __init__(self, nickname, level = 0, score = 0, lanking=0):
        self.nickname = nickname
        self.level = 0
        self.score = 0
        self.lanking = 0

    # 클래스의 인스턴스 변수들의 값을 업데이트 또는 읽기 하는 메서드
    #set메서드 - get메서드
    def setlevel(self, level):
        self.level = level

    def setScore(self, score):
        self.score = score

    def setLanking(self, lanking):
        self.lanking = lanking

    def update(self, level, score, lanking):
        self.level = level
        self.score = score
        self.lanking = lanking

    def getNickname(self): return  self.nickname

    def getScore(self): return self.score

    def getLanking(self): return self.lanking



