try:
    f=open("foo.txt",'r')
except FileNotFoundError as e:
    print(e)