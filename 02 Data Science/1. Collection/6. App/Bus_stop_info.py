from urllib.request import Request,urlopen
from urllib.parse import quote_plus
import datetime
import json

Codejson=[]
access_key='oQSz2oLeE2%2FyKkC5Bvap%2ByKJ7NjXePjiinT9FimEL9PX9o0aEMHImBYj3NVIi9ArzQx4avj62hoXKqANLvj%2FcA%3D%3D'

def get_Request_URL(url):
    req = Request(url)

    try:
        response = urlopen(req)
        if response.getcode() == 200 :
            if __name__ == '__main__':
                print('[%s] Url Request Success'%datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print('[%s] Error for URL : %s'%(datetime.datetime.now(),url))
        return None

def get_Bus_stop_ID():
    end_point = 'http://openapi.tago.go.kr/openapi/service/BusSttnInfoInqireService/getSttnNoList?_type=json'
    parameters = '&serviceKey='+access_key
    parameters+= '&cityCode=%s'%get_cityCode()
    parameters+= '&nodeNm=%s'%quote_plus(stopName)
    url = end_point + parameters
    print(url)
    retData = get_Request_URL(url)
    if(retData == None):
        return None
    else:
        stop_json = json.loads(retData)
        if stop_json['response']['header']['resultMsg'] == 'NORMAL SERVICE.':
            return stop_json['response']['body']['items']['item']['nodeid']

def get_cityCode():
    global Codejson
    cityCode_url = 'http://openapi.tago.go.kr/openapi/service/ArvlInfoInqireService/getCtyCodeList?_type=json'
    parameters = '&ServiceKey=%s'%access_key
    cityCode_url = cityCode_url+parameters
    CodeData = get_Request_URL(cityCode_url)
    if (CodeData == None):
        return None
    else:
        Codejson = json.loads(CodeData)
        if Codejson['response']['header']['resultMsg'] == 'NORMAL SERVICE.':
            for prn_data in Codejson['response']['body']['items']['item']:
                if prn_data['cityname']==cityName:
                    return prn_data['citycode']

def get_arrive_info_URL():
    end_point = 'http://openapi.tago.go.kr/openapi/service/ArvlInfoInqireService/getSttnAcctoArvlPrearngeInfoList?_type=json'
    parameters = '&serviceKey=%s'%access_key
    parameters += '&cityCode=%s'%get_cityCode()
    parameters += '&nodeId=%s'%get_Bus_stop_ID()
    url = end_point + parameters
    retData = get_Request_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def Make_arrive_info_json():
    jsonData = get_arrive_info_URL()

    if ['response']['header']['resultMsg'] == 'NORMAL SERVICE.':
        prn_data = jsonData['response']['body']
        json_arrive_result.append({'routeid':prn_data['routeid'],'routeno':prn_data['routeno'],
                                   'arrprevstationcnt':prn_data['arrprevstationcnt'],
                                   'vehicletp':prn_data['vehicletp'],'arrtime':prn_data['arrtime']})

    return json_arrive_result

cityName = '대구광역시'
stopName = '대원유치원건너'
json_arrive_result=[]
if __name__ == '__main__':
    print(json_arrive_result)