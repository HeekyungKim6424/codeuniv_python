#달콤한 파이썬 난이도 중
a= int(input("숫자를 입력해주세요: "))
b=1

for i in range(1,a+1):
    b=i*b
    
print("{}!은 {}입니다.".format(a,b))


#달콤한 파이썬 난이도 상
c=input("숫자 두 개를 입력해주세요: ").split()
d=int(input("배수를 알고싶은 숫자를 입력해주세요: "))

if int(c[0])//d>0:
    e=int(c[0])//d
else:
    e=1
f=int(c[1])//d

for i in range(e,f+1):
    g=i*d
    print(g, end=" ")