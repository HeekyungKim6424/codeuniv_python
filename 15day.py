#모각코 달콤한 파이썬 난이도 중
month_dic={'1':31,'2':28,'3':31,'4':30,'5':31,'6':30,'7':31,'8':31,'9':30,'10':31,'11':30,'12':31}
month=input("월: ")
day=input("일: ")
cal_month=0

if int(month)==1:
    cal_month=0
else:
    for i in range(1,int(month)):
        cal_month=cal_month+month_dic['{}'.format(i)]
final_day=cal_month+int(day)

if final_day%7==0:
    print("{}월{}일은 목요일 입니다.".format(month,day))
elif final_day%7==1:
    print("{}월 {}일은 금요일 입니다.".format(month,day))
elif final_day%7==2:
    print("{}월 {}일은 토요일 입니다.".format(month,day))
elif final_day%7==3:
    print("{}월 {}일은 일요일 입니다.".format(month,day))
elif final_day%7==4:
    print("{}월 {}일은 월요일 입니다.".format(month,day))
elif final_day%7==5:
    print("{}월 {}일은 화요일 입니다.".format(month,day))
else:
    print("{}월 {}일은 수요일 입니다.".format(month,day))
#해당달은 뺴고 날짜만 더해야 하는데 달도 같이 계산해서 오류가 나왔었다.
#그리고 계속 변수타입 헷갈려서 오류났다. 조심하자.

