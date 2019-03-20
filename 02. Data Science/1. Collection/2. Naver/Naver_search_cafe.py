# [참고사항]
# - API 호출수 25,000회/일로 제한
# - 한번 호출에 최대 100개 검색 (display_count)
# - 한번 실행에 최대 1000개 까지 기사 검색(index)
import urllib.request
import datetime
import json
import re

app_id='iwG0jsok7VYtKG8sEglH' # ID입력
app_pw='b5Im0LMALv' # Password 입력

def get_request_url(url):
    req = urllib.request.Request(url)
    req.add_header('X-Naver-Client-Id',app_id)
    req.add_header('X-Naver-Client-Secret',app_pw)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print('[%s] Url:%s => Request Success'%(datetime.datetime.now(),url))
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print('[%s] Error for URL: %s'%(datetime.datetime.now(),url))
        return None

def getNaverSearchResult(sNode,search_text,page_start,display):
    base = 'https://openapi.naver.com/v1/search'
    node = '/%s.json'%sNode
    parameters = '?query=%s&start=%s&display=%s'%(urllib.parse.quote(search_text),page_start,display)
    url = base+node+parameters
    retData = get_request_url(url)

    if(retData == None):
        return None
    else:
        return json.loads(retData)

def getPostData(post,jsonResult):
    title = post['title']
    description = post['description']
    link = post['link']
    cafename = post['cafename']
    cafeurl = post['cafeurl']

    jsonResult.append({'cafename':cafename,'title':title,'description':description,'link':link,'cafeurl':cafeurl})
    return

def main(search_text):
    jsonResult=[]
    sNode = 'cafearticle'
    display_count = 100
    jsonSearch = getNaverSearchResult(sNode,search_text,1,display_count)
    index=1
    while((jsonSearch!=None) and (jsonSearch['display']!=0) and index<10):
        for post in jsonSearch['items']:
            getPostData(post,jsonResult)

        nStart = jsonSearch['start']+jsonSearch['display']
        jsonSearch = getNaverSearchResult(sNode,search_text,nStart,display_count)
        index = index+1

    with open('%s_naver_%s.json'%(search_text,sNode),'w',encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult,indent=4,sort_keys=True,ensure_ascii=False)
        outfile.write(retJson)

    print('%s_naver_%s.json SAVED'%(search_text,sNode))

if __name__ == '__main__':
    search_text = input('검색어 입력:')
    main(search_text)