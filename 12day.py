#모각코 달콤한 파이썬 난이도 중
while True:
    num=int(input("2부터 9사이 숫자를 입력해주세요(1을 누르면 프로그램이 종료됩니다.): "))

    if num==1:
        print("프로그램을 종료합니다.")
        break
    else:
        for i in range (1,10):
            print(num,"x",i,"=",num*i)
