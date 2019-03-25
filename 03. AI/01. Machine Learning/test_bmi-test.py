from sklearn import svm,metrics
from sklearn.model_selection import train_test_split
import pandas as pd

bmi_csv = pd.read_csv('bmi.csv')
w = bmi_csv['weight']/80
h = bmi_csv['height']/200
label = bmi_csv['label']
wh = pd.concat([w,h],axis=1)

train_data,test_data,train_label,test_label = train_test_split(wh,label)

svm_model = svm.SVC(gamma='auto')
svm_model.fit(train_data,train_label)
predicted = svm_model.predict(test_data)

print('정답률= %s %%'%(metrics.accuracy_score(test_label,predicted)))
print('리포트\n',metrics.classification_report(test_label,predicted))