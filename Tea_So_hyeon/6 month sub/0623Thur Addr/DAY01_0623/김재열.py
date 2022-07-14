#1. ShowAll
def ShowAll():
    print('전체보기''\n''홍길동_1234''\n''마징가_1111''\n''홍길동_8888''\n''베트맨_2323')

#3. AddTxt

def AddTxt():
    data=input('이름, 전화번호, 지역, 이메일 순서대로 입력하세요\n:')
    data2=[x.strip().strip(',') for x in data.split(' ')]
    file_name=data2[0]+'_'+data2[1][-4:]+'.txt'
    file = open(file_name, mode='w', encoding='utf-8')
    file.write(data)
    file.close()


#2. look
def search():
    search=input('검색단어\n')
    for file in filelist



AddressBook='===나의 주소록===''\n''1.전체보기''\n''2.검   색''\n''3.추   가''\n''4.종   료''\n''=============='
while True:
    print(AddressBook)
    a=int(input(f'숫자를 입력해주세요:'))
    if a==1:
        ShowAll()
    elif a==3:
        AddTxt()
    elif a==2:
        pass
    elif 4 in [a]:break
    else:
        print('1~4사이의 숫자를 입력하세요')




