DIR_PATH='./addressbook/'
import os

if not os.path.exists(DIR_PATH):
        os.makedirs(DIR_PATH)

datalist=os.listdir(DIR_PATH)



#1. ShowAll
def ShowAll():
    for data in datalist:
        print(data[:-4])

#3. AddTxt

def AddTxt(data):
    data2=data.strip().split(',')
    result=[]
    for i in data2:
        result.append(i)
    file_name=result[0]+'_'+result[1][-4:]
    with open(DIR_PATH + '_' +file_name+'.txt', mode='w', encoding='utf-8') as file:
        file.write(data)



#2. search
def search(name_phone):
    for file in datalist:
        if name_phone in file:
            print(f'파일명: {file[:-4]}')
            with open(DIR_PATH+file, mode='r', encoding='utf-8')as f:
                print(f.read())



AddressBook='===나의 주소록===''\n''1.전체보기''\n''2.검   색''\n''3.추   가''\n''4.종   료''\n''=============='
while True:
    print(AddressBook)
    a=int(input(f'숫자를 입력해주세요:'))
    if a==1:
        ShowAll()
    elif a==3:
        data=input('이름, 전화번호, 지역, 이메일 순서대로 입력하세요\n:')
        AddTxt(data)
    elif a==2:
        name_phone=input('검색단어: ')
        search(name_phone)
    elif a==4:
        print('프로그램을 종료합니다.')
        break
    else:
        print('1~4사이의 숫자를 입력하세요')




