mul_n=0
n_break=0
n= int(input())
print(n)

while True:
    for i in str(n):
        if i!='1':
            n_break=1
            break
    if n_break==0:
        print(len(n))
        break
    n=n*n