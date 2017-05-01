import cv2
import numpy as np

img = cv2.imread('05.jpg')
#gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT()
kp = sift.detect(img,None)

img=cv2.drawKeypoints(img,kp)

cv2.imwrite('x1.jpg',img)
img = cv2.imread('x1.jpg')
cv2.imshow("key points",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
