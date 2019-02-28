for a in range(1,500):
    for b in range(a,500):
        for c in range(b,500):
            if (a*a+b*b==c*c) and a<b<c and a+b+c==1000:
                print(a*b*c)