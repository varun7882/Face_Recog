import cv2
import os
rtdr="AT&T"
for rtdr,drs,fs in os.walk(rtdr):
    if len(fs)!=0:
        for img in fs:
            ph=os.path.join(rtdr,img)
            im=cv2.imread(ph)
            os.remove(ph)
            nimg=img.split(".")[0]+".jpg"
            print nimg
            cv2.imwrite(os.path.join(rtdr,nimg),im)
            
    
