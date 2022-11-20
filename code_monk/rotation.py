
t=int(input())
u=[]
p=[]
for i in range(t):
        a,b=map(int,input().split())
        y=list(map(int,input().strip().split()))[:a]
        r=a-(b%a)
        u=y[r:a]
        p=u+y[0:r]
        for i in p:
                print(i,end=" ")
        print("")
