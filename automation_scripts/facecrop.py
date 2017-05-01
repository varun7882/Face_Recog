import numpy as np
import os
import cv2
ndr="gt_db3"
cascPath = "haarcascade_frontalface_default.xml"
detector = cv2.CascadeClassifier(cascPath)
if not os.path.exists(ndr):
     os.mkdir(ndr)
n=1
for rtdr,drs,fs in os.walk("gt_db"):
     if len(fs)!=0:
          for i in fs:
               ph=os.path.join(rtdr,i)
               im=cv2.imread(ph)
               faces = detector.detectMultiScale(im, 1.2, 5)
               for (x,y,w,h) in faces:
                    trI=im[y:y+h,x:x+w]
                    #cv2.imshow("ds",trI)
                    #cv2.waitKey(10)
                    #cv2.destroyAllWindows()
                    nph=rtdr.replace("gt_db","gt_db3")
                    if not os.path.exists(nph):
                         os.mkdir(nph)
                    print nph,n
                    n=n+1
                    cv2.imwrite(os.path.join(nph,i),trI)
               
     
