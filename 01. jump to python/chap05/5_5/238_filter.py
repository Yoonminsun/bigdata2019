# def positive(x):
#     return x>0
# f_result = filter(positive,[1,-3,2,0,-5,6])
# l_result = list(f_result)
# print(l_result)

print(list(filter(lambda x:x>0, [1,-3,2,0,-5,6])))