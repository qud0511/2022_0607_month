# PATH => 경로
# 절대 경로 : 파일 및 폴더 존재하는 위치의 경로       예) C:\Uesr\....\....
# 상대 경로 : 현재 코드 파일 기준으로 경로를 지정, 나를 기준으로
#   .     : 현재 위치
#   ..    : 상위 한단계 위
# --------------------------------------
filename=r'C:\Users\User\PycharmProjects\pythonProject\0623'
filename='../Data/home.html'
filename='./home.html'

# home.html 파일을 라인 단위로 읽어서 화면에 출력하기

# 파일 읽기
file=open(filename, mode='r', encoding='utf-8')

# 파일 읽기
# data=file.read(6)
# print(f'all data => {data}')


# while True:
#     data=file.readline()
#     if not data : break
#     print(f'line data => {data.lstrip("\n")}')

# f-string expression part cannot include a backslash???
# __chars????


while True:
    data= file.readline()
    if not data: break      #데이터가 없다면 브레이크
    data= data.split()
    if len(data)>0: print(data)

# 파일 닫기
file.close()

print('\n')

# with ~ as 구문
# file.close() 알아서 해줌.
with open(filename, mode='r', encoding='utf-8') as file:
    while True:
        data = file.readline()
        if not data: break  # 데이터가 없다면 브레이크
        data = data.split()
        if len(data) > 0: print(data)


# https://withcoding.com/86