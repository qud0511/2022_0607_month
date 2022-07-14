# https://verificationkr.tistory.com/573

# --------------

def calculate_change(payment, cost):
    change = payment - cost

    fiftyCount = change // 50000
    tenCount = (change % 50000) // 10000
    five_count = (change % 10000) // 5000
    one_count = (change % 5000) // 1000

    print(f'50000원짜리 지폐 {fiftyCount}장.')
    print(f'10000원짜리 지폐 {tenCount}장.')
    print(f'5000원짜리 지폐 {five_count}장.')
    print(f'1000원짜리 지폐 {one_count}장.')

calculate_change(60000,14000)


# -------------------------------



# --------------------------

money=int(input('가지고 있는 금액'))
cost=int(input('제품 금액'))

change=money-cost

c50000= change // 50000
c10000= c50000 // 10000
c5000= c10000 // 5000
c1000= c5000 // 1000

print(f'50000원 지폐는 {c50000}장입니다.')
print(f'10000원 지폐는 {c10000}장입니다.')
print(f'5000원 지폐는 {c5000}장입니다.')
print(f'1000원 지폐는 {c1000}장입니다.')