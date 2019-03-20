# 목적: pandas 문법으로 특정 열 선택하기 (헤더 이름 기준)
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame_column_by_name = data_frame.loc[:,['Invoice Number','Purchase Date']]
data_frame_column_by_name.to_csv(output_file,index=False)