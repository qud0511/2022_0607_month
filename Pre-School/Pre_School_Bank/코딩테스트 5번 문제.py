import calendar

season = int(input("좋아하는 월 입력 : "))

str_s_name = ""
if (season == 12 or season == 1 or season == 2):
    str_s_name = "Winter"
elif (season == 3 or season == 4 or season == 5):
    str_s_name = "Spring"
elif (season == 6 or season == 7 or season == 8):
    str_s_name = "Summer"
elif (season == 9 or season == 10 or season == 11):
    str_s_name = "Auturm"
else:
    str_s_name = "존재하지 않는 월입니다."

if season <= 12 and season >= 1 :
    print(calendar.month_name[season] + " ", end='')
print(str_s_name)

#-------------------

import calendar
mon = int(input("좋아하는 월 입력:"))

if mon < 1 or mon > 12:
    print("존재하지 않는 월입니다")
else:
    a = calendar.month_name[mon]

    if mon == 3 or mon == 4 or mon == 5:
        print(a, "Spring")
    elif mon == 6 or mon == 7 or mon == 8:
        print(a, "Summer")
    elif mon == 9 or mon == 10 or mon == 11:
        print(a, "Autumn")
    elif mon == 12 or mon == 1 or mon == 2:
        print(a, "Winter")


# -----------------------------------

month=["January, Winter", "Febraury, Winter", "March, Spring", "April, Spring", "May, Spring", "June, Summer", "July, Summer", "August, Summer", "September, Fall", "October, Fall", "November, Fall", "December, Winter"]
n = int(input("월을 입력하세요: "))
print(f"{n}월은 {month[n-1]}월 입니다.")