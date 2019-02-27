import urllib.request
from bs4 import BeautifulSoup
import re

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')
soup = str(soup)
tags_list = ['순위,영화명,변동폭']
p_title = re.compile(r'<a href="/.*" title="(.+)">\1</a>$',re.MULTILINE)
p_updown = re.compile('<td class="ac">.+ alt="([a-z]+)"',re.MULTILINE)
p_change = re.compile('<td class="range ac">(\d)',re.MULTILINE)

title_list = p_title.findall(soup)
updown_list = p_updown.findall(soup)
change_list = p_change.findall(soup)
for index in range(len(title_list)):
    if title_list[index].find(',')!=-1:
        title = '"'+title_list[index]+'"'
    else:
        title = title_list[index]
    if updown_list[index]=='up':
        change = '+'+change_list[index]
    elif updown_list[index]=='down':
        change = '-'+change_list[index]
    else:
        change = change_list[index]
    tags_list.append(str(index + 1) + ',' + title + ',' + change)

f = open('Naver_movie_ranking_re_2.csv','w')
f.write('\n'.join(tags_list))
f.close()