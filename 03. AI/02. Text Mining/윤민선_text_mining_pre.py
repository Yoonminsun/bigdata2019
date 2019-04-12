# 데이터: http://blog.naver.com/PostView.nhn?blogId=samsjang&logNo=220982297456&redirect=Dlog&widgetTypeCall=true
# 책 : https://books.google.co.kr/books?id=RQM5DwAAQBAJ&pg=PA280&lpg=PA280&dq=term_counts+%3D+vectorizer.fit_transform(documents)&source=bl&ots=IxnFJwD_7i&sig=ACfU3U2YopyWcRvkX07A-C5gKa3XNgrhDQ&hl=ko&sa=X&ved=2ahUKEwiM1o7G3cnhAhUlCqYKHUGKDFEQ6AEwAHoECAkQAQ#v=onepage&q=term_counts%20%3D%20vectorizer.fit_transform(documents)&f=false
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

positive = '1\t'
negative = '0\t'
labels=[]
document=[]

with open('movie_review.txt','r',encoding='utf8') as file:
    for line in file:
        if line.startswith(positive):
           labels.append(1)
           document.append(line[len(positive):])
        elif line.startswith(negative):
            labels.append(0)
            document.append(line[len(negative):])

count_vector = CountVectorizer()
word_count = count_vector.fit_transform(document)
voca = count_vector.get_feature_names()

tf_trans = TfidfTransformer(use_idf=False).fit(word_count)
feature = tf_trans.transform(word_count)

with open('pre_movie_review.pickle','wb') as file:
    pickle.dump((labels,voca,feature),file)