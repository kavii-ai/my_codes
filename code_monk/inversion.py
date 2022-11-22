t = int(input().strip())

while t > 0:
    matsize = int(input().strip())
    ar = [None]*matsize
    ind = 0
    #creating the 2D array via reading the input
    while matsize > 0:
        ar[ind]= list(map(int,input().split()))
        ind += 1
        matsize -= 1

    #reinitialising the matsize
    matsize = ind
    #operations on the 2d array read from input
    #four nested for loops
    res = 0
    for i in range(0, matsize):  
        for j in range(0,matsize):
            for p in range(i,matsize):
                for q in range(j,matsize):
                    if ar[i][j] > ar[p][q]:
                        res += 1
    print (res)
    t -= 1
