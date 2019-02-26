# [참고사항]
# - API 호출수 25,000회/일로 제한
# - 한번 호출에 최대 100개 검색 (display_count)
# - 한번 실행에 최대 1000개 까지 기사 검색(index)
import urllib.request
import datetime
import json

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

def getNaverSearchResult(sNode,search_text,page_start,display,genre,country):
    base = 'https://openapi.naver.com/v1/search'
    node = '/%s.json'%sNode
    parameters = '?query=%s&start=%s&display=%s&genre=%s&country=%s'\
                 %(urllib.parse.quote(search_text),page_start,display,genre,country)
    url = base+node+parameters
    retData = get_request_url(url)

    if(retData == None):
        return None
    else:
        return json.loads(retData)

def getPostData(post,jsonResult):
    title = post['title']
    link = post['link']
    image = post['image']
    pubDate = post['pubDate']
    subtitle = post['subtitle']
    director = post['director']
    actor = post['actor']
    userRating = post['userRating']

    jsonResult.append({'title':title,'link':link,'image':image,'pubDate':pubDate,'subtitle':subtitle,'director':director,
                       'actor':actor,'userRating':userRating})
    return

def main(search_text,genre,country):
    jsonResult=[]
    sNode = 'movie'
    display_count = 100
    jsonSearch = getNaverSearchResult(sNode,search_text,1,display_count,genre,country)
    index=1
    while((jsonSearch!=None) and (jsonSearch['display']!=0) and index<10):
        for post in jsonSearch['items']:
            getPostData(post,jsonResult)

        nStart = jsonSearch['start']+jsonSearch['display']
        jsonSearch = getNaverSearchResult(sNode,search_text,nStart,display_count,genre,country)
        index = index+1

    with open('%s_naver_%s.json'%(search_text,sNode),'w',encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult,indent=4,sort_keys=True,ensure_ascii=False)
        outfile.write(retJson)

    print('%s_naver_%s.json SAVED'%(search_text,sNode))

if __name__ == '__main__':
    search_text = input('검색어 입력: ')
    search_genre = input('장르 코드 입력: ')
    search_country = input('국가 코드 입력: ')
    main(search_text,search_genre,search_country)