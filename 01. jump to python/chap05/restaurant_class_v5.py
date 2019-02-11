class MyRestaurant:
    restaurant_name=''
    cuisine_type=''
    number_served=0
    total_price=0
    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type
    def describe_restaurant(self):
        print("저희 %s 레스토랑 명칭은 '%s'입니다."%(self.cuisine_type,self.restaurant_name))
    def open_restaurant(self):
        print("\n저희 %s 레스토랑이 오픈했습니다.\n"%self.restaurant_name)
    def reset_number_served(self):
        self.number_served=0
        print("손님 카운팅을 0으로 초기화 하였습니다.\n")
    def increment_number_served(self,number):
        self.number_served += number
    def check_customer_number(self):
        print("지금까지 총 %d명 손님께서 오셨습니다.\n"%self.number_served)
    def order_menu_list(self,menu_list):
        menu_name = list(menu_list.keys())
        menu_price = list(menu_list.values())
        for i in range(len(menu_list)):
            print(" %d. %s %s원 "%(i+1,menu_name[i],menu_price[i]),end='')
        print('')
        choice_menu = int(input("메뉴를 고르세요(1~4): "))
        print("%s의 가격은 %s원 입니다. 감사합니다."%(menu_name[choice_menu-1],menu_price[choice_menu-1]))
        self.total_price += menu_price[choice_menu-1]
    def __del__(self):
        print("%s 레스토랑 문닫겠습니다" % self.restaurant_name)

class Japanese_Restaurant(MyRestaurant):
    # menu_list=['초밥 8000','사케동 5000','가츠동 4000','다코야끼 3500']
    menu_list = {'초밥':12000,'사케동':5000,'가츠동':4000,'다코야끼':3500}
    def describe_restaurant(self):
        print("저희 일식 레스토랑 명칭은 '%s'입니다."%(self.restaurant_name))

class Chinese_Restaurant(MyRestaurant):
    menu_list=['짜장면 3500','짬뽕 5500','탕수육 8000','깐풍기 9500']
    def describe_restaurant(self):
        print("저희 중식 레스토랑 명칭은 '%s'입니다."%(self.restaurant_name))

open_yn= ''
menu = ''

name, type = input("레스토랑 명칭과 종류를 선택하세요.(공백으로 구분): ").split()

if type=='일식':
    my_restaurant = Japanese_Restaurant(name,type)
elif type=='중식':
    my_restaurant = Chinese_Restaurant(name,type)
else:
    print("없는 레스토랑입니다.")
    exit()

my_restaurant.describe_restaurant()
open_yn= input("레스토랑을 오픈하시겠습니까?(y/n)")
if open_yn=='n':
    exit()
my_restaurant.open_restaurant()

while True:
    menu = input("어서오세요. 무엇을 도와드릴까요?(종료:-1,주문:order,가격확인:price): ")
    if menu=='-1':
        exit()
    elif menu=='order':
        my_restaurant.order_menu_list(my_restaurant.menu_list)
    elif menu=='price':
         print("지금까지 총 가격은 %s 입니다."%my_restaurant.total_price)
    else:
        my_restaurant.increment_number_served(int(menu))
        print("손님 %d명 들어오셨습니다. 자리를 안내해 드리겠습니다."%int(menu))


