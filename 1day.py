

#달콤한 파이썬 난이도 상
a=input("문장을 입력해 주세요: ").split(". ")
b=list(a)
for i in b:
    p=i[0]
    q=i[1:]
    print(p,q)

print(b)
