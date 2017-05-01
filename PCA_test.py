import numpy as np
x=[2.5,0.5,2.2,1.9,3.1,2.3,2,1,1.5,1.1]
y=[2.4,0.7,2.9,2.2,3.0,2.7,1.6,1.1,1.6,.9]
print len(x)
#print len(y)
sx=0
sy=0
for ex in x:
    sx=sx+ex
for ey in y:
    sy=sy+ey
mx=sx/len(x)
my=sy/len(y)
#print x,y
for i in range(len(x)):
    x[i]=x[i]-mx
    y[i]=y[i]-my
cov_mat=np.cov(x,y)
#print cov_mat
eigval, eigvec = np.linalg.eig(cov_mat)
print eigvec
if(eigval[0]>eigval[1]):
    impvec=eigvec.T[0]
else:
    impvec=eigvec.T[1]
#print impvec
alldata=[x,y]
ans=np.dot(impvec,alldata)
print ans


