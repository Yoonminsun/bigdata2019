# pandas 문법을 이용해 헤더 추가하기
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

header_list = ['Supplier Name','Invoice Number','Part Number','Cost','Purchase Date']
data_frame = pd.read_csv(input_file,header=None,names=header_list)
data_frame.to_csv(output_file,index=False)