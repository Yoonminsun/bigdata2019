# 회귀선과 일변량 히스토그램을 포함한 산점도
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sns.set(color_codes=True)

# 쌍별 이변량 산점도 (Pairwise bivariate)
iris = sns.load_dataset("iris")
print(iris.head(100))
# sns.pairplot(iris)
sns.pairplot(iris,hue="species") # species 별로 색을 다르게 해서 나타내줌
plt.show()