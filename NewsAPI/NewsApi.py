from urllib.request import Request,urlopen
from urllib.parse import quote_plus
import json
import time, datetime

access_key = '6c09faee-0d56-4ceb-aff3-9a33878a1369'

def get_Request_URL(url):
    req = Request(url)
    try:
        response = urlopen(req)
        if response.getcode() == 200:
            if __name__ == '__main__':
                print('[%s] Url Request Success'%datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print('[%s] Error for URL: %s'%(datetime.datetime.now(),url))
        return None

def get_News_URL():
    end_point = 'http://tools.kinds.or.kr:8888/time_line'
    parameters = ''
