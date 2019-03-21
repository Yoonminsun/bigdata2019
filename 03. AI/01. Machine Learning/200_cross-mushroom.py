import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics,svm,model_selection
from sklearn.model_selection import train_test_split
from datetime import datetime
import time

start = datetime.fromtimestamp(time.time())
# 데이터 읽어 들이기
mr = pd.read_csv("mushroom.csv", header=None)
# 데이터 내부의 분류 변수 전개하기
label = []
data = []
attr_list = []
for row_index, row in mr.iterrows():
    label.append(row.ix[0])
    exdata = []
    for col, v in enumerate(row.ix[1:]):
        if row_index == 0:
            attr = {"dic": {}, "cnt":0}
            attr_list.append(attr)
        else:
            attr = attr_list[col]
        # 버섯의 특징 기호를 배열로 나타내기
        d = [0,0,0,0,0,0,0,0,0,0,0,0]
        if v in attr["dic"]:
            idx = attr["dic"][v]
        else:
            idx = attr["cnt"]
            attr["dic"][v] = idx
            attr["cnt"] += 1
        d[idx] = 1
        exdata += d
    data.append(exdata)
# 크로스 밸리데이션하기 --- (※3)
# clf = svm.SVC(gamma='auto') ## 0.84
clf = RandomForestClassifier() ## 0.92
scores = model_selection.cross_val_score(clf, data, label, cv=5)
print("각각의 정답률 =", scores)
print("평균 정답률 =", scores.mean())