import numpy as np
import os
import cv2
import cPickle as pickle
import sys

feature = {} 
sift = cv2.SIFT()
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
i=1
for rtdr,drs,fs in os.walk("dataset_1"):
     for image in fs:
         ph=os.path.join(rtdr,image)
         I = cv2.imread(ph)
         gray = cv2.imread(ph,cv2.COLOR_BGR2GRAY)
         faces = detector.detectMultiScale(gray, 1.3, 5)
         for (x,y,w,h) in faces:
              trI=gray[y:y+h,x:x+w]
              print ph,i
              i=i+1
              #cv2.imshow("hey",I)
              #cv2.waitKey(0)
              #cv2.destroyAllWindows()
              kp,des = sift.detectAndCompute(trI,None)
              feature[ph] = des
print feature
f = open("siftonlyfaces.txt","wb")
pickle.dump(feature,f)
f.close()      
     
