## 1000번 돌려서 평균값 내기
from sklearn import model_selection,svm,metrics
from sklearn.model_selection import train_test_split
import pandas as pd

all_data = pd.read_csv("./mnist/all_data.csv",header=None)
match_percent=[]
all_label = all_data.iloc[:,0]
all_images = all_data.iloc[:,1:]
indx=1
for index in range(len(all_images.columns)):
    apply_images = all_images.iloc[:,index]
    all_images[index] = apply_images.apply(lambda x:int(x)/256)
for num in range(1000):
    train_data, test_data, train_label, test_label = train_test_split(all_images,all_label,shuffle=True)
    clf = svm.SVC(gamma='auto')
    clf.fit(train_data,train_label)
    pre = clf.predict(test_data)
    ac_score = metrics.accuracy_score(test_label,pre)
    print("전체 데이터 수: %d"%(len(all_images)))
    print("학습 전용 데이터 수: %d"%(len(train_data)))
    print("테스트 데이터 수: %d"%(len(test_data)))
    print("%d. 정답률 = %.2f %%"%(indx,ac_score*100))
    match_percent.append(ac_score*100)
    indx+=1

match_sum = sum(match_percent)
print("1000번: %.2f %%"%(match_sum/1000))
