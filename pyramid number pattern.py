n=int(input())
f=[]
c=1
for i in range(n):
    f.append(str(c))
    c+=2
f.reverse()
x=0
z=0
for i in range(n):
    print("{}{}".format(" "*x,f[z]*int(f[z])))
    z=z+1
    x+=1
