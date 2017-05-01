
import matplotlib.pyplot as plt
frr=raw_input("Enter the FRR file ")
far=raw_input("Enter the FAR file ")
frr=frr+".txt"
frr=open(frr,"r")
ls1=[]
for i in frr:
    ls1.append(eval(i))
frr.close()
##plt.xlabel("threshold")
##plt.ylabel("frr")
##plt.plot(ls1[0],ls1[1],'g')
##plt.title("False Rejection Rate")
##plt.show()
far=far+".txt"
far=open(far,"r")
ls2=[]
for i in far:
    ls2.append(eval(i))
far.close()
##plt.xlabel("threshold")
##plt.ylabel("far")
##plt.plot(ls2[0],ls2[1],'r')
##plt.title("False Acceptance Rate")
##plt.show()
ths=ls1[0]
frrs=ls1[1]
fars=ls2[1]
plt.xlabel("thresholds")
plt.ylabel("rates")
plt.plot(ls1[0],ls1[1],'g',ls2[0],ls2[1],'r')
plt.show()


tars=frrs[:]
import numpy as np
tars=np.array(tars)
tars=100-tars
print tars
print fars
if len(fars)<len(tars):
    for i in range(len(tars)-len(fars)):
        fars.append(0)
elif len(fars)>len(tars):
    for i in range(len(fars)-len(tars)):
        tars.append(0)
    
plt.xlabel("FAR")
plt.ylabel("TAR")
plt.plot(fars,tars)
plt.title("ROC curve")
plt.show()
