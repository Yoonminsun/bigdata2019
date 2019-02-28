import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')
tags_list = ['순위,영화명,변동폭']
rank=1
title=''
up_down=''
change=''
tags = soup.find('table',attrs={'class':'list_ranking'})
for tag in tags.find_all('tr'):
    up_down_list = tag.find_all('img')
    if tag.find('a') and tag.find_all('td',attrs={'class':'range ac'}) and up_down_list:
        title = tag.find('a').string
        if title.find(',')!=-1:
            title = '"'+title+'"'
        if tag.find_all('td',attrs={'class':'range ac'}):
            change = tag.find_all('td',attrs={'class':'range ac'})[0].string
        if up_down_list:
            up_down = up_down_list[1].get('alt')
            if up_down=='up':
                change = '+'+change
            elif up_down=='down':
                change = '-'+change
        tags_list.append(str(rank)+','+title+','+change)
        rank+=1
print(tags_list)
f = open('Naver_movie_ranking_test.csv','w')
f.write('\n'.join(tags_list))
f.close()