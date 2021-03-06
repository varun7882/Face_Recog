import numpy as np
import os
import cv2
import cPickle as pickle
import sys

feature = {} 
sift = cv2.SIFT()

i=1
for rtdr,drs,fs in os.walk("dataset_1"):
     for image in fs:
         ph=os.path.join(rtdr,image)
         I = cv2.imread(ph)
         print ph,i
         i=i+1
         #cv2.imshow("hey",I)
         #cv2.waitKey(0)
         #cv2.destroyAllWindows()
         kp,des = sift.detectAndCompute(I,None)
         feature[ph] = des

print "writing features...."
f = open("sift.txt","wb")
pickle.dump(feature,f)
f.close()      
print "Done."    
