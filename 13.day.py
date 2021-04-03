#모각코 달콤한 파이썬 난이도 상
word=input("단어를 입력해주세요: ")
list=[]
change_list=[]

for i in range(0,len(word)):
    a=word[i]
    list.append(a)
for i in range(1,len(word)+1):
    change_list.append(word[-i])

if list==change_list:
    print("회문입니다.")
else:
    print("회문이 아닙니다.")



