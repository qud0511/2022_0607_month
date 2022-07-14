# [실습]
# CSV 파일 읽고 컬럼별 최고값과 값의 개수 출력

import pandas as pd

DIR_PATH='../../Data/'
FILE_NAME=DIR_PATH+'iris2.csv'

# (1) File ==> DataFrame으로 가져오기
irisDF_2=pd.read_csv(FILE_NAME, header=None)

# (1) 데이터 확인하기 -------------
irisDF_2.info()

# CSV 파일 읽고 컬럼별 최고값과 값의 개수 출력

print('irisDF_2.columns->\n', irisDF_2.columns)

for i in irisDF_2.columns:
      print(f'{i}번째 컬럼의 값의 최고값->\n',
            irisDF_2[i].max())

for i in irisDF_2.columns:
      print(f'{i}번째 값의 개수->\n',
            irisDF_2[i].value_counts())
