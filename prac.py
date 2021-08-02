"""a=int(input())
b=input()
c=["S","M","U","P","C"]
d="".join(b)
for i in b:
    for j in c:
        b=d.split(j)

print(b)"""

'''a=input().split(" ")
b=input().split(" ")
c=0
j=0
for i in range(0,int(a[1])):
    if int(a[0])<j:
        print(c)
        break
    if len(b)<=3:
        j=j+1
        c=c+int(b[j])    
    else:
        if i==0:
            j=j+1
            c=(c//2)+int(b[j])
        elif i<3:
            j=j+2
            c=(c//2)+int(b[j])
        else:
            j=j+1
            c=c+int(b[j])    
print(c)'''

'''a=input().split(" ")
d=[]
for i in range(0,a[0]):
    line=[]
    b=input()
    c=line.append(b)
    if "P" in b:
        d.append(b.index("P"))'''




