def matcher(des,test):
    rt=[]
    if des is None:
        return [[0,0]]
    for i in des:
        mn1=9999999999999999999999999999
        mn2=9999999999999999999999999999
        for j in test:
            x=dis(i,j)
            if x<mn1:
                t=mn1
                mn1=x
                mn2=t
            elif x<mn2:
                mn2=x
        rt.append([mn1,mn2])
    return rt
def dis(x,y):
    t=0
    for i in range(len(x)):
        t=t+pow(x[i]-y[i],2)
    return pow(t,.5)
def getPer(x,y):
    x=float(x)
    y=float(y)
    return (x/y)*100
