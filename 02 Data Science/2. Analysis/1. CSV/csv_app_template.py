import csv
import math
import sys

input_file = 'Demographic_Statistics_By_Zip_Code.csv'
read = open(input_file,'r',newline='')
filereader = csv.reader(read)
value_list = list(filereader)
header_list = value_list[0]
value_list.remove(value_list[0])

def get_csv_row_instance(primary_key):
    Row_instance=[]
    for row_list in value_list:
        if row_list[0] == primary_key:
            Row_instance = row_list
    return Row_instance
def get_csv_col_instance(col_name):
    col_instance=[]
    index = header_list.index(col_name)
    for row_list in value_list:
        col_instance.append(row_list[index])
    return col_instance
def My_Sum(data_list):
    My_Sum=0
    data_list_int = Convert_Type(data_list)
    My_Sum = sum(data_list_int)
    return My_Sum
def My_Average(data_list):
    My_Average=0
    My_Average = My_Sum(data_list)/len(data_list)
    return My_Average
def My_Max(data_list):
    My_Max=0
    data_list_int = Convert_Type(data_list)
    My_Max = max(data_list_int)
    return My_Max
def My_Min(data_list):
    My_Min = 0
    data_list_int = Convert_Type(data_list)
    My_Min = min(data_list_int)
    return My_Min
def Convert_Type(data_list):
    data_list_int = []
    for data in data_list:
        data_list_int.append(int(data))
    return data_list_int
def My_Deviation(data_list,print_flag): # 편차
    My_Deviation_sum=0
    average = My_Average(data_list)
    data_list_int = Convert_Type(data_list)
    for data in data_list_int:
        if print_flag==0:
            print(data,data-average)
        My_Deviation_sum+=(data-average)**2
    return My_Deviation_sum
def My_Standard_Deviation(data_list):# 표준편차
    My_Standard_Deviation = 0
    My_Standard_Deviation = math.sqrt(My_Variance(data_list))
    return My_Standard_Deviation
def My_Variance(data_list): # 분산(Variance) 공식: ∑(표본-평균)**/표본수
    My_Variance=0
    deviation_sigma = My_Deviation(data_list,1)
    My_Variance = deviation_sigma/len(data_list)
    return My_Variance
def My_Ascendant(data_list):#오름차순
    data_list_int = Convert_Type(data_list)
    data_list_int.sort()
    for data in data_list_int:
        print(data,end=' ')
    print()
def My_Descendant(data_list):#내림차순
    data_list_int = Convert_Type(data_list)
    data_list_int.sort(reverse=True)
    for data in data_list_int:
        print(data, end=' ')
    print()
def print_col(column_list):
    for column in column_list:
        print(column)
# menu 처리
while True:
    print('<CSV Handle 연습예제>')
    print('0.종료 1.행 2.열 3.총합 4.평균 5.최대값 6.최소값 7.편차 8.분산 9.표준편차 10.오름차순 정렬 11. 내림차순 정렬')
    menu_num = int(input('메뉴를 선택하세요: '))
    if menu_num!=0:
        Access_Key = input('Access Key를 입력하세요: ')
    if menu_num==1: # 행출력
        row_list = get_csv_row_instance(Access_Key)
        print('행 데이터는 아래와 같습니다.')
        for row in row_list:
            print(row,end=' ')
        print()
    elif menu_num==2: # 열출력
        column_list = get_csv_col_instance(Access_Key)
        print_col(column_list)
    elif menu_num==3: # 총합
        column_list = get_csv_col_instance(Access_Key)
        print_col(column_list)
        print('총합:',My_Sum(column_list))
    elif menu_num==4: # 평균
        column_list = get_csv_col_instance(Access_Key)
        print_col(column_list)
        print('평균값:',My_Average(column_list))
    elif menu_num==5: # 최대값
        column_list = get_csv_col_instance(Access_Key)
        print_col(column_list)
        print('최대값:',My_Max(column_list))
    elif menu_num==6: # 최소값
        column_list = get_csv_col_instance(Access_Key)
        print_col(column_list)
        print('최소값:',My_Min(column_list))
    elif menu_num==7: # 편차
        print('편차(Deviation) 공식: 표본값 - 평균')
        print('표본  편차')
        column_list = get_csv_col_instance(Access_Key)
        My_Deviation(column_list,0)
    elif menu_num==8: # 분산
        column_list = get_csv_col_instance(Access_Key)
        print_col(column_list)
        print('분산(Variance) 공식: ∑(표본-평균)**2/표본수')
        print(My_Variance(column_list))
    elif menu_num==9: # 표준편차
        column_list = get_csv_col_instance(Access_Key)
        print_col(column_list)
        print('표준편차(Standard Deviation) 공식: √분산')
        print(My_Standard_Deviation(column_list))
    elif menu_num==10: # 오름차순 정렬
        column_list = get_csv_col_instance(Access_Key)
        My_Ascendant(column_list)
    elif menu_num==11: # 내림차순 정렬
        column_list = get_csv_col_instance(Access_Key)
        My_Descendant(column_list)
    elif menu_num==0: # 종료
        print('프로그램을 종료합니다.')
        exit()
    else:
        print('없는 메뉴 입니다.')



