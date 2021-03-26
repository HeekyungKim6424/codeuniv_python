#달콤한 파이썬 난이도 중
a=input()
b=len(a)
c=set()

for i in range(0,b):
    c.add(a[i])
d=list(c)
d.sort()
print(d)

#달콤한 파이썬 난이도 상
print('''======음료수 목록======
물               700원
콜라            1000원
사이다          1000원
과일주스        800원
======================''')

money=int(input("소지하고 있는 돈의 액수를 입력해주세요: "))
drink=input("마시고 싶은 음료를 입력하세요: ")

dic_drink={"물":700,"콜라":1000,"사이다":1000,"과일주스":800}
count_drink={"물":3,"콜라":2,"사이다":1,"과일주스":2}

rest_money=money-dic_drink[drink]
rest_count=count_drink[drink]-1

if rest_money>0:
    print('''{}의 가격은 {}원입니다.
    주문이 완료되었습니다.
    잔액은 {}원 입니다.'''.format(drink,dic_drink[drink],rest_money))
else:
    print('''{}의 가격은 {}원 입니다.
    돈이 부족합니다.'''.format(drink,dic_drink[drink]))

    
if rest_count<0:
     print('''{}의 가격은{}원 입니다.
    현재 해당 음료는 품절 상태 입니다.'''.format(drink,dic_drink[drink]))

while True:
    drink=input("마시고 싶은 음료를 입력하세요: ")

    rest_money=rest_money-dic_drink[drink]
    rest_count=count_drink[drink]-1
    
    if rest_money>0:
        print('''{}의 가격은 {}원입니다.
        주문이 완료되었습니다.
        잔액은 {}원 입니다.'''.format(drink,dic_drink[drink],rest_money))
    else:
        print('''{}의 가격은 {}원 입니다.
        돈이 부족합니다.'''.format(drink,dic_drink[drink]))
        break
    
    if rest_count<0:
        print('''{}의 가격은{}원 입니다.
        현재 해당 음료는 품절 상태 입니다.'''.format(drink,dic_drink[drink]))
        break