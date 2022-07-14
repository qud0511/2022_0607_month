def print1():
    print('=== 나의 주소록 ===')
    print('1. 전체보기')
    print('2. 검   색')
    print('3. 추   가')
    print('4. 종   료')
    print('=================')

print1()

fileName = 'jusolok.txt'
with open(fileName, mode='a', encoding='utf-8') as fn:
   while True:
       menu = input('메뉴 선택:')
       if menu in ['4']: break
       elif menu == '1':
           total = open(fileName, mode='r', encoding='utf-8')
           data = total.read()
           print(f'전체 보기\n{data}')
       elif menu == '3':
           add = input('이름, 전화번호, 지역, 이메일 :')
           fn.write(add + '\n')
       elif menu == '2':
           search = open(fileName, mode='r', encoding='utf-8')
           a = input('검색 단어 :')
           readData = search.readline()
           print(f'파일명: {a[:3]}_{a[4:8]}')
           print(f'{a[:3]} {a[4:8]} {a[9:10]} ')
       else:
           print("잘못 입력하셨습니다")
           break