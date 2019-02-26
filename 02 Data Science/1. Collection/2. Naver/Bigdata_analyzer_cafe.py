import json
import re

cafe_name_list=[]
cafe_name_dict = {}
cafe_name_set=()
news_count_sum=0
analysis_keyword = input('분석 키워드를 입력하세요: ')

try:
    with open('%s_naver_cafearticle.json'%analysis_keyword, encoding='UTF8')as json_file: json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    json_big_data = json.loads(json_string)
except FileNotFoundError:
    print('파일 없음')
    exit()

print('데이터 분석을 시작합니다.')
for in_cafe in json_big_data:
    cafe_name_list.append(in_cafe['cafename'])
    news_count_sum+=1
print(cafe_name_list)
cafe_name_set = set(cafe_name_list)
p = re.compile('http://cafe.naver.com/(\w+)')
for cafe_name in cafe_name_set:
    for cafe in json_big_data:
        if cafe_name == cafe['cafename']:
            cafe_url = p.sub('\g<1>',cafe['cafeurl'])
            cafe_name_dict[cafe_name_list.count(cafe_name)] = cafe_name+'('+cafe_url+')'

print('<네이버 검색 빅데이터 분석>')
print('검색어:%s\n전체 도메인 수:%s\n전체 건수:%s'%(analysis_keyword,len(cafe_name_set),news_count_sum))
print('\n- 카페 별 분석')
for count,cafe_name in sorted(cafe_name_dict.items(), reverse=True):
    print('>> %s: %s건'%(cafe_name,count))

print('분석을 완료합니다.')
