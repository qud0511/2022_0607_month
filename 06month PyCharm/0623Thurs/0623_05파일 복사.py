# 조건
# home.html 파일을 복사해서 html.txt 파일로 만들기
# - 함수명 : fileCopy

def fileCopy1(filenames):
    # 원본파일 열고 데이터 꺼내기
    sourceFile=open(filenames, mode='r', encoding='utf-8')
    data=sourceFile.read()
    sourceFile.close()

    # 복사본 파일에 데이터 쓰기
    # 'home.html'.index('.')
    # 'home.html'.strip('.')
    'home.html'.split('.')[0]+'.txt'
    desFile=open(filenames, mode='r', encoding='utf-8')
    desFile.write(data)
    desFile.close()

fileCopy1('./html/home.html')
filename='./html/home.html'
# # datas=filename.split('.')
# # print(f' data => {datas}, datas[0] => {datas[0]}')
# print(filename.split('.')[0])
print(f'.의 인덱스 => {filename.index(".")}')
print(f'.의 인덱스 오른쪽부터 => {filename.rindex(".")}')
print(f'확장자 제거 => {filename.rindex(".")}')

# ----

def fileCopy2(filenames):
    newFilenames=filenames[:filename.rindex('.')+'.txt']

    with open(filename, mode='r', encoding='utf-8') as srcFile:
        with open(newFilenames, mode='w', encoding='utf-8') as desFile:
            desFile.write(srcFile.read())

fileCopy2()