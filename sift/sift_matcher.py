import numpy as np
import os
import cv2
import cPickle as pickle
import sys
f = open("sift.txt","rb")
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
           if len(kp_test)==0:
               print "bad quality image Can't be matched"
               continue
           result = {}
           i=0
           for filename_train,des_train in feature.items():
               i=i+1
               good = []
               ctr = 0
               matches = flann.knnMatch(des_train,des_test, k=2)
               print len(matches)
               if des_train is not None:
                   print len(des_train)
               print len(des_test),"item ",i
               #raw_input()
               for m,n in matches:
                   #print m.distance,n.distance
                   if (m.distance < 0.8*n.distance): #Apply the ratio test as per the paper
                      good.append([m])
                      ctr=ctr+1
               result[filename_train] = ctr
               #raw_input()
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
