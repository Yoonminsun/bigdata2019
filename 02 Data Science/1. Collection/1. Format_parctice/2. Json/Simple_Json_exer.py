import json
g_json_big_data=[]
with open('sample.json', encoding='UTF8')as json_file: json_object = json.load(json_file)
json_string = json.dumps(json_object)
json_big_data = json.loads(json_string)

print(json_big_data)
# print(json_big_data[0])
# print(json_big_data[0]['레벨 2-1 키'])
# print(json_big_data[1])
# print(json_big_data[1]['레벨 2-2 키'])
# print(json_big_data[1]['레벨 2-3 키'])
# print(json_big_data[1]['레벨 2-3 키']['레벨 3-1 키'])
# print(json_big_data[1]['레벨 2-3 키']['레벨 3-1 키'][0])
# print(json_big_data[1]['레벨 2-3 키']['레벨 3-1 키'][0]['레벨 4-1 키'])
# print(json_big_data[1]['레벨 2-3 키']['레벨 3-1 키'][0]['course_code'])

# 삽입
json_big_data.append({"레벨 2-4 키":"수박"})
print(json_big_data)
# 수정
json_big_data[0]['레벨 2-1 키'] = '체리'

# 삭제
del json_big_data[2]

# 자식 레벨 값 접근
print(json_big_data[1]['레벨 2-3 키']['레벨 3-1 키'][0]['course_code'])
# json_big_data[1]['레벨 2-2 키']['추가2'] = {}
# print(json_big_data)
print(json_big_data[1])
json_big_data[1]['추가2'] = {}
print(json_big_data[1])
# with open('sample_modify.json', 'w', encoding='utf8') as outfile:
#     readable_result = json.dumps(json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
#     outfile.write(readable_result)
#     print('ITT_Student.json SAVED')