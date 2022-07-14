# https://kmatter.tistory.com/entry/2%EC%A0%9C-%EC%B4%88%EA%B0%92%EC%9D%84-%EC%9E%85%EB%A0%A5%EB%B0%9B%EC%95%84-%EC%9D%BC-%EC%8B%9C-%EB%B6%84-%EC%B4%88%EB%A1%9C-%EB%82%98%EB%88%84%EC%96%B4-%EC%B6%9C%EB%A0%A5%ED%95%98%EB%8A%94-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8%EC%9D%84-%EC%9E%91%EC%84%B1%ED%95%98%EC%8B%9C%EC%98%A4

milsecond = int(input("밀리세컨드를 입력하세요: "))
second = milsecond//1000
print(f"밀리세컨드: {milsecond}")

hour = 60*60
minute = 60

hours = int(second//hour)

second %= hour
minutes = int(second//minute)

second %= minute

print("%d시-%d분-%d초입니다."%(hours, minutes, second))
