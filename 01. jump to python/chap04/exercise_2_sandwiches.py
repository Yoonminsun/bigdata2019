def input_ingredient():
    choice_ingredient = []
    while True:
        in_choice = input('안녕하세요. 원하시는 재료를 입력하세요: ')
        if in_choice=='종료':
            return choice_ingredient
        else:
            choice_ingredient.append(in_choice)


def make_sandwiches(list_ingredient):
    if not list_ingredient: # 주문 없이 바로 종료한 경우
        print("재료가 없습니다.")

    else:
        print("샌드위치를 만들겠습니다.")
        for i in list_ingredient:
            print("%s 추가합니다."%i)
        print("여기 주문하신 샌드위치 만들었습니다. 맛있게 드세요.")

list_ingredient=[]

while True:
    menu = int(input("1.주문\n2.종료\n입력:"))

    if menu==1:
        list_ingredient.extend(input_ingredient()) # 추가로 주문할 경우를 위해 extend 사용

    elif menu==2:
        make_sandwiches(list_ingredient)
        break

    else:
        print("다시 입력하세요")