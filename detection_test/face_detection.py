import cv2
import sys
import os
# Get user supplied values 
#imagePath = "samples/people1.jpg"
#imagePath="C:/Python27/project/images/a.jpg"
#imagePath="C:/Python27/project/images/scan0001.jpg"
#imagePath="C:/Python27/project/images/a.jpg"
cascPath = "haarcascade_frontalface_default.xml"
pt="C:\Python27\project\databases\gt_db\s01"
ls=os.listdir(pt)
faceCascade = cv2.CascadeClassifier(cascPath)  

# Read the image
for imagePath in ls:
    imagePath=os.path.join(pt,imagePath)
    image = cv2.imread(imagePath) 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
    s=0
    # Detect faces in the image 
    faces = faceCascade.detectMultiScale( 
        gray, 
        scaleFactor=1.1, 
        minNeighbors=5, 
        minSize=(30, 30), 
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )  
    # Draw a rectangle around the faces 
    for (x, y, w, h) in faces:
        s=s+1
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)   
        #cv2.circle(image, (x+w/2, y+h/2), (w+h)/2, (0, 255, 0), 2)
    cv2.imshow("Faces" ,image)
    print "faces found",s
    cv2.waitKey()
    cv2.destroyAllWindows()
