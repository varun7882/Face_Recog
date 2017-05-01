import os
import sys
import cv2
c=0
rootdir2="dataset_2"
if(not os.path.exists(rootdir2)):
    os.mkdir(rootdir2)
'''im=cv2.imread("dataset\User.Himanshu.1.jpg",cv2.IMREAD_GRAYSCALE)
#imq=cv2.resize(im,(160,160))
print im.shape
cv2.imshow("tez ldka",im)
#cv2.imshow("tez ldka 160*160",imq)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
t=""
c=0
s="."
print "hey"
for rtdr,drs,fs in os.walk("dataset"):
    #print type(fs)
    for i in range(len(fs)):
        ph=os.path.join(rtdr,fs[i])
        im=cv2.imread(ph,cv2.IMREAD_GRAYSCALE)
        z=fs[i].split(".")
        nm=z[1]
        if nm!=t:
            t=nm
            c=c+1
        z.insert(2,str(c))
        print z
        nfs=s.join(z)
        ph=os.path.join("dataset_2",nfs)
        cv2.imwrite(ph,im)
