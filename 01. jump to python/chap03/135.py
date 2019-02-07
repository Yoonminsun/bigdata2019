for i in range(2,10):
    for j in range(1,10):
       # print("%-3d"%(i*j),end=' ')
        print("{0:^3d}".format(i*j),end=' ')
    print('')
