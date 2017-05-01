import numpy as np
import os
import cv2
import cPickle as pickle
import sys
f = open("siftonlyfaces.txt","rb")
feature = pickle.load(f)
f.close()
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50) 
flann = cv2.FlannBasedMatcher(index_params,search_params)
c="a"
while c!="q":
    test_im_name = raw_input('Enter the name of the image ')
    test_im_name = "test_1\\"+test_im_name+'.jpg'
    sift = cv2.SIFT()
    if os.path.isfile == False:
       sys.exit("Exiting program. File doesn't exist.")
    else:
       J = cv2.imread(test_im_name)
       if J is None:
           print "Image Not found"
       else:
           raw_input("start matching...")
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
           print best_match
           raw_input("view results...")
           I = cv2.imread(best_match)
           cv2.imshow('Query image',J)
           cv2.imshow('Matching image',I)
           cv2.waitKey(0)
           cv2.destroyAllWindows()
           a=[]
           for i in result:
               a.append((result[i],i))
           a.sort()

               
           c=raw_input("Enter q to end...")
