# 목적: 그룹화, 히스토그램
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read the data set into a pandas DataFrame
wine = pd.read_csv('winequality-both.csv',sep=',',header=0)
wine.columns = wine.columns.str.replace(' ','_')

# Display descriptive statistics for quality by wine type
print("< 와인 종류에 따른 기술통계를 출력하기 >")
# 엑셀의 피벗테이블 효과
print(wine.groupby('type')[['alcohol']].describe().unstack('type'))

# Calculate specific quantiles
print("< 특정 사분위수 계산하기 >")
print(wine.groupby('type')[['quality']].quantile([0.25,0.75]).unstack('type'))

print("\n"+'='*80)
print("7.2.2 그룹화, 히스토그램, t 검정")
red_wine = wine.loc[wine['type']=='red','quality']
white_wine = wine.loc[wine['type']=='white','quality']

sns.set_style("dark")
print(sns.distplot(red_wine,norm_hist=True,kde=False,color="red",label="Red wine"))
print(sns.distplot(white_wine,norm_hist=True,kde=False,color="white",label="White wine"))

plt.xlabel("Quality Score")
plt.ylabel("Density")
plt.title("Distribution of Quality by Wine Type")
plt.legend()
plt.show()

# Test whether mean quality is different between red and white wines
print("\n와인의 종류에 따라 품질의 차이 검정")
print(wine.groupby(['type'])[['quality']].agg(['std','mean']))
tstat,pvalue,df = sm.stats.ttest_ind(red_wine,white_wine)
print('tstat: %.3f  pvalue: %.4f'%(tstat,pvalue))