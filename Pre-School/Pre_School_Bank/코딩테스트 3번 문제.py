data=input('숫자열과 콤마로만 이루어진 문자열 123,42,98,18').replace(',','')

sum=0

for i in range(len(data)):
    sum += int(data[i])

print(f' 합 : {sum}')
print(f' 가장 큰 수 : {max(data)}')
print(f' 가장 작은 수 : {min(data)}')




