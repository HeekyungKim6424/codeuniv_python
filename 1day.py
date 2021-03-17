#달콤한 파이썬 난이도 중
a=input("문장을 입력해 주세요: ").split()
b=set(a)
b1=list(b)
b1.sort()
print(b1)

#달콤한 파이썬 난이도 상
a=input("문장을 입력해 주세요: ").split(". ")
b=list(a)
for i in b:
    p=i[0]
    q=i[1:]
    p.capitalize()
    q.lower()
    i=p+q
    
    for j in i:
        if j=="i"
            b.replace("i","I") 

print(b)
