import Step5_Weather_Realtime_Info_for_student
import threading,time,ctypes
g_Radiator = False
g_Gas_Valve = False
g_Balcony_Windows = False
g_Door = False
g_AI_Mode = False
json_list=[]
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
    print('4. 프로그램 종료')

def print_device_status(device_name, device_status):
    print('%s 상태: '%device_name,end='')
    if device_status == True:print('작동')
    else: print('정지')

def check_device_status():
    print_device_status('난방기',g_Radiator)
    print_device_status('가스밸브',g_Gas_Valve)
    print_device_status('발코니(베란다) 창문',g_Balcony_Windows)
    print_device_status('출입문 상태',g_Door)

def print_device_menu():
    print('\n상태 변경할 기기를 선택하세요.')
    print('1. 난방기')
    print('2. 가스밸브')
    print('3. 발코니(베란다) 창문')
    print('4. 출입문')

def control_device():
    global g_Radiator,g_Gas_Valve,g_Balcony_Windows,g_Door

    check_device_status()
    print_device_menu()
    menu_num = int(input('번호를 입력하세요: '))

    if menu_num ==1: g_Radiator = not g_Radiator
    elif menu_num ==2: g_Gas_Valve = not g_Gas_Valve
    elif menu_num ==3: g_Balcony_Windows = not g_Balcony_Windows
    elif menu_num ==4: g_Door = not g_Door
    check_device_status()

def get_realtime_weather_info():
    global json_list
    while True:
        if g_AI_Mode == False:
            continue
        else:
            time.sleep(3600)
            json_weather.get_Realtime_Weather_Info()
            json_list = json_weather.json_weather_result

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
        ai_scheduler.daemon = True
        g_AI_Mode = not g_AI_Mode
        print('현재 인공지능 모드:',end='')
        if g_AI_Mode == True:

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
        json_weather.get_Realtime_Weather_Info()
        json_list = json_weather.json_weather_result

def changed_status(): # 기준에 따라 기기 상태 바꾸는 함수 작성하기
    pass

print('<스마트 홈네트워크 시뮬레이션 프로그램 ver 1.0>')

while True:
    json_weather = Step5_Weather_Realtime_Info_for_student
    json_weather.get_Realtime_Weather_Info()
    json_list = json_weather.json_weather_result

    print_main_menu()
    menu_num = int(input('메뉴를 선택하세요: '))

    if menu_num==1:
        check_device_status()
    elif menu_num==2:
        control_device()
    elif menu_num==3:
        smart_mode()
    elif menu_num==4:
        break