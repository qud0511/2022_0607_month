#-------------
# 파일 읽고 쓰기 => 파일 입출력(I/O)(Input, Output)
#-------------

filename='mydata.txt'

# 파일 쓰기 -------------------------
# (1) 파일 열기
# mode 'w' 는 파일이 없으면 생성 후 쓰기
#            파일 있으면 내용 지우고 쓰기
fileIO=open(filename, mode='a', encoding='utf-8') #통로

# mode 'a' => (append 약자)
#           => 파일 없으면 생성 후 쓰기
#           => 파일 있으면 덧붙이기. 즉 append
#stream: InputStream, OutputStream
#파일 -> 컴퓨터 :  OutputStream
#파일 <- 컴퓨터 :  InputStream

# (2) 파일에 데이터 쓰기
fileIO.write('Good\n') #\n: 줄바꿈
fileIO.write('Happy\n')
fileIO.write('123\n')
# (3) 파일 닫기
fileIO.close()

# 파일 읽기 —————————————————
# mode ='r' => read 의 약자, 기본값
# (1) 파일 열기
fileIO=open(filename, mode='r')

# (2) 파일 일기
data=fileIO.read(3) #파일 전체 데이터 가져오기
print(f'read data => {data}')
print(f'read data type=> {type(data)}')

fileIO.seek(0)
data2=fileIO.read()
print(f'read data2 => {data2}, len = {len(data2)}')

# 파일 포인트 제일 앞으로
fileIO.seek(0)
# 파일에서 1줄 읽기
data3=fileIO.readline()
print(f'read data3 => {data3}')
data3=fileIO.readline()
print(f'read data3 => {data3}')
data3=fileIO.readline()
print(f'read data3 => {data3}')

#1줄씩 읽어서 리스트에 담아서 가져오기
data4=fileIO.readlines()
print(f'read data4 => {data4}')
#print(f'read data4 => {data4[0]}')

# (3) 파일 닫기
fileIO.close()