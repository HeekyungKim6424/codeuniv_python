#모각코 달콤한 파이썬 난이도 중
time=(input("24시 기준의 시간을 입력해주세요 (ex.15:24): ")).split(":")
hour=time.pop(0)

if int(hour)<=12: #오전인 경우
    time.insert(0,str(hour)) #리스트 요소를 원하는 자리에 추가하고 싶다면 insert요소를 사용하면 된다.인덱스,아이템 순으로 넣으면 됨
    new_time=":".join(time)
    print(new_time)
else:
    hour=int(hour)-12 #오후인 경우
    time.insert(0,str(hour))
    new_time=":".join(time)
    print(new_time)
#각 변수의 타입을 파악하고 코드를 짜자. 나누거나 합치는 옵션은 문자열만 해당이 된다.


