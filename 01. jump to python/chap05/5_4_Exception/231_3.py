input_denominator = int(input("분모를 입력하세요:"))
try:
    f=open('foo.txt','r')
    result = 4/input_denominator
except Exception as e:
    print(e)
finally:
    print("Finally 블록 수행")
    f.close()
