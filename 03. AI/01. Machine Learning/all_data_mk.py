## train, test 를 하나로 합치는 코드
import pandas as pd

# *_2.csv는 공백줄 없이 저장한 csv
data = pd.read_csv("./mnist/train_2.csv",header=None)
test = pd.read_csv("./mnist/t10k_2.csv",header=None)

all_data = []
all_data.append(data)
all_data.append(test)
data_concat = pd.concat(all_data)
data_concat.to_csv('./mnist/all_data.csv',index=False,header=0)