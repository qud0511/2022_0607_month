import operator

a_dic = {"마징가":[187.5, 91], "베트맨":[174.9, 102.3], "홍길동":[192, 72], "가가멜":[167.2, 89.3]}

sorted_a_dic=sorted(a_dic.items(), key=operator.itemgetter(1))

print(sorted_a_dic)