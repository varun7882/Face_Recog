import os
import sys
import cv2
c=0
rootdir2="test_gt_db3_imposters"
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
for rtdr,drs,fs in os.walk("gt_dbi"):
    if len(fs)!=0:
        print fs
        #raw_input()
        c=1
        for i in range(1,10,2):
            ph=os.path.join(rtdr,fs[i])
            im=cv2.imread(ph)
            print ph
            z=ph.split("\\")
            nm=z[1]+"."+str(c)+".jpg"
            nph=os.path.join(rootdir2,nm)
            cv2.imwrite(nph,im)
            c=c+1
