# BMI 건강지수 프로그램
# 키, 몸무게 입력받기 => 정수 변환
# BMI 지수 구하기 => BMI 공식 = 몸무게kg / 키m * 키m *
#                  키m = 키cm / 100
# BMI 지수에 따른 건강 상태 출력
print('-'*40)
print(f'BMI 건강지수 프로그램')
print('-'*40)

# (1) 키와 몸무게 데이터 입력 받기
data=input('키와 몸무게를 입력하세요. 예: 180 77')

# (2) 데이터 전처리, 즉 원하는 형태로 만들기
data=data.split()            # 공백을 기준으로 쪼개기    180 77 ==> [ '180' , '34' ]

# str -> int
data[0]=int(data[0])
data[1]=int(data[1])

# cm -> m 단위변환
data[0] = data[0]/100

# 준비된 데이터 확인
print(f'준비 완료 : {data}')

# (3) BMI 공식에 맞추어 BMI 지수 계산
bmi=data[1]/(data[0]*data[0])
print(f'bmi : {bmi}')

# (4) 사용자에게 BMI 건강지수 출력하기
print('-'*40)
if bmi<18.5:
    print(f'당신은 저체중 - {bmi}입니다.')
elif bmi <= 24.9:
    print(f'당신은 저체중 - {bmi}입니다.')
else:
    print(f'당신은 과체중 - {bmi}입니다.')