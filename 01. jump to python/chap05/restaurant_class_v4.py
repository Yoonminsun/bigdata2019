class MyRestaurant:
    restaurant_name=''
    cuisine_type=''
    number_served=0
    todays_customer=0
    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.f=open("./고객서빙현황로그.txt",'r')
        self.number_served = int(self.f.read())
        self.f.close()
        self.f=open("./고객서빙현황로그.txt", 'w')
    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 '%s'이고 '%s' 전문점입니다."%(self.restaurant_name,self.cuisine_type))
    def open_restaurant(self):
        print("\n저희 %s 레스토랑이 오픈했습니다.\n"%self.restaurant_name)
    def reset_number_served(self):
        self.todays_customer=0
        print("손님 카운팅을 0으로 초기화 하였습니다.\n")
    def increment_number_served(self,number):
        self.todays_customer += number
    def check_customer_number(self):
        print("당일 지금까지 총 %d명 손님께서 오셨습니다.\n"%(self.todays_customer))
    def __del__(self):
        self.number_served = self.number_served + self.todays_customer
        self.f.write(str(self.number_served))
        self.f.close()
        print("%s 레스토랑 문닫겠습니다.\n 이용해 주셔서 감사합니다." % self.restaurant_name)

open_yn = ''
menu = ''

name, type = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분): ").split()
my_restaurant = MyRestaurant(name,type)
my_restaurant.describe_restaurant()
open_yn = input("레스토랑을 오픈하시겠습니까?(y/n)")
if open_yn=='n':
    exit()
my_restaurant.open_restaurant()

while True:
    menu = input("어서오세요. 몇명이십니까?(초기화:0 입력, 종료:-1, 누적고객 확인:p): ")
    if menu=='-1':
        exit()
    elif menu=='0':
        my_restaurant.reset_number_served()
    elif menu=='p':
        my_restaurant.check_customer_number()
    else:
        my_restaurant.increment_number_served(int(menu))
        print("손님 %d명 들어오셨습니다. 자리를 안내해 드리겠습니다.\n"%int(menu))


