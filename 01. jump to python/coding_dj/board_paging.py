m,n = map(int,input("입력(','구분): ").split(','))

result = m//n
if m%n>0:
    result+=1

print(result)