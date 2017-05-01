import os
dr="gt_db3"
i=1
for rtdr,drs,fs in os.walk(dr):
        if len(fs)!=0:
            if len(fs)!=15:
                print rtdr,len(fs),i
                os.rename(rtdr,os.path.join("gt_dbi",rtdr.split("\\")[1]))
                i=i+1
