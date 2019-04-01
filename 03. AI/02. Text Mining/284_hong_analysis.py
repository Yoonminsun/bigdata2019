from gensim.models import word2vec,FastText
model = word2vec.Word2Vec.load('hong.model')
print(model.wv.most_similar(positive=['대통령']))
## Word2Vec 모델은 오타를 허용하지 않는다, 에러발생
## 이러한 경우 FastText 모델을 사용하면 오타를 가지고도 유사도를 출력할 수 있다

