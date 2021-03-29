#모각코 달콤한 파이썬 난이도 중
n=int(input("숫자를 입력해주세요: "))
k=int(input("몇번째 약수를 알고 싶은지 입력하세요: "))
a=[]

for i in range(1,n+1):
    if n%i==0:
        a.append(i)

if len(a)<k:
    print("입력하신 숫자만큼의 약수가 존재하지 않습니다.")

print("{}의 {}번째 약수는 {}입니다.".format(n,k,a[k-1]))

#모각코 달콤한 파이썬 난이도 상
num_of_subject=int(input("총 과목의 수를 입력하세요: "))
b=[]

for i in range(1,num_of_subject+1):
    score=int(input("점수를 입력해주세요"))
    b.append(score)
    
    if score<=100 and score>=90:
        print("해당 과목 등급: A")
    elif score<90 and score>=80:
        print("해당 과목 등급: B")
    elif score<80 and score>=70:
        print("해당 과목 등급: C")
    elif score<70 and score>=60:
        print("해당 과목 등급: D")
    else:
        print("해당 과목 등급: F")

sum_of_sbject=sum(b)
print("총 과목의 평균은 {}입니다.".format(sum_of_sbject/num_of_subject))
    
