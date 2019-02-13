import pickle
f = open('pickle_test.txt','wb')
# data = {1:'python',2:'you need'}
data = ['a','b','c']
pickle.dump(data,f)
f.close()

f = open('pickle_test.txt','rb')
result = pickle.load(f)
print(result)
print(result[1])