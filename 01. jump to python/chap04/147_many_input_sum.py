def sum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

tu = list(map(int,input().split()))
# tu = tuple(tu)
print(tu)
print(sum(*tu))