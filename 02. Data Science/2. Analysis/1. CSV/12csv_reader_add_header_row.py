# 목적: 헤더 추가하기
import sys,csv

input_file = sys.argv[1]
output_file = sys.argv[2]

row_counter=0
with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file,delimiter=',')
        filewriter = csv.writer(csv_out_file,delimiter=',')
        header_list = ['Supplier Name','Invoice Number','Part Number','Cost','Purchase Date']
        filewriter.writerow(header_list)
        for row in filereader:
            filewriter.writerow(row)