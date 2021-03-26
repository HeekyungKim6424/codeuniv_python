#모각코 달콤한 파이썬 난이도 중
print('''==========도형 목록==========
1. 원
2. 삼각형
3. 직사각형
4. 정사각형
============================''')

a=int(input("도형 목록에서 넓이를 계산할 도형의 번호를 입력해주세요: "))

if a == 1:
    b=int(input("원의 반지름 길이를 입력해주세요: "))
    area=(b**2)*3.14
    print("반지름의 길이가 {}인 원의 넓이는 약 {}입니다.".format(b,area))
elif a==2:
    b=int(input("삼각형의 밑변의 길이를 입력해주세요:"))
    c=int(input("삼각형의 높이를 입력해주세요: "))
    area=(b*c)/2
    print("밑변이 {}, 높이가 {}인 삼각형의 넓이는 {}입니다.".format(b,c,int(area)))
elif a==3:
    b=int(input("직사각형의 가로길이를 입력해주세요: "))
    c=int(input("직사각형의 세로길이를 입력해주세요: "))
    area=b*c
    print("가로길이가 {}, 세로길이가{}인 직사각영의 넓이는{}입니다.".format(b,c,int(area)))
else:
    b=int(input("정사각형 한변의 길이를 입력해주세요: "))
    area=b**2
    print("한변의 길이가{}인 정사각형의 넓이는 {}입니다.".format(b,int(area)))


#모각코 달콤한 파이썬 난이도 상

d=int(input("입력받을 숫자의 갯수를 입력해주세요: "))
f=[]
k=[]
m=[]
o=[]

for i in range(1,d+1):
    e=int(input("각 {}번째 숫자를 입력해주세요: ".format(i)))
    f.append(e)

for i in f:
    g=len(str(i))
    for j in range(0,g):
        h=i//(10**j)
        k.append(h)
    for j in k:
        l=j*(10**(g-1))
        g=g-1
        m.append(l)
    n=sum(m)
    for j in range(2,n+1):
        p=n%j
        o.append(p)
    if o.count(0)==1:
        print(i)

