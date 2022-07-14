# ------------------------------------------------------
# 사용자가 입력한 댓글을 파일로 저장하기
# (조건)
# - 키보드로 댓글 입력 받기
# - 입력 받은 댓글 누적 하기
# - 댓글 입력 종료 조건으로 q 또는 Q 입력시 댓글 입력 종료
# ------------------------------------------------------

# 병준 답
filename='댓글.txt'

with open(filename, mode='a', encoding='utf-8') as file:
    while True:
        n = input('댓글을 입력하시오')
        file.write(n+'\n')
        if n=='q' or n=='Q':
            break

# 강사님 답
filename2='강사님 댓글.txt'

with open(filename2, mode='a', encoding='utf-8') as f:
    while True:
        txt= input('댓글 입력 :')
        if txt in ['q', 'Q']:
            break
        print(f'txt => {txt}')
        f.write((txt + '\n'))