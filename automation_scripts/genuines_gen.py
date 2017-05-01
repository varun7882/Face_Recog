import os
import sys
import cv2
c=0
rootdir2="test_gt_db3_genuines"
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
for rtdr,drs,fs in os.walk("gt_db3"):
    if len(fs)!=0:
        print fs
        #raw_input()
        c=1
        for i in range(0,9,2):
            ph=os.path.join(rtdr,fs[i])
            im=cv2.imread(ph)
            print ph
            z=ph.split("\\")
            nm=z[1]+"."+str(c)+".jpg"
            c=c+1
            nph=os.path.join(rootdir2,nm)
            cv2.imwrite(nph,im)
            os.remove(ph)
        
    
        
