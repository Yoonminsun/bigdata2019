import codecs
from konlpy.tag import Okt
from gensim.models import word2vec,FastText

fp = codecs.open("hong.txt",'r',encoding='utf-8')
text = fp.read()

okt = Okt()
lines = text.split('\r\n')

token_list=[]
for line in lines:
    token=[]
    malist = okt.pos(line,norm=True,stem=True)
    for word in malist:
        if not word[1] in ['Josa', 'Eomi', 'Punctuation']:
            token.append(word[0])
    if token:
        token_list.append(token)

# Word2Vec 과 FastText를 이용한 오타가 들어갔을 경우 차이
# 오타가 발생할 경우 고쳐주는 프로그램을 아래처럼 작성 가능
# 현재는 hong.txt 기준이지만 많은 단어 빅데이터를 이용하면 확장 가능

input_str = input('단어 입력: ')


try:
    model = word2vec.Word2Vec(sentences=token_list,size=100,window=5,min_count=2,workers=4,sg=0)
    print(model.wv.most_similar(input_str)) # 에러
except Exception:
    model = FastText(sentences=token_list,size=100,window=5,min_count=2,workers=4,sg=0)
    a = model.wv.most_similar(input_str)
    print(a) # 유사도 출력
    print('오타 수정:',a[0][0])
else:
    print('오타 없음')