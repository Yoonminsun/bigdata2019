import pandas as pd
import os
import numpy as np

df = pd.read_csv('movie_review.csv')
f = open('movie_review.txt','w',encoding='utf8')
for i in range(len(df['review'])):
    f.writelines('%s\t%s\n'%(df['sentiment'][i],df['review'][i]))

f.close()


