class MyRestaurant:
    restaurant_name='' # 레스토랑 명칭
    cuisine_type=''    # 레스토랑 종류
    total_price=0      # 오늘 총 매출
    total_sales=0      # 총 매출(매출.txt)
    # 생성자
    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.f=open("./%s 매출.txt"%self.cuisine_type,'r')
        self.total_sales = int(self.f.read())
        self.f.close()
        self.f=open("./%s 매출.txt"%self.cuisine_type,'w')
    # 소개
    def describe_restaurant(self):
        print("저희 %s 레스토랑 명칭은 '%s'입니다."%(self.cuisine_type,self.restaurant_name))
    # 오픈
    def open_restaurant(self):
        print("\n저희 %s 레스토랑이 오픈했습니다.\n"%self.restaurant_name)
    # 메뉴 주문
    def order_menu_list(self,menu_list):
        menu_name = list(menu_list.keys())
        menu_price = list(menu_list.values())
        for i in range(len(menu_list)):
            print(" %d. %s %s원 "%(i+1,menu_name[i],menu_price[i]),end='')
        print('')
        choice_menu = int(input("메뉴를 고르세요: "))-1
        if choice_menu>len(menu_list)-1:
            print("없는 메뉴입니다.")
        else:
            print("%s의 가격은 %s원 입니다. 감사합니다.\n"%(menu_name[choice_menu],menu_price[choice_menu]))
            self.total_price += menu_price[choice_menu]
    # 소멸자
    def __del__(self):
        self.total_sales = self.total_sales + self.total_price
        self.f.write(str(self.total_sales))
        print("%s 레스토랑 문닫겠습니다" % self.restaurant_name)

# 일식 레스토랑
class Japanese_Restaurant(MyRestaurant):
    menu_list = {'초밥':12000,'사케동':5000,'가츠동':4000,'다코야끼':3500,'우동':2500}
    def describe_restaurant(self):
        print("저희 일식 레스토랑 명칭은 '%s'입니다."%(self.restaurant_name))
# 중식 레스토랑
class Chinese_Restaurant(MyRestaurant):
    menu_list = {'짜장면':3500,'짬뽕':5500,'탕수육':8000,'깐풍기':9500}
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
    menu = input("어서오세요. 무엇을 도와드릴까요?\n(종료:-1/ 주문:order/ 주문가격확인:price/ 총매출확인:total): ")
    if menu=='-1':      # 종료
        exit()
    elif menu=='order': # 주문
        my_restaurant.order_menu_list(my_restaurant.menu_list)
    elif menu=='price': # 주문 가격 확인
         print("지금까지 총 가격은 %s원 입니다.\n"%my_restaurant.total_price)
    elif menu=='total': # 총 매출 확인
        print("어제까지 총 매출은 %s원 입니다.\n"%my_restaurant.total_sales)
    else:
          print("없는 메뉴입니다. 다시 선택하세요.")


