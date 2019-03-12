import MySQLdb
from xlrd import open_workbook
from xlwt import Workbook

input_file = 'Student_Info_DB_Scheme.xlsx'

con = MySQLdb.connect(host='localhost',port=3306,db='my_suppliers',user='open_source',passwd='1111',charset='utf8mb4')
c = con.cursor()

workbook = open_workbook(input_file)
worksheet = workbook.sheet_by_name('Sheet1')

delete_table = "delete from Students"
c.execute(delete_table)
con.commit()

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
rows=()
id_num=0

def DB_Insert():
    global rows,id_num
    data=[]
    for row in range(1, worksheet.nrows):
        for each in worksheet.row(row):
            data.append(each.value)
        c.execute("INSERT INTO Students VALUES ('%s', '%s', '%s', %s, '%s', '%s', '%s', '%s', '%s');"
                  %(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8]))
        data = []
    con.commit()
    c.execute("SELECT * FROM Students")
    rows = c.fetchall()
    id_num = int(rows[len(rows) - 1][0][3:]) + 1
def Print_Main_input():
    print('[ 메인 메뉴 ]')
    print('1. 요약 정보\n2. 입력\n3. 조회\n4. 수정\n5. 삭제\n6. 종료')
    menu = int(input('메뉴 입력: '))
    return menu
def Print_Search_input():
    print('< 조회 서브 메뉴 >')
    print('1. 개별 학생 조회\n2. 전체 학생 조회\n3. 상위 메뉴')
    menu = int(input('메뉴 입력: '))
    return menu
def Print_Search_each_input():
    print('< 검색 조건 >')
    print('1. ID\n2. 이름\n3. 나이\n4. 전공\n5. 컴퓨터 언어 명\n6. 컴퓨터 언어 레벨\n7. 상위메뉴')
    menu = int(input('메뉴 입력: '))
    return menu
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
    for row in rows:
        if row[2]=='남':
            total_male+=1
        elif row[2]=='여':
            total_female+=1
        if 20<=int(row[3])<30:
            total_20+=1
            list_20.append('%s:%s'%(row[1],int(row[3])))
        elif 30<=int(row[3])<40:
            total_30+=1
            list_30.append('%s:%s'%(row[1],int(row[3])))
        elif 40<=int(row[3])<50:
            total_40+=1
            list_40.append('%s:%s'%(row[1],int(row[3])))
        if '컴퓨터 공학' in row[4] or '통계' in row[4]:
            total_major+=1
        if row[5]:
            total_lang+=1
            if '파이썬' in row[5]:
                total_python+=1
            if row[6]:
                total_high+=1

    list_info = [len(rows),total_male,total_female,total_major,total_lang,total_high,total_python,
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
def Input_Student():
    global rows,id_num
    languages=[]
    high=[]
    middle=[]
    low=[]
    print('< 신규 학생 정보 입력 >')
    name = input('- 이름을 입력하세요(종료는 Enter 입력): ')
    if not name: return
    id = 'ITT{0:03d}'.format(id_num)
    id_num+=1
    sex = input('- 성별을 입력하세요: ')
    age = input('- 나이를 입력하세요: ')
    major = input('- 전공을 입력하세요: ')
    print('- 사용 가능한 컴퓨터 언어를 입력하세요.')
    while True:
        lang_name = input('  > 언어 이름(종료는 Enter 입력):')
        if not lang_name: break
        level = input('  > 수준(상,중,하): ')
        languages.append(lang_name)
        if level=='상':
            high.append(lang_name)
        elif level=='중':
            middle.append(lang_name)
        elif level=='하':
            low.append(lang_name)

    languages = ','.join(languages)
    high = ','.join(high)
    middle = ','.join(middle)
    low = ','.join(low)
    c.execute("INSERT INTO Students VALUES ('%s','%s','%s',%s,'%s','%s','%s','%s','%s')"
              % (id, name, sex, age, major,languages,high,middle,low))
    con.commit()
    c.execute("SELECT * FROM Students")
    rows = c.fetchall()
def Search_Student_Each(menu):
    search_str = input('검색어를 입력하세요: ')
    search_row=[]
    for row in rows:
        if menu==1 and row[0]==search_str:
            search_row.append(row)
        elif menu==2 and (search_str in row[1]):
            search_row.append(row)
        elif menu==3 and row[3]==int(search_str):
            search_row.append(row)
        elif menu==4 and (search_str in row[4]):
            search_row.append(row)
        elif menu==5 and (search_str in row[5]):
            search_row.append(row)
        elif menu==6:
            if search_str=='상' and row[6]:
                search_row.append(row)
            elif search_str=='중' and row[7]:
                search_row.append(row)
            elif search_str=='하' and row[8]:
                search_row.append(row)
    if len(search_row)>1:
        for row in search_row:
            print('- %s (%s, %d, %s)'%(row[0],row[1],int(row[3]),row[2]))
    elif len(search_row)==1:
        Search_Student_Print(search_row[0])
    else:
        print('* 검색 결과가 없습니다. *')
    return
def Search_Student_Print(row):
    print('* %s (%s)'%(row[0],row[1]))
    print('- 성별: %s'%row[2])
    print('- 나이: %d'%int(row[3]))
    print('- 전공: %s'%row[4])
    if not row[5]:
        print('- 사용 가능한 컴퓨터 언어: 없음')
    else:
        print('- 사용 가능한 컴퓨터 언어')
        languages = row[5].split(',')
        for lang in languages:
            print('  > %s '%lang,end='')
            if lang in row[6]:
                print('(Level: 상)')
            elif lang in row[7]:
                print('(Level: 중)')
            elif lang in row[8]:
                print('(Level: 하)')
def Update_Student():
    global rows
    update_student_ID = input('수정할 학생의 ID를 입력하세요: ')
    index = 5
    level=[]
    c.execute("SELECT * FROM Students WHERE ID='%s'" % update_student_ID)
    update_student = c.fetchall()[0]
    print('1. 이름: %s'%update_student[1])
    print('2. 성별: %s'%update_student[2])
    print('3. 나이: %d'%int(update_student[3]))
    print('4. 전공: %s'%update_student[4])
    if not update_student[5]:
        print('5. 사용가능한 컴퓨터 언어: 없음')
    else:
        print('사용 가능한 컴퓨터 언어')
        languages = update_student[5].split(',')
        for lang in languages:
            print('%d. %s'%(index,lang))
            print('%d. Level: '%(index+1),end='')
            if lang in update_student[6]:
                print('상')
                level.append(6)
            elif lang in update_student[7]:
                print('중')
                level.append(7)
            elif lang in update_student[8]:
                print('하')
                level.append(8)
            index+=2

    choice = int(input('수정할 항목의 번호를 입력하세요: '))
    modify = input('수정할 값을 입력하세요: ')

    if choice ==1:
        c.execute("UPDATE Students SET Name='%s' WHERE ID='%s'"%(modify,update_student_ID))
    elif choice ==2:
        c.execute("UPDATE Students SET Sex='%s' WHERE ID='%s'" % (modify, update_student_ID))
    elif choice ==3:
        c.execute("UPDATE Students SET Age=%s WHERE ID='%s'" % (modify, update_student_ID))
    elif choice ==4:
        c.execute("UPDATE Students SET Major='%s' WHERE ID='%s'" % (modify, update_student_ID))
    else:
        if (choice-5)%2==0:
            modify = str(update_student[5]).replace(languages[(choice-5)//2],modify)
            c.execute("UPDATE Students SET Languages='%s' WHERE ID='%s'"%(modify,update_student_ID))
        elif (choice-6)%2==0:
            index = (choice - 6) // 2
            modify_list1 = str(update_student[level[index]])
            print(modify_list1)
            # modify_list1.remove(languages[index])
            # print(modify_list1)
            # if modify=='상':
            # elif modify=='중':
            # elif modify=='하':



    con.commit()
    c.execute("SELECT * FROM Students")
    rows = c.fetchall()
    for row in rows:
        print(row)
DB_Insert()
menu = Print_Main_input()
while True:
    if menu==1:
        list_info, list_20, list_30, list_40 = Count_Student_Info()
        Print_Info(list_info, list_20, list_30, list_40)
        menu = Print_Main_input()
    elif menu==2:
        Input_Student()
        menu = Print_Main_input()
    elif menu==3:
        search_menu = Print_Search_input()
        if search_menu==1:
            each_menu = Print_Search_each_input()
            if each_menu==7:
                pass
            else:
                Search_Student_Each(each_menu)
        elif search_menu==2:
            print('< 전체 학생 데이터 >')
            for row in rows:
                Search_Student_Print(row)
                print()
        elif search_menu==3:
            menu = Print_Main_input()
    elif menu==4:
        Update_Student()
    elif menu==5:
        pass
    elif menu==6:
        print('학생 정보 분석 완료!')
        exit()