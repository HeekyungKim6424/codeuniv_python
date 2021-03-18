#달콤한 파이썬 난이도 중
a=float(input("숫자를 입력해 주세요: "))
b=a//1
c=(a-b)*10
if c>5:
    print("{0}".format(int(b+1)))
else:
    print("{0}".format(int(b)))

#달콤한 파이썬 난이도 상
d=input("각 숫자를 공백으로 입력해주세요: ").split()
d1=list(map(str, d))
max=0
for i in d1:
    n=len(i)
    sum=0
    for j in range(n):
        sum=sum+int(i[j])
    
    if sum>max:
        max=i
    else:
        continue

print(max)


    





    


