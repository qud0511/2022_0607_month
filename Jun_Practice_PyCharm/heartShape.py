import time as t

h='\u2661'

heart= f'''
   {h*3}      {h*3}
 {h}------{h} {h}------{h}
{h}{'-'*18}{h}
 {h}{'-'*16}{h}
  {h}{'-'*14}{h}
    {h}{'-'*10}{h}
      {h}{'-'*6}{h}
        {h}{'-'*2}{h}
          {h}
'''



score=int(input('-1 ~ 3'))


sh=heart.split('\n')  # splitheart

if score ==3:
    print(heart.replace('-','*'))

elif score ==2:
    heart.split('\n')
    for i in range(len(sh)):
        if i >= 4:
            sh[i]=sh[i].replace('-','*')
        print(sh[i])

elif score ==1:
    heart.split('\n')
    for i in range(len(sh)):
        if i >= 6:
            sh[i]=sh[i].replace('-','*')
        print(sh[i])

elif score ==0:
    heart.split('\n')
    for i in range(len(sh)):
        if i >= 8:
           sh[i]=sh[i].replace('-','*')
        print(sh[i])

elif score ==-1:
    print(heart)

shit='''
'''