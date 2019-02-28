import urllib.request
import datetime
import json
import time

access_key='oQSz2oLeE2%2FyKkC5Bvap%2ByKJ7NjXePjiinT9FimEL9PX9o0aEMHImBYj3NVIi9ArzQx4avj62hoXKqANLvj%2FcA%3D%3D'

def get_Request_URL(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print('[%s] Url Request Success'%datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print('[%s] Error for URL : %s'%(datetime.datetime.now(),url))
        return None

def get_Weather_URL(day_time):
    end_point = 'http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData'
    parameters = '?_type=json&serviceKey='+access_key
    parameters+= '&base_date='+yyyymmdd
    parameters+= '&base_time='+day_time
    parameters+= '&nx='+x_coodinate
    parameters+= '&ny='+y_coodinate
    parameters+= '&numOfRows=100'

    url = end_point + parameters
    retData = get_Request_URL(url)
    if(retData == None):
        return None
    else:
        return json.loads(retData)

def Make_Weather_Json(day_time):
    jsonData = get_Weather_URL(day_time)

    if(jsonData['response']['header']['resultMsg'] == 'OK'):
        for prn_data in jsonData['response']['body']['items']['item']:
            json_weather_result.append({'baseDate':prn_data.get('baseDate'),'baseTime':prn_data.get('baseTime'),
                                        'category':prn_data.get('category'),'fcstDate':prn_data.get('fcstDate'),
                                        'fcstTime':prn_data.get('fcstTime'),'fcstValue':prn_data.get('fcstValue'),
                                        'nx':prn_data.get('nx'),'ny':prn_data.get('ny')})
    with open('동구_신암동_초단기예보조회_%s%s.json'%(yyyymmdd,day_time),'w',encoding='utf8') as outfile:
        retJson = json.dumps(json_weather_result, indent=4, sort_keys=True,ensure_ascii=False)
        outfile.write(retJson)
    print('동구_신암동_초단기예보조회_%s_%s.json SAVED\n'%(yyyymmdd,day_time))

def get_Realtime_Weather_Info():
    day_min_int=int(day_min)
    if 30 < day_min_int <=59:
        day_time = time.strftime("%H%M",time.localtime(time.time()))
        print('\n<<실시간 기상정보 업데이트를 실시합니다!!>>\n'.center(30))
        Make_Weather_Json(day_time)
    elif 0<=day_min_int<=30:
            day_hour_int = int(day_hour)
            day_hour_int = day_hour_int -1
            revised_min = 60+(day_min_int-30)
            day_time = '{0:0>2}'.format(day_hour_int)+str(revised_min)
            print('\n<<가장 최신 기상정보 업데이트를 실시합니다!!>>\n'.center(30))
            Make_Weather_Json(day_time)
    return day_min_int

json_weather_result=[]
yyyymmdd = time.strftime("%Y%m%d")
day_time = time.strftime("%H%M")
day_hour = time.strftime("%H")
day_min = time.strftime("%M")
x_coodinate = "89"
y_coodinate = "91"

if __name__ == '__main__':
    get_Realtime_Weather_Info()
    print(json_weather_result)