class MyRestaurant:
    restaurant_name=''
    cuisine_type=''
    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type
    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 '%s'이고 '%s' 전문점입니다."%(self.restaurant_name,self.cuisine_type))
    def open_restaurant(self):
        print("저희 %s 레스토랑이 오픈했습니다.\n"%self.restaurant_name)
    def __del__(self):
        print("%s 레스토랑 문닫겠습니다"%self.restaurant_name)

list =['first','second','third']

for i in range(3):
    name, type = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분): ").split()
    list[i] = MyRestaurant(name,type)
    list[i].describe_restaurant()
    list[i].open_restaurant()

print("저녁 10시가 되었습니다.\n")


