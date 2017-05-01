frr=open("FRR10_yale.txt","r")
ls1=[]
for i in frr:
    ls1.append(eval(i))
frr.close()
far=open("FAR10_yale.txt","r")
ls2=[]
for i in far:
    ls2.append(eval(i))
far.close()
ths=ls1[0]
frrs=ls1[1]
fars=ls2[1]
mn=999999999
for i in range(len(ths)):
    if abs(frrs[i]-fars[i])<mn:
        mn=abs(frrs[i]-fars[i])
        res=i
print "Equal Error rate at ",ths[res],fars[res],frrs[res]
print "Efficiency ",100-(fars[res]+frrs[res])/2.0
    
    
