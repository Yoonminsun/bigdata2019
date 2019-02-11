class HousePark: # 부모 클래스 (Super class)
    __last_name__ = '박'
    full_name=''
    def __init__(self,name):
        self.full_name = self.__last_name__ + name
    def travel(self,where):
        print("%s, %s여행을 가다."%(self.full_name,where))

class HouseKim(HousePark): # 자식클래스 (Child Class)
    __last_name__ = '김'
    def travel(self,where,day): # Method Overriding
        print("%s, %s여행 %d일 가다."%(self.full_name,where,day))


kitty = HouseKim('만복')
kitty.travel('제주',6)
