import os
import sys
import cv2
c=0
rootdir2="test_yale_imposters"
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
print "hey"
for rtdr,drs,fs in os.walk("yale_imposters"):
    if len(fs)!=0:
        print fs
        #raw_input()
        ph=os.path.join(rtdr,fs[1])
        im=cv2.imread(ph)
        print ph
        z=ph.split("\\")
        nm=z[1]+".1.jpg"
        nph=os.path.join(rootdir2,nm)
        cv2.imwrite(nph,im)
        os.remove(ph)
        ph=os.path.join(rtdr,fs[6])
        im=cv2.imread(ph)
        print ph
        z=ph.split("\\")
        nm=z[1]+".2.jpg"
        nph=os.path.join(rootdir2,nm)
        cv2.imwrite(nph,im)
        os.remove(ph)
