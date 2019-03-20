import pandas as pd
from sklearn import svm,metrics

xor_input = [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

and_input = [
    [0,0,0],
    [0,1,0],
    [1,0,0],
    [1,1,1]
]

or_input = [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,1]
]

nand_input = [
    [0,0,1],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

nor_input = [
    [0,0,1],
    [0,1,0],
    [1,0,0],
    [1,1,0]
]

# data_set = xor_input
data_set = and_input
# data_set = or_input
# data_set = nand_input
# data_set = nor_input

xor_df = pd.DataFrame(data_set)
# xor_data = xor_df.iloc[:,0:2]
xor_data = xor_df.loc[:,0:1]
xor_label = xor_df.iloc[:,2]

clf = svm.SVC()
clf.fit(xor_data,xor_label)
pre = clf.predict(xor_data)

ac_score = metrics.accuracy_score(xor_label,pre)
print("정답률 =",ac_score)