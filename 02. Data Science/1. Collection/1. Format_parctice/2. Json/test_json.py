import json
with open('./ITT_Student.json',encoding='UTF8')as json_file:json_object = json.load(json_file)
json_string = json.dumps(json_object)
g_json_big_data = json.loads(json_string)

for i in range(len(g_json_big_data)):
    print('주소=',g_json_big_data[i]['address'])
    print('ID=',g_json_big_data[i]['student_ID'])
    print('나이=',g_json_big_data[i]['student_age'])
    print('이름=',g_json_big_data[i]['student_name'])
    in_total = g_json_big_data[i]['total_course_info']
    for j in in_total['learning_course_info']:
        print('개강일=', j['open_date'])
        print('강의 코드=', j['course_code'])
        print('강의명=', j['course_name'])
        print('강사명=',j['teacher'])
        print('종료 일=', j['close_date'])
    print('과거 수강 이력=',in_total['num_of_course_learned'],'\n')


# in_total = g_json_big_data[0]['total_course_info']
# for i in g_json_big_data[0]['total_course_info']:
#     print(in_total[i]) # value 출력
#     print(i) # key 출력
# print(in_total['learning_course_info']) # key에 해당하는 value출력
# print(in_total['learning_course_info'][0]) # len 만큼 for 돌려서 모든 수강 과목 정보 조회 가능할듯
# print(in_total['learning_course_info'][0]['close_date']) # 해당 인덱스 안의 딕셔너리에서 key값과 매칭해 value 출력
