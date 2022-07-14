from settings import *


def get_questions():
    with open(QUESTIONS, 'r', encoding='utf-8') as f:
        total = f.read()
    head_question = []
    MBTI_answers = []
    for data in total.split('<title>')[1:]:


        datas = [x for x in data.strip().split('\n') if len(x)][2:]   # 공백 0칸

        for i in range(len(datas)):
            if not i % 2:   # i를 2로 나눈 나머지가 0이라면 = 2의 배수라면
                head_question.append(datas[i])
            else :          # i를 2로 나눈 나머지가 0이 아니라면 = 2배의 배수가 아니라면
                MBTI_answers.append(datas[i])
    # i가 0일 때는 폴쓰고 나머지 숫자는 트루
    return head_question, MBTI_answers
        #if 다음에 ==이 없다면 기본적으로 숫자일때는 0이 폴쓰고 1이 트루인데 트루값을 기본적으로 줌 # 0제외 True라고 나옴

class mbtiTest():
    head_question, MBTI_answers = get_questions()

    def __init__(self):
        self.mbti_type = ''
        self.testing = False # 테스트가 시험 중인데, false 시행 중이지 않다.
        self.answer = 0
        self.question_num = -1    # +1하면 0번 인덱스라서
        self.result = 0


    # 함수 설명 --------------------------------------
    #   함수명 : mbtiTest.mbtiDetail
    #   입력값 : mbti_type
    #   반환값 : mbti 유형 설명 문자열 리스트
    #   기능   : 해당 유형의 자세한 특징 불러오기
    # ------------------------------------------------
    def mbtiDetail(self, mbti_type):
        path = './mbti_info/'+mbti_type+'.txt'       # 지금은 ./mbti_info/.txt 이 상태 ===>  ./mbti_info/ENFP.txt
        with open(path, mode='r', encoding='utf-8') as f:
            data = []
            for d in f.readlines():
                try:
                    for s in d.split('. '):
                        data.append(s)
                except:
                    data.append(d)
        return data


    # 함수 설명 --------------------------------------
    #   함수명 : mbtiTest.show_detail
    #   입력값 : detail_text (설명 입력칸), mbti_type
    #   반환값 : Nan
    #   기능   : 해당 유형의 자세한 특징 입력 칸에 출력
    # ------------------------------------------------
    def show_detail(self, detail_text, mbti_type):
        detail = self.mbtiDetail(mbti_type)

        detail_text.config(state='normal')
        detail_text.delete('1.0', 'end')
        for i in range(len(detail)):
            if len(detail[i].strip()):
                detail_text.insert('current', detail[i] + '.\n\n')
        detail_text.config(state='disabled')


    # 함수 설명 --------------------------------------
    #   함수명 : getMBTI_gui.getMBTI
    #   입력값 : none
    #   반환값 : mbti_type
    #   기능   : tkinter 사용해 설문에 응답 입력 받고 mbti 유형 추정
    # ------------------------------------------------
    def getMBTI_gui(self, question_label, detail_text):
        self.question_num = self.question_num+1     # 원래 question_num=-1
        if self.question_num == 12 : # 모든 질문 문답 시(테스트가 끝났을 때)
            self.testing = False    # 검사 종료      #gui 시작하면 true로 바뀜. 끝나면 false로 바뀜
            question_label['text'] = '당신의 MBTI 성향은 ' + self.mbti_type + '!' # 검사 결과 출력
            self.show_detail(detail_text, self.mbti_type) # 상세 결과 출력


            self.question_num = -1  # 다음 검사를 위해 초기화
        else:  # 테스트 할 때
            kind = MBTI_KIND[self.question_num // 3] # 분류 유형 변환




            self.result = self.result + self.answer   # 0= 0+0    =>     answer 왼쪽버튼은 1, 오른쪽버튼 0 앤써값이 계속 드감

            if self.question_num % 3 == 2:  # 1,2,3,번 문제는 0,1,'2'  2를 3으로 나누면 '2'   45'6' -> 34'5' -- '   2번 문제,5번문제,8번문제, 11번문제 마다 코드실행
                if self.result > 1: # e성향 다 누른다치면 3, i성향만 누른다치면 0 -> 2하고 3은 e성향인셈, 0하고 1은 i 셈 그러니까 1보다크면 e성향이니까ㅓ 앞인덱스줌.
                    self.choice = 0 # 유형 '문자열' 의 첫 번째 값
                else:
                    self.choice = -1 # 유형 '문자열' 의 마지막 값
                self.mbti_type = self.mbti_type+ kind[self.choice] # 뽑아낸 문자를 최종 결과에 추가    -> 3문제 풀고 E 넣고, 3문제 풀고 N넣고.... 4글자 완성  12문제 끝날떼까지

                self.result = 0 # 분류 유형 변환시 초기화

            # head 문제와 대답 후보
            question = mbtiTest.head_question[self.question_num]
            answers =  mbtiTest.MBTI_answers[self.question_num].split('vs')
            question_label['text'] = question + '\n\n'+ answers[0] + '\nVS \n' + answers[1]

