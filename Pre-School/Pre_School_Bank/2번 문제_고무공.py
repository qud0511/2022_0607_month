height = 100
i = 1
while i <= 10:
    height = height*3/5
    print(height)
    i=i+1

print('\n')

# ----------------------------


height = 100
bounce = 3 / 5

i = 1

while i <= 10:
    height = height * bounce
    print(i, round(height, 4))
    i = i + 1

print('\n')

# ----------------------------

h=100
for i in range(1,11):
	h = h*0.6
	print(h, i)