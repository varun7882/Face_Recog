import numpy as np
import os
import cv2
import cPickle as pickle
import sys
import auxfuns as ax
#f=raw_input("Enter feature file to be loaded ")
#f=f+".txt"
#f = open(f,"rb")
f = open("sift_AT&T_0.5.txt","rb")
feature = pickle.load(f)
f.close()
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50) 
flann = cv2.FlannBasedMatcher(index_params,search_params) 
#ts=raw_input("Enter imposter users' directory ")
ts="test_AT&T_imposters"
fs=os.listdir(ts)
print fs
sift=cv2.SIFT()
tas=len(fs)
Thresholds=[]
FARs=[]
for th in range(5,95,2): #can be changed increment
    Thresholds.append(th)
    acs=0
    for i in fs:
        ph=os.path.join(ts,i)
        J=cv2.imread(ph)
        kp_test,des_test = sift.detectAndCompute(J,None)
        if len(kp_test)==0:
            print "bad quality image Can't be matched"
            continue
        result = {}
        for filename_train,des_train in feature.items():
            good = []
            ctr = 0
            matches = flann.knnMatch(des_train,des_test, k=2)
            #print len(matches)
            #if des_train is not None:
               #print len(des_train)
            #print len(des_test),"item ",i
            #raw_input()
            for m,n in matches:
               #print m.distance,n.distance
               if (m.distance < 0.8*n.distance): #Apply the ratio test as per the paper
                  good.append([m])
                  ctr=ctr+1
            result[filename_train] = ctr
           #raw_input()
        best_match = max(result,key = lambda x: result[x])
        #print best_match,ph
        #print result[best_match],len(kp_test)
        bsi=cv2.imread(best_match)
        kp_bsi,des_bsi = sift.detectAndCompute(bsi,None)
        bsi=len(kp_bsi)
        pr=ax.getPer(result[best_match],bsi)
        print pr,result[best_match],bsi
        bsn=best_match.split("\\")[1]
        fsn=ph.split("\\")[1].split(".")[0]
        print bsn,fsn
        if pr>=th:
            acs=acs+1
        #raw_input("view results...")
        #I = cv2.imread(best_match)
        #cv2.imshow('Query image',J)
        #cv2.imshow('Matching image',I)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
    tx=ax.getPer(acs,tas)
    FARs.append(tx)
    print Thresholds
    print FARs
    if tx==0:
        break
    #raw_input("sfaa")
wrf=open("FAR2_AT&T.txt","w")
wrf.write(str(Thresholds))
wrf.write("\n")
wrf.write(str(FARs))
wrf.close()
