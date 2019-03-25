import pandas as pd
import sklearn.cluster, sklearn.preprocessing
from sklearn import metrics

alco = pd.read_csv('niaaa-report2009.csv',index_col='State')

columns = ['Wine','Beer']

kmeans = sklearn.cluster.KMeans(n_clusters=9)
kmeans.fit(alco[columns])
alco['Cluster'] = kmeans.labels_
alco.to_csv('Clustering_Result.csv',index=False)

data = alco[['Wine','Beer']]
label = alco['Cluster']

predicted = kmeans.predict(data)
print('예측결과\n',predicted)
ac_score = round(metrics.accuracy_score(label,predicted)*100,2)
print('정답률 = %s %%'%ac_score)
