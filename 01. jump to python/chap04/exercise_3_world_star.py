def show_candidates(candidate_list):
    for i in candidate_list:
        print(i.rstrip())

def make_idol(candidate_list):
    for i in candidate_list:
        print("신예 아이돌 %s 인기 급상승"%i.rstrip())

def make_world_star(candidate_list):
    for i in candidate_list:
        print("아이돌 %s 월드스타 등극"%i.rstrip())


f = open("./연습생.txt",'r',encoding='UTF-8')
candidate_list = f.readlines()

show_candidates(candidate_list)
make_idol(candidate_list)
make_world_star(candidate_list)