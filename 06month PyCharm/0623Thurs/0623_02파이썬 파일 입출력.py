# ASCII(American Standard Code for Information Interchange, 미국 정보 교환 표준 부호) CODE, ANSI CODE
# EUC-KR, CP949
# UTF-8, UNICODE

# 파일 읽고 쓰기 => 파일 입출력(I/O)
# input stream output stream
filename = 'mydata.txt' # 경로 지정


# 파일 쓰기
# (1) 파일 열기
# file = open(filename, mode='w', encoding='utf-8')
# mode='w' => 파일 없으면 생성 후 쓰기
#          => 파일 있으면 내용 지우고 쓰기

file = open(filename, mode='a', encoding='utf-8')
# mode='a' => append의 약자, 파일이 없으면 생성 후 쓰기
#          =>               파일이 있으면 덧붙이기, 즉 append함.


# (2) 파일에 데이터 쓰기
file.write('Good\n')   # \n줄바꿈 안하면 붙어서 출력됨
file.write('Happy\n')
file.write('12345')     # 숫자도 상관없이 '', "" 사용, 무조건 str 타입


# (3) 파일 닫기
file.close()

# -----------------

# 파일 읽기
# mode='r => read의 약자, 기본값

# (1) 파일 열기
file = open(filename, mode='r')


# (2) 파일 읽기
data = file.read()                          # 파일 전체 데이터 가져오기
print(f'read data => {data}')
print(f'read data type => {type(data)}')
                                        # 읽고 나면 커서 제일 끝으로 이동함. so, data2 read 시 0 출력


file.seek(0)           # 파일 포인트 제일 앞으로, 0번 자리로!, 커서 제일 앞으로 감.
data2 = file.read()
print(f'read data2 => {data2}, len => {len(data2)}')

data3 = file.readline()                # 한 줄 읽기
print(f'read data3 => {data3}')
data3 = file.readline()
print(f'read data3 => {data3}')


data4 = file.readlines()              # 한 줄씩 읽어서 리스트에 담아서 가져오기
print(f'read data4 => {data4}')


file.read(6)                    # 공백 포함 6개 읽음

# (3) 파일 닫기
file.close()



