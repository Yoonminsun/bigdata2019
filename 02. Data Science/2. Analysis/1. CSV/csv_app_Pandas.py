import pandas as pd
import sys
import numpy as np

input_file = 'Demographic_Statistics_By_Zip_Code.csv'
data_frame = pd.read_csv(input_file,index_col=None)

def print_column(data_list):
    np_list = np.array(data_list)
    for data in data_list:
        print(data)
    return np_list
def My_Deviation(data_list):
    mean = data_frame.loc[:,Access_Key].mean()
    for data in data_list:
        print(data,data-mean)
while True:
    print('<CSV Handle Pandas 연습예제>')
    print('0.종료 1.행 2.열 3.총합 4.평균 5.최대값 6.최소값 7.편차 8.분산 9.표준편차 10.오름차순 정렬 11. 내림차순 정렬')
    menu_num = int(input('메뉴를 선택하세요: '))
    if menu_num!=0:
        Access_Key = input('Access Key를 입력하세요: ')
    if menu_num==1: # 행출력
        print('행 데이터는 아래와 같습니다.')
        index = int(data_frame[data_frame['JURISDICTION NAME']==int(Access_Key)].index.values)
        for data in data_frame.loc[index,]:
            if data%1==0:
                data= int(data)
            print(data,end=' ')
        print()
    elif menu_num==2: # 열출력
        print('열 데이터는 아래와 같습니다.')
        print_column(data_frame.loc[:,Access_Key])
    elif menu_num==3: # 총합
        # print(data_frame.loc[:,Access_Key])
        print_column(data_frame.loc[:, Access_Key])
        print('총합:',data_frame.loc[:,Access_Key].sum())
    elif menu_num==4: # 평균
        print_column(data_frame.loc[:, Access_Key])
        print('평균:',data_frame.loc[:,Access_Key].mean())
    elif menu_num==5: # 최대값
        print_column(data_frame.loc[:, Access_Key])
        print('최대값:',data_frame.loc[:,Access_Key].max())
    elif menu_num==6: # 최소값
        print_column(data_frame.loc[:, Access_Key])
        print('최소값:',data_frame.loc[:,Access_Key].min())
    elif menu_num==7: # 편차
        print('편차(Deviation) 공식 : 표본값 - 평균')
        print('표본  편차')
        My_Deviation(data_frame.loc[:,Access_Key])
    elif menu_num==8: # 분산 # 1865.1986498132708
        np_list = print_column(data_frame.loc[:, Access_Key])
        print('분산(Variance) 공식: ∑(표본-평균)**2/표본수')
        print('분산:',np.var(np_list))
    elif menu_num==9: # 표준편차 # 43.187945654004785
        np_list = print_column(data_frame.loc[:, Access_Key])
        print('표준편차(Standard Deviation) 공식: √분산')
        print('표준편차:',np.std(np_list))
    elif menu_num==10: # 오름차순 정렬
        print_column(data_frame.loc[:, Access_Key].sort_values())
    elif menu_num==11: # 내림차순 정렬
        print_column(data_frame.loc[:, Access_Key].sort_values(ascending=False))
    elif menu_num==0: # 종료
        print('프로그램을 종료합니다.')
        exit()
    else:
        print('없는 메뉴 입니다.')
