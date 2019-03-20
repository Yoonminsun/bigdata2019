# 목적: pandas 문법으로 특정 열 선택하기 (인덱스 기준)
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame_column_by_index = data_frame.iloc[:,[0,3]]
data_frame_column_by_index.to_csv(output_file,index=False)
