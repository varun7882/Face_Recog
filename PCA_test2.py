import numpy as np
x=[2.5,0.5,2.2,1.9,3.1,2.3,2,1,1.5,1.1]
y=[2.4,0.7,2.9,2.2,3.0,2.7,1.6,1.1,1.6,.9]
print "Inital data..."
raw_input("")
print "x",x
print "y",y
sx=0
sy=0
mx=np.mean(x)
my=np.mean(y)
raw_input("")
print "mean_x",mx
print "mean_y",my
for i in range(len(x)):
    x[i]=x[i]-mx
    y[i]=y[i]-my
print "mean centered data..."
raw_input("")
rx=np.round(x,2)
ry=np.round(y,2)
print "x",rx
print "y",ry
mx=np.mean(x)
my=np.mean(y)
cov_mat=np.cov(x,y)
#print cov_mat
eigval, eigvec = np.linalg.eig(cov_mat)
print "eigen values are..."
print eigval
print "eigen vectors are..."
print eigvec
if(eigval[0]>eigval[1]):
    impvec=eigvec.T[0]
else:
    impvec=eigvec.T[1]
#print impvec
alldata=[x,y]
ans=np.dot(impvec,alldata)
raw_input("")
print "transformed data..."
print np.round(ans,2)
raw_input("")
import matplotlib.pyplot as plt
plt.plot(x,y,'bo')
plt.plot(mx,my,'go')
xx=[0]*len(x)
plt.plot(ans,xx,'ro')
ax=plt.axes()
ax.arrow(mx,my,eigvec.T[0][0],eigvec.T[0][1],head_width=0.05, head_length=0.1, fc='k',color="green")
ax.arrow(mx,my,eigvec.T[1][0],eigvec.T[1][1],head_width=0.05, head_length=0.1, fc='k', color="green")
#plt.plot([-1,-2,0,1,2,3,4,5,6,7],xx)
plt.show()
