user = int(input('월을 입력해주세요'))

if user in [12,1,2]:
    print('winter')
elif user in [3,4,5]:
    print('spring')
elif user in [6,7,8,]:
    print('summer')
elif user in [9,10,11]:
    print('fall')
else:
    print('잘못된 데이터입니다.')