#달콤한 파이썬 난이도 중
a= int(input("삼각형의 높이를 입력하세요: "))
for i in range(1,a+1):
    if i==a:
        print('*'*i)
    else:
        print(' '*(a-i-1),'*'*i)

#달콤한 파이썬 난이도 상
print("  \t \t <3월 달력>")
print(" 일\t월\t화\t수\t목\t금\t토 ")
print("\t",end="")
for i in range(1,32):
    print(i,"\t",end="")
    if i%7==6:
        print("\n")
    else:
        continue
