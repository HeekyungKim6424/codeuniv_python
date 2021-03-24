#모각코 달콤한 파이썬 난이도 중
a=input("OX퀴즈의 결과를 입력해주세요: ")
b=a.split("x")
d=0
f=[]
for i in range(1,len(a)+1):
    c=b.count("o"*i)
    d=sum(range(1,i+1))
    e=c*d
    f.append(e)

print(sum(f))

#모각코 달콤한 파이썬 난이도 상
h=[]

while True:
    g=input("")
    h.append(g)
    if h.index(g)==0:
         g=input("")
         h.append(g)
        
    else:
        if (h.index(g)+1)%5==0:
             print("(중간점검) 현재 {}개의 단어를 입력하셨습니다.".format(h.index(g)+1))

        if h[-2][-1]!=h[-1][0]:
            print("틀린단어를 입력하셨습니다. 게임을 종료합니다.")
            break

        if h[-1] in h[:-2]:
            print("틀린단어를 입력하셨습니다. 게임을 종료합니다.")
            break