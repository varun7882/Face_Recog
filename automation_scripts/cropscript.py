import numpy as np
import os
import cv2
ndr="gt_db2"
if not os.path.exists(ndr):
     os.mkdir(ndr)
for rtdr,drs,fs in os.walk("gt_db"):
     if len(fs)!=0:
          for i in fs:
               ph=os.path.join(rtdr,i)
               im=cv2.imread(ph)
               im=im[80:430,100:450]
               #cv2.imshow("ds",im)
               #cv2.waitKey(0)
               #cv2.destroyAllWindows()
               nph=rtdr.replace("gt_db","gt_db2")
               if not os.path.exists(nph):
                    os.mkdir(nph)
               print nph
               cv2.imwrite(os.path.join(nph,i),im)
               
     
