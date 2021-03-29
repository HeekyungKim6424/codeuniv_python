#모각코 달콤한 파이썬 난이도 중

class rectangle:
   
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def round(self):
        result1=(self.width*2)+(self.height*2)
        return result1
    def area(self):
        result2=self.width*self.height
        return result2 

width=int(input("가로: "))
height=int(input("높이: "))
a = rectangle(width, height)
print("직사각형의 둘레는{}이고, 넓이는{}입니다.".format(a.round(),a.area()))
