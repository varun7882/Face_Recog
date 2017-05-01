import numpy as np
import os
import cv2
import cPickle as pickle
import glob
import sys



feature = {} #Create a dictionary to store the descriptors and the associated filename
sift = cv2.SIFT() # Create SIFT object

a = os.chdir("dataset")
file_list = glob.glob('*.jpg')
print file_list
raw_input("Press a Key...")
for image in file_list:
    I = cv2.imread(image)
    #print I
    #cv2.imshow("hey",I)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    kp,des = sift.detectAndCompute(I,None)
    feature[image] = des #Store the descriptor using the filename as key
print feature
f = open("sift.txt","wb")
pickle.dump(feature,f)
f.close()      
     
f = open("sift.txt","rb")
feature = pickle.load(f)
f.close()
a = os.chdir("..\\")
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50) 
flann = cv2.FlannBasedMatcher(index_params,search_params)
# 120 images exist in the testing folder
test = os.chdir("test")
test_im_name = raw_input('Enter the name of the image ')
test_im_name = test_im_name+'.jpg'


if os.path.isfile == False:
   sys.exit("Exiting program. File doesn't exist.")
else:
   J = cv2.imread(test_im_name)
   cv2.imshow('Query image',J)
   kp_test,des_test = sift.detectAndCompute(J,None)
   result = {}
   for filename_train,des_train in feature.items():
       good = []
       ctr = 0
       matches = flann.knnMatch(des_train,des_test, k=2)    
       for m,n in matches:
           if (m.distance < 0.8*n.distance): #Apply the ratio test as per the paper
              good.append([m])
              ctr=ctr+1
       result[filename_train] = ctr
   best_match = max(result,key = lambda x: result[x])
   os.chdir("..\\dataset")
   I = cv2.imread(best_match)
   cv2.imshow('Matching image',I)
   cv2.waitKey(0)
