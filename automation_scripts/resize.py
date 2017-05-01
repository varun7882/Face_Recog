import os
import sys
import cv2
import numpy as np
print "da"
'''im=cv2.imread("test_data/himanshu/User.Himanshu.1.jpg",cv2.IMREAD_GRAYSCALE)
imq=cv2.resize(im,(160,160))
print im.shape
cv2.imshow("tez ldka",im)
cv2.imshow("tez ldka 160*160",imq)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
c=0
rootdir2="test_data_2"
if(not os.path.exists(rootdir2)):
    os.mkdir(rootdir2)
for rootdir,dirs,fname in os.walk("test_data"):
    #print rootdir,dirs,fname
    for files in dirs:
        print files
        c=c+1
        path=os.path.join(rootdir,files)
        path2=os.path.join(rootdir2,str(c)+files)
        if(not os.path.exists(path2)):
            os.mkdir(path2)
        for img in os.listdir(path):
            im=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
            #cv2.imshow("h",im)
            imgs=cv2.resize(im,(160,160))
            #cv2.imshow("jh",imgs)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
            print os.path.join(path2,img)
            cv2.imwrite(os.path.join(path2,img),imgs)
       
        
    
