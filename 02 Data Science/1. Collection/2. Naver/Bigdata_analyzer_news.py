import json
import re

domain_list=[]
domain_dict = {}
domain_set=()
news_count_sum=0
inaccuracy_data=0
analysis_keyword = input('분석 키워드를 입력하세요: ')

try:
    with open('%s_naver_news.json'%analysis_keyword, encoding='UTF8')as json_file: json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    json_big_data = json.loads(json_string)
except FileNotFoundError:
    print('파일 없음')
    exit()

print('데이터 분석을 시작합니다.')
p=re.compile('.+://\w+.\w+(?!/).?\w*(?!/).?\w*')
for in_news in json_big_data:
    if not in_news['org_link']:
        inaccuracy_data+=1
        print('org_link가 없는 기사를 발견했습니다.')
    else:
        domain = p.search(in_news['org_link'])
        domain_list.append(domain.group())
        news_count_sum+=1
domain_set = set(domain_list)
for domain in domain_set:
    domain_dict[domain_list.count(domain)] = domain

print('<네이버 검색 빅데이터 분석>')
print('검색어:%s\n전체 도메인 수:%s\n전체 건수:%s\n부정확한 데이터 수:%s'%(analysis_keyword,len(domain_set),news_count_sum,inaccuracy_data))
print('\n- 도메인 별 뉴스 기사 분석')
for count,domain in sorted(domain_dict.items(), reverse=True):
    print('>> %s: %s건'%(domain,count))

print('분석을 완료합니다.')
