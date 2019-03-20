import urllib.request
from bs4 import BeautifulSoup
import re

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')
soup = str(soup)
tags_list = ['순위,영화명,변동폭']
p=re.compile(r'title="(.+)">\1</a>\n</div>\n</td>\n.+\n.+\n<td class="ac">.+alt="([a-z]+)".+\n<td class=.+(\d+)')
match_list = p.findall(soup)

for index in range(len(match_list)):
    if match_list[index][0].find(',')!=-1:
        title = '"'+match_list[index][0]+'"'
    else:
        title = match_list[index][0]
    if match_list[index][1]=='up':
        change = '+'+match_list[index][2]
    elif match_list[index][1]=='down':
        change = '-'+match_list[index][2]
    else:
        change = match_list[index][2]
    tags_list.append(str(index + 1) + ',' + title + ',' + change)

f = open('Naver_movie_ranking_re_3.csv','w')
f.write('\n'.join(tags_list))
f.close()