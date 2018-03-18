import math
deg=[x for x in range(1,179)]
a=[]
for i in deg:
    a.append(2*round(math.sin(math.radians(i/2)),3))
for i in range(0,len(deg)):
    if (a[i]==0.618)|(a[i]==1.618):
        print(deg[i])
