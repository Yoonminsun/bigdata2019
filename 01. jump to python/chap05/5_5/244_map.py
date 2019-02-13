def two_times(x): return x*2 # map_result,list_result 에 필요

# print(map(two_times,[1,2,3,4])) # map_result
# print(list(map(two_times,[1,2,3,4]))) # list_result

print(list(map(lambda x:x*2,[1,2,3,4]))) # lambda_result ,p245
