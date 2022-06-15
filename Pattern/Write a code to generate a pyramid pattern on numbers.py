def Repeat(x):
    size=len(x)
    repeated=[]
    for i in range(size):
        k=i+1
        for j in range(k,size):
            if x[i]==x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated
n=int(input())
list1=list(map(int,input().split(" ")))
X=len(Repeat(list1))
Y=Repeat(list1)
if(X>0):
    G=[int(k) for k in Y]
    GG=" ".join(map(str,G))
    print(GG)
else:
    print(-1)
