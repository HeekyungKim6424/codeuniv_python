#모각코 달콤한 파이썬 난이도 중
time=int(input("초 단위의 시간을 입력해주세요: "))
hour=time//3600

if hour>0:
    min=(time-(hour*3600))//60
    if min>0:
        sec=time-(hour*3600)-(min*60)
        print("{}초: {}시간 {}분 {}초".format(time,hour,min,sec))
    else:
        sec=time-(hour*3600)
        print("{}초: {}시간 {}초".format(time,hour,sec))
else:
    min=time//60
    if min>0:
        sec=time-(min*60)
        print("{}초: {}분 {}초".format(time,min,sec))
    else:
        print("{}초: {}초".format(time,time))

#모각코 달콤한 파이썬 난이도 상
print("1. 10초    2. 30초    3. 1분    4. 10분    5.시작")
min=00
sec=00

while True:
    menu=int(input("원하는 시간의 숫자 버튼을 입력해주세요: "))
    
    if menu==1:
        sec=sec+10
        if sec>60:
            min=min+1
            sec=sec-60
        print(str(min)+":"+str(sec))
    elif menu==2:
        sec=sec+30
        if sec>60:
            min=min+1
            sec=sec-60
        print(str(min)+":"+str(sec))
    elif menu==3:
        min=min+1
        print(str(min)+":"+str(sec))
    elif menu==4:
        min=min+10
        print(str(min)+":"+str(sec))
    elif menu==5:
        print("전자레인지를 작동합니다")
        break
    else:
        print("잘못된 입력입니다.")

    
