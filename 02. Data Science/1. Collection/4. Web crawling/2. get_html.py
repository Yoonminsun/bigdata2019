import requests # 웹 페이지의 HTML을 가져오는 모듈
from bs4 import BeautifulSoup # HTML을 파싱하는 모듈

# 웹 페이지를 가져온 뒤 BeautifulSoup 객체로 만듦
response = requests.get('http://www.weather.go.kr/weather/observation/currentweather.jsp')
soup = BeautifulSoup(response.content,'html.parser')

# <table_class="table_develop3"을 찾음
table = soup.find('table',{'class':'table_develop3'})
data = [] # 데이터를 저장할 리스트 생성

def data_correction(org_text): # 데이터 보정작업
    if org_text == '\xa0':
        return 'N/A'
    return org_text

for tr in table.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds: # <td> 태그 리스트 반복(각 날씨 값을 가져옴)
        if td.find('a'):
            point = data_correction(td.find('a').text)
            cloud = data_correction(tds[1].text)
            visibility = data_correction(tds[2].text)
            temperature = data_correction(tds[5].text)
            wd_temp = data_correction(tds[7].text)
            humidity = data_correction(tds[10].text)
            wind_direction= data_correction(tds[11].text)
            wind_speed = data_correction(tds[12].text[16:19])
            data.append([point,cloud,visibility,temperature,wd_temp,humidity,wind_direction,wind_speed])
#
print('%8s%8s%8s%8s%8s%8s%8s%8s'%('지점','현재일기','시정(km)','현재 기온','체감 온도','습도(%)','풍향','풍속(m/s)'))
for dat in data:
    for index in range(len(dat)):
        print('%10s'%dat[index],end='')
    print()


