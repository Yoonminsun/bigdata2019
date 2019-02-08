class HousePark:

    lastname = '박'
    def __init__(self,name):
        self.fullname = self.lastname+name
    def travel(self,where):
        print("%s, %s여행을 가다."%(self.fullname,where))

class HouseKim(HousePark):

    lastname = '김'
    def travel(self,where,day):
        print("%s, %s여행을 %d일 가다"%(self.fullname,where,day))

my = HousePark("응용")
print(my.lastname)
print(my.fullname)
my.travel("부산")

print('')
my2 = HouseKim("줄리엣")
print(my2.lastname)
print(my2.fullname)
my2.travel("독도",3)