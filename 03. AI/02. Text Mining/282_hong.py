# pip install gensim
import codecs
from konlpy.tag import Okt
from gensim.models import word2vec,FastText # word2vec: 문장 내부의 단어를 벡터로 변환하는 도구
# utf-8 인코딩으로 파일을 열고 출력
fp = codecs.open("hong.txt",'r',encoding='utf-8')
text = fp.read()
# 텍스트를 한 줄씩 처리
okt = Okt()
results=[]
lines = text.split('\r\n')
for line in lines:
    # 형태소 분석, 단어의 기본형 사용
    malist = okt.pos(line,norm=True,stem=True)
    r=[]
    for word in malist:
        # 어미/조사/구두점 등은 대상에서 제외
        if not word[1] in ['Josa','Eomi','Punctuation']:
            r.append(word[0])
    rl = (' '.join(r)).strip()
    results.append(rl)
    # print(rl)

# 파일로 출력
# wakati_file = 'hong.wakati'
# with open(wakati_file,'w',encoding='utf-8') as fp:
#     fp.write('\n'.join(results))
# # Word2Vec 모델 만들기
# data = word2vec.LineSentence(wakati_file)
#
# # window: 중심 단어를 예측하기 위해 앞뒤로 각 몇개의 단어를 볼지 정하는 범위
# model = word2vec.Word2Vec(data,size=200,window=10,hs=1,min_count=2,sg=1)
# model.save('hong.model')

print('\n\n========== 분석 완료 ===========')

## Word2Vec 과 FastText 모델 차이를 알기 위한 Test 코드 부분
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

try:
    model = word2vec.Word2Vec(sentences=token_list,size=100,window=5,min_count=2,workers=4,sg=0)
    print(model.wv.most_similar('대통렁')) # 에러
except Exception:
    model = FastText(sentences=token_list,size=100,window=5,min_count=2,workers=4,sg=0)
    a = model.wv.most_similar('대통렁')
    print(a) # 유사도 출력
    print('오타 수정:',a[0][0])
else:
    print('오타 없음')
