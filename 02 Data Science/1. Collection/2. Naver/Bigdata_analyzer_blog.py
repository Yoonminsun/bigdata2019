import json
import re

domain_list=[]
domain_dict = {}
domain_set=()
name_list=[]
name_dict={}
name_set=()
news_count_sum=0
analysis_keyword = input('분석 키워드를 입력하세요: ')

try:
    with open('%s_naver_blog.json'%analysis_keyword, encoding='UTF8')as json_file: json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    json_big_data = json.loads(json_string)
except FileNotFoundError:
    print('파일 없음')
    exit()

print('데이터 분석을 시작합니다.')
p=re.compile('.+://\w+.\w+(?!/).?\w*(?!/).?\w*')
for in_blog in json_big_data:
    domain = p.search(in_blog['link'])
    domain_list.append(domain.group())
    name_list.append(in_blog['name'])
    news_count_sum+=1
domain_set = set(domain_list)
name_set = set(name_list)
for domain in domain_set:
    domain_dict[domain_list.count(domain)] = domain
p=re.compile('http://blog.naver.com/(\w+)')
for name in name_set:
    for blog in json_big_data:
        if blog['name'] == name:
            if p.search(blog['bloggerlink']):
                bloggerid = p.sub('\g<1>',blog['bloggerlink'])
                name_dict[name_list.count(name)]=name+'('+bloggerid+')'
            else:
                name_dict[name_list.count(name)] = name

print('<네이버 검색 빅데이터 분석>')
print('검색어:%s\n전체 도메인 수:%s\n전체 건수:%s'%(analysis_keyword,len(domain_set),news_count_sum))
print('\n- 도메인 별 분석')
for count,domain in sorted(domain_dict.items(), reverse=True):
    print('>> %s: %s건'%(domain,count))

print('\n- 블로거 이름 별 분석')
for count,name in sorted(name_dict.items(), reverse=True):
    print('>> %s : %s건'%(name,count))
print('분석을 완료합니다.')
