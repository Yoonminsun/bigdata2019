import MySQLdb
from xlrd import open_workbook
from xlwt import Workbook

input_file = 'Student_Info_DB_Scheme.xlsx'

con = MySQLdb.connect(host='localhost',port=3306,db='my_suppliers',user='open_source',passwd='1111',charset='utf8mb4')
c = con.cursor()

create_table = """CREATE TABLE IF NOT EXISTS Students
                  (ID VARCHAR(20),
                  Name VARCHAR(20),
                  Sex VARCHAR(10),
                  Age FLOAT,
                  Major VARCHAR(20),
                  Languages VARCHAR(40),
                  High VARCHAR(20),
                  Middle VARCHAR(20),
                  Low VARCHAR(20));"""
c.execute(create_table)
con.commit()

workbook = open_workbook(input_file)
worksheet = workbook.sheet_by_name('Sheet1')

def Print_Main_input():
    print('[ 메인 메뉴 ]')
    print('1. 요약 정보\n2. 입력\n3. 조회\n4. 수정\n5. 삭제\n6. 종료')
    menu = int(input('메뉴 입력: '))
    return menu

def DB_Insert():
    # for each in range(1,worksheet.nrows):
    #     print(worksheet.row(each))
    #     print('name: ',worksheet.row(each)[1].value)
        # print(worksheet.row(each)[6].ctype)
    data=[]
    for row in range(1,worksheet.nrows):
        for each in worksheet.row(row):
            if not each.value:
                data.append('없음')
            else:
                data.append(each.value)
        print(data)
        # (ID, Name, Sex, Age, Major, Languages, High, Middle, Low)
        query = """INSERT INTO Students VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        c.execute(query,data)
        data=[]
    con.commit()
    c.execute("SELECT * FROM Students")
    rows = c.fetchall()
    for row in rows:
        row_list_output = []
        for column_index in range(len(row)):
            row_list_output.append(str(row[column_index]))
        print(row_list_output)
    # c.execute("SELECT * FROM Students")
    # rows = c.fetchall()
    # for row in rows:
    #     row_list_output = []
    #     for column_index in range(len(row)):
    #         row_list_output.append(str(row[column_index]))
    #     print(row_list_output)
def Count_Student_Info():
    total_male = 0
    total_female = 0
    total_major = 0
    total_lang = 0
    total_high = 0
    total_python = 0
    total_20 = 0
    total_30 = 0
    total_40 = 0
    list_20=[]
    list_30=[]
    list_40=[]
    for row_index in range(1, worksheet.nrows):
            if worksheet.cell_value(row_index,2)=='남':
                total_male+=1
            elif worksheet.cell_value(row_index,2)=='여':
                total_female+=1
            if 20<=int(worksheet.cell_value(row_index,3))<30:
                total_20+=1
                list_20.append('%s:%s'%(worksheet.cell_value(row_index,1),int(worksheet.cell_value(row_index,3))))
            elif 30<=int(worksheet.cell_value(row_index,3))<40:
                total_30+=1
                list_30.append('%s:%s'%(worksheet.cell_value(row_index,1),int(worksheet.cell_value(row_index,3))))
            elif 40<=int(worksheet.cell_value(row_index,3))<50:
                total_40+=1
                list_40.append('%s:%s'%(worksheet.cell_value(row_index,1),int(worksheet.cell_value(row_index,3))))
            if worksheet.cell_value(row_index,4).find('컴퓨터 공학')!=-1 \
                    or worksheet.cell_value(row_index,4).find('통계')!=-1:
                total_major+=1
            if worksheet.cell_value(row_index,5):
                total_lang+=1
            if worksheet.cell_value(row_index,5).find('파이썬')!=-1:
                total_python+=1
            if worksheet.cell_value(row_index,6):
                total_high+=1
    list_info = [worksheet.nrows-1,total_male,total_female,total_major,total_lang,total_high,total_python,
                 total_20,total_30,total_40]
    return list_info,list_20,list_30,list_40

def Print_Info(list_info,list_20,list_30,list_40):
    print('< 요약 정보 >')
    print('* 전체 학생수: %d명'%list_info[0])
    print('* 성별')
    print('  - 남학생: %d명 (%.1f%%)'%(list_info[1],(list_info[1]/list_info[0])*100))
    print('  - 여학생: %d명 (%.1f%%)'%(list_info[2],(list_info[2]/list_info[0])*100))
    print('* 전공 여부')
    print('  - 전공자(컴퓨터 공학, 통계): %d명 (%.1f%%)'%(list_info[3],(list_info[3]/list_info[0])*100))
    print('  - 프로그래밍 언어 경험자: %d명 (%.1f%%)'%(list_info[4],(list_info[4]/list_info[0])*100))
    print('  - 프로그래밍 언어 상급자: %d명 (%.1f%%)'%(list_info[5],(list_info[5]/list_info[0])*100))
    print('  - 파이썬 경험자: %d명 (%.1f%%)'%(list_info[6],(list_info[6]/list_info[0])*100))
    print('* 연령대')
    print('  - 20대: %d명 (%.1f%%) '%(list_info[7],(list_info[7]/list_info[0])*100),end='')
    print(list_20)
    print('  - 30대: %d명 (%.1f%%) ' % (list_info[8], (list_info[8] / list_info[0]) * 100), end='')
    print(list_30)
    print('  - 40대: %d명 (%.1f%%) ' % (list_info[9], (list_info[9] / list_info[0]) * 100), end='')
    print(list_40)

DB_Insert()

# while True:
#     menu = Print_Main_input()
#     if menu==1:
#         list_info, list_20, list_30, list_40 = Count_Student_Info()
#         Print_Info(list_info, list_20, list_30, list_40)
#     elif menu==2:
#         pass
#     elif menu==3:
#         pass
#     elif menu==4:
#         pass
#     elif menu==5:
#         pass
#     elif menu==6:
#         print('학생 정보 분석 완료!')
#         exit()