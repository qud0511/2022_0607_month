weight=input('몸무게를 입력하시오. 예) 75')
height=input('키를 입력하시오. 예) 1.72')

weight=int(weight)
height=float(height)

bmi=weight/(height*height)
print(bmi)

if weight/(height*height) < 18.5:
    print('저체중')

elif weight/(height*height) <= 24.9:
    print('정상체중')

else:
    print('저체중')
print('='*40, ' The end ', '='*40 )