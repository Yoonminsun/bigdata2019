import urllib.request
from bs4 import BeautifulSoup
import re

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')
tags_list = ['순위,영화명,변동폭']
tags = soup.findAll('div',attrs={'class':'tit3'})
tags2 = soup.findAll(attrs={'class':'arrow'})
tags3 = soup.findAll(attrs={'class':'range ac'})

p1 = re.compile('.*>(.+)</a>.*')
p2 = re.compile('.+alt="(\w+)".*')
p3 = re.compile('.*ac">(\d).*')

for index in range(len(tags)):
    title = str(tags[index]).replace('\n', '')
    title = p1.sub('\g<1>',title)
    if title.find(',')!=-1:
        title = '"'+title+'"'
    change = p2.sub('\g<1>',str(tags2[index]))
    if change=='down':
        change = '-'+p3.sub('\g<1>',str(tags3[index]))
    elif change =='up':
        change = '+'+p3.sub('\g<1>',str(tags3[index]))
    else:
        change = p3.sub('\g<1>',str(tags3[index]))
    tags_list.append(str(index+1)+','+title+','+change)

for list in tags_list:
    print(list)

f = open('Naver_movie_ranking_re.csv','w')
f.write('\n'.join(tags_list))
f.close()