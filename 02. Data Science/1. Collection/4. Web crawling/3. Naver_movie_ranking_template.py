import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')
tags_list = ['순위,영화명,변동폭']
tags = soup.findAll('div',attrs={'class':'tit3'})
tags2 = soup.findAll(attrs={'class':'arrow'})
tags3 = soup.findAll(attrs={'class':'range ac'})

for index in range(len(tags)):
    if tags2[index]['alt']=='down':
        change = '-'+tags3[index].string
    elif tags2[index]['alt']=='up':
        change = '+'+tags3[index].string
    else:
        change = tags3[index].string
    title = tags[index].find('a').text
    if title.find(',')!=-1: # ','가 포함된 영화명은 ""으로 감싸서 넣어주면 csv에서 ','가 문자로 인식됨
        title = '"'+title+'"'
    tags_list.append(str(index+1)+','+title+','+change)

f = open('Naver_movie_ranking.csv','w')
f.write('\n'.join(tags_list))
f.close()