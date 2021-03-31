#모각코 달콤한 파이썬 난이도 중
a=input()

if len(a)%2==0:
    print("{}".format(a[(len(a)//2)-1:(len(a)//2)+1]))
else:
    print("{}".format(a[(len(a)//2)]))

#모각코 달콤한 파이썬 난이도 상
import random
user=input("가위바위보 게임입니다.무엇을 낼지 입력해주세요: ")
n = random.randint(1, 3)
def choice_of_computer(n):
    if n==1:
        com="가위"
        print("컴퓨터: {}".format(com))
        return com
    elif n==2:
        com="바위"
        print("컴퓨터: {}".format(com))
        return com
    else:
        com="보"
        print("컴퓨터: {}".format(com))
        return com

def game(user,choice_of_computer):
    com=choice_of_computer
    if user==com:
        print("비겼습니다.")
    elif user=="가위":
        if com=="바위":
            print("컴퓨터가 이겼습니다.")
        else:
            print("당신이 이겼습니다.")
    elif user=="바위":
        if com=="가위":
            print("당신이 이겼습니다.")
        else:
            print("컴퓨터가 이겼습니다.")
    else:
        if com=="가위":
            print("컴퓨터가 이겼습니다.")
        else:
            print("당신이 이겼습니다.")

choice_of_computer(n)
game(user,choice_of_computer)