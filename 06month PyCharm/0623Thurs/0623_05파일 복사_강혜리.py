# ------------------------------------------------------------------------
# [조건]
# - home.html 파일을 복사해서 home.txt 파일로 만들기
# - 함수명 : fileCopy
# - 매개변수 : 파일명
# - 반환값 : 없음
# ------------------------------------------------------------------------
def fileCopy(filename):
    print(f'filename = {filename}')
    #원본파일 열고 데이터 꺼내기
    srcFile=open(filename, mode='r', encoding='utf-8')
    data=srcFile.read()
    srcFile.close()

    #복사본 파일에 데이터 쓰기'
    filename=filename[:filename.rindex(".")] + '.txt'
    #split('.') 혹은 index('.')으로 . 앞글자 따오기
    print(f'filename = {filename}')
    desFile=open(filename, mode='w', encoding='utf-8')
    desFile.write(data)
    desFile.close()

fileCopy('./html/home.html')


#filename = 'home.html'
#datas = filename.split('.')
#print(f'datas = {data} ,datas[0] = {data[0]}')
#print(filename.split('.')[0])

def fileCopy2(filename):
    newFilename=filename[:filename.rindex(".")] + '.txt'
    with open(filename, mode='r',encoding='utf-8') as srcFile:
        with open(newFilename, mode='w' ,encoding='utf-8') as desFile:
            desFile.write(srcFile.read())