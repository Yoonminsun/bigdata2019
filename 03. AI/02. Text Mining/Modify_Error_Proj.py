from konlpy.tag import Okt
from gensim.models import word2vec,FastText
import pandas as pd

kr = pd.read_csv('kr_korean.csv',header=None)
word_data = kr.iloc[:,0]
pos = kr.iloc[:,1]
word=[]
for i in range(len(word_data)):
    if pos[i]=='명사':
       word.append(word_data[i])

input_str = input('단어 입력: ')

try:
    model = word2vec.Word2Vec(sentences=word,size=100,window=5,min_count=2,workers=4,sg=0)
    print(model.wv.most_similar(input_str)) # 에러
except Exception:
    model = FastText(sentences=word,size=100,window=5,min_count=2,workers=4,sg=0)
    a = model.wv.most_similar(input_str)
    print(a) # 유사도 출력
    print('오타 수정:',a[0][0])
else:
    print('오타 없음')
