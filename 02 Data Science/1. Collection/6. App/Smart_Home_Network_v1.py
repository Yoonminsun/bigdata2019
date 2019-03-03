import Step5_Weather_Realtime_Info_for_student
import Air_Pollution_Info
import threading,time,ctypes
g_Radiator = False
g_Air_Conditioner = False
g_Gas_Valve = False
g_Balcony_Windows = False
g_Door = False
g_AI_Mode = False

json_list_weather=[]
json_list_air=[]
# xml, 웹크롤링(BeautifulSoup),웹크롤링(정규식) 각 1개씩 해보는 것도 좋음, 나머지는 json
def terminate_ai_mode(ai_scheduler):
    if not ai_scheduler.isAlive():
        return
    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(ai_scheduler.ident),exc)
    if res == 0:
        raise ValueError('nonexistent thread id')
    elif res>1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ai_scheduler.ident,None)
        raise SystemError('PyhreadState_SetAsyncExc failed')

def print_main_menu():
    print('\n1. 장비상태 확인')
    print('2. 장비제어')
    print('3. 스마트모드')
    print('4. 현재 미세먼지 확인')
    print('5. 프로그램 종료')

def print_device_status(device_name, device_status):
    print('%s 상태: '%device_name,end='')
    if device_status == True:print('작동')
    else: print('정지')

def check_device_status():
    print_device_status('난방기',g_Radiator) # 기온 5도 이하,10도 이상
    print_device_status('에어컨',g_Air_Conditioner)# 기온 30도 이상, 18도 이하
    print_device_status('가스밸브',g_Gas_Valve)
    print_device_status('발코니(베란다) 창문',g_Balcony_Windows) # 비,미세먼지,난방기,에어컨
    print_device_status('출입문 상태',g_Door)

def print_device_menu():
    print('\n상태 변경할 기기를 선택하세요.')
    print('1. 난방기')
    print('2. 에어컨')
    print('3. 가스밸브')
    print('4. 발코니(베란다) 창문')
    print('5. 출입문')

def control_device():
    global g_Radiator,g_Gas_Valve,g_Balcony_Windows,g_Door,g_Air_Conditioner

    check_device_status()
    print_device_menu()
    menu_num = int(input('번호를 입력하세요: '))

    if menu_num ==1: g_Radiator = not g_Radiator
    elif menu_num ==2: g_Air_Conditioner = not g_Air_Conditioner
    elif menu_num ==3: g_Gas_Valve = not g_Gas_Valve
    elif menu_num ==4: g_Balcony_Windows = not g_Balcony_Windows
    elif menu_num ==5: g_Door = not g_Door
    check_device_status()

def get_realtime_weather_info():
    global json_list_weather,json_list_air
    while True:
        if g_AI_Mode == False:
            break
        else:
            time.sleep(3)
            json_weather.get_Realtime_Weather_Info()
            json_list_weather = json_weather.json_weather_result
            json_list_air = json_air.Make_Air_Json()
            changed_status()

def smart_mode():
    global g_AI_Mode
    print('1. 인공지능 모드 조회')
    print('2. 인공지능 모드 상태 변경')
    print('3. 실시간 기상정보 Update')
    menu_num = int(input('메뉴를 선택하세요: '))

    if menu_num==1:
        print('현재 인공지능 모드:',end='')
        if g_AI_Mode == True: print('작동')
        else: print('중지')
    elif menu_num==2:
        ai_scheduler = threading.Thread(target=get_realtime_weather_info)
        g_AI_Mode = not g_AI_Mode
        print('현재 인공지능 모드:',end='')
        if g_AI_Mode == True:
            ai_scheduler.daemon = True
            ai_scheduler.start()
            print('인공지능 모드 작동')
        else:
            while ai_scheduler.is_alive():
                try:
                    terminate_ai_mode(ai_scheduler)
                except:
                    pass
            print('인공지능 모드 정지')
    elif menu_num==3:
        global json_list_weather,json_list_air
        json_weather.get_Realtime_Weather_Info()
        json_list_weather = json_weather.json_weather_result
        json_list_air = json_air.Make_Air_Json()[0]

def changed_status(): # 기준에 따라 기기 상태 바꾸는 함수 작성하기
    last_time = json_list_weather[0]['fcstTime']
    global g_Radiator,g_Balcony_Windows,g_Air_Conditioner
    for result in json_list_weather:
        if result['fcstTime'] == last_time and result['category']=='T1H': # 난방기,에어컨
            if result['fcstValue']<=5 and g_Radiator==False: # 기온 5도이하, 난방기 정지시 작동
                g_Radiator=True
                print('기온이 5도 이하 이므로 난방기를 작동합니다.')
            elif result['fcstValue']>=10 and g_Radiator==True: # 기온 10도 이상, 난방기 작동시 정지
                g_Radiator=False
                print('기온이 10도 이상이므로 난방기를 정지합니다.')
            if result['fcstValue']>=30 and g_Air_Conditioner==False: # 기온 30도 이상, 에어컨 정지시 작동
                g_Air_Conditioner=True
                print('기온이 30도 이상이므로 에어컨을 작동합니다.')
            elif result['fcstValue']<=18 and g_Air_Conditioner==True: # 기온 18도 이하, 에어컨 작동시 정지
                g_Air_Conditioner=False
                print('기온이 18도 이하이므로 에어컨을 정지합니다.')
        if g_Balcony_Windows==True:
            if result['fcstTime'] == last_time and result['category'] == 'RN1': # 창문
                if result['fcstValue']>0: # 비 예보가 있으면 창문 닫음
                    g_Balcony_Windows=False
                    print('곧 비 예보가 있으므로 창문을 닫습니다.')
                elif g_Radiator==True: # 난방기가 켜진 경우 창문 닫음
                    g_Balcony_Windows=False
                    print('난방기가 작동 중 이므로 창문을 닫습니다.')
                elif g_Air_Conditioner==True: # 에어컨이 켜진 경우 창문 닫음
                    g_Balcony_Windows=False
                    print('에어컨이 작동 중 이므로 창문을 닫습니다.')
            elif 81<=int(json_list_air[0]['pm10Value']) <= 150 or 51<=int(json_list_air[0]['pm25Value']) <= 100:
                g_Balcony_Windows = False
                print('미세먼지 등급이 "나쁨" 이므로 창문을 닫습니다.')
            elif int(json_list_air[0]['pm10Value']) >= 151 or int(json_list_air[0]['pm25Value']) >= 101:
                g_Balcony_Windows = False
                print('미세먼지 등급이 "매우나쁨" 이므로 창문을 닫습니다.')

def air_info_check():
    global json_list_air
    json_list_air = json_air.Make_Air_Json()[0]
    pm10 = int(json_list_air['pm10Value'])
    pm25 = int(json_list_air['pm25Value'])
    print('미세먼지 농도:%d(㎍/㎥) 초미세먼지 농도:%d(㎍/㎥)' % (pm10, pm25))
    if pm10<=30 or pm25<=15:
        print('미세먼지 예보 등급: 좋음')
    elif pm10<=80 or pm25<=50:
        print('미세먼지 예보 등급: 보통')
    elif pm10 <= 150 or pm25 <= 100:
        print('미세먼지 예보 등급: 나쁨')
    elif pm10>=151 or pm25>=101:
        print('미세먼지 예보 등급: 매우나쁨')


print('<스마트 홈네트워크 시뮬레이션 프로그램 ver 1.0>')
json_weather = Step5_Weather_Realtime_Info_for_student
json_weather.get_Realtime_Weather_Info()
json_list_weather = json_weather.json_weather_result
json_air = Air_Pollution_Info
json_list_air = json_air.Make_Air_Json()[0]
print(json_list_air)
while True:
    print_main_menu()
    try:
        menu_num = int(input('메뉴를 선택하세요: '))
    except:
        menu_num = int(input('메뉴를 다시 선택하세요: '))

    if menu_num==1:
        check_device_status()
    elif menu_num==2:
        control_device()
    elif menu_num==3:
        smart_mode()
    elif menu_num==4:
        air_info_check()
    elif menu_num==5:
        break