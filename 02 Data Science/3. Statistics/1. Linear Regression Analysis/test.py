import pandas as pd
from statsmodels.formula.api import ols
import operator
from itertools import combinations

wine = pd.read_csv('winequality-both.csv',sep=',',header=0)
wine.columns = wine.columns.str.replace(' ','_')

dependent_value = wine['quality']
columns_list = ['fixed_acidity','volatile_acidity','citric_acid','residual_sugar','chlorides','free_sulfur_dioxide',
                'total_sulfur_dioxide','density','pH','sulphates','alcohol']

match_dic={}

for num in range(1,12):
    combi_list = list(combinations(columns_list,num))
    for tup in combi_list:
        my_formula = 'quality ~ '
        for data in tup:
            my_formula+='%s + '%data
        my_formula = my_formula.strip().rstrip('+')
        lm = ols(my_formula,data=wine).fit()
        print(lm.summary())
        independent_values_list = wine[list(tup)]
        y_predicted = lm.predict(independent_values_list)
        y_predicted_rounded = [round(score) for score in y_predicted]
        match_count=0
        for index in range(len(y_predicted_rounded)):
            if y_predicted_rounded[index]==dependent_value.values[index]:
                match_count+=1
        print('>> %s'%(my_formula.replace('quality ~ ','')))
        print('>> match count= %d'%match_count)
        print('>> 정답률: %.2f %%'%(match_count/len(y_predicted_rounded)*100))
        match_dic['%s'%my_formula.replace('quality ~ ','')] = match_count/len(y_predicted_rounded)*100

match_dic = sorted(match_dic.items(),key=operator.itemgetter(1),reverse=True)
print('총 조합 갯수: %d'%len(match_dic))
print('MAX 조합: %s >> %.2f %%'%(match_dic[0][0],match_dic[0][1]))
