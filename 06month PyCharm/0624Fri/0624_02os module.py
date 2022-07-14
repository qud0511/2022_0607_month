# ---------------------
# File & Dir 관련 모듈
import os.path as path
import os

# 특정 폴더 존재여부 체크 => 해당하는 폴더 없으면 폴더 생성하기
# DIR_PATH='./DATA'
# print(path.exists(DIR_PATH))        # os.path.exist()은 폴더와 파일 있는지 없는지 bool타입으로 검사

DIR_PATH='./Image/jpg/01/'

if not path.exists(DIR_PATH):
    # os.mkdir(DIR_PATH)              # os.mkdir()은 폴더 하나만 생성, 경로 상에 없으면 오류 => DIR_PATH='./Image/jpg/01/001'
    os.makedirs(DIR_PATH)             # os.makedirs()은 폴더 여러 개 생성, 경로 상에 없으면 다 만들어서 줌.

DATA_FILE=DIR_PATH+'/flower.jpg';
if not path.exists(DATA_FILE):
    print('파일 없음.')


# ----------------
# page 247도 참고
# listdir(), scandir()

# 특정 경로 안에 존재하는 내용 리스트화 ------
dataList=os.listdir('./AddressBook_ap')
print(dataList)


# page 253, time

import time as t

print(t.time())
print(t.localtime(t.time()))

currentTime=t.localtime(t.time())
print(currentTime.tm_year, currentTime.tm_hour, currentTime.tm_wday)
# 2022-06-24 2022/06/24 24/06/2022

for num in range(1,10):
    t.sleep(0.1)                           # 시간 차
    print('*', end='')



# page 257, random
import random
print(random.random()) # 0.0 ~ 1.0 사이의 실수 중에서 난수 값을 돌려주는 예를 보여준다.
