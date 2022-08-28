import csv
import os
import json
from pathlib import Path

class Session:
    def __init__(self,_uid,_sid='s1.csv'):
        self.sdir='session/'
        self.uid=_uid
        self.sid=_sid

        self.sd=os.path.join(self.sdir,self.uid)
        self.sf=os.path.join(self.sdir,self.uid,self.sid)

        os.makedirs(self.sd,exist_ok=True)
        Path(self.sf).touch()
        return


    def attach(self):
        os.chdir(os.getcwd())
        os.chdir(self.sdir)
        os.chdir(self.uid)

    def detach(self):
        os.chdir("..")
        os.chdir("..")
        
    def tdir(self,dname):
        if not os.path.isdir(dname):
            os.mkdir(dname)

    def get(self,uid):
        pass

    def readcsv(self):
        ret=[]
        with open(self.sf,'r') as csvfile:
            scsv=csv.reader(csvfile)
            for i in scsv:
                ret.extend(i)
        return ret

    def writecsv(self,lst):
        with open(self.sf,'w') as csvfile:
            scsv=csv.writer(csvfile)
            scsv.writerow(lst)

    def readjson(self):
        with open(self.sf,'r') as jsonfile:
            contents=json.load(jsonfile)
        return contents

    def writejson(self,dic):
        with open(self.sf,'w') as jsonfile:
            json.dump(dic,jsonfile)

    def push_back(self,data):
        cur=self.readcsv()
        cur.extend([data])
        self.writecsv(cur)
    
    def zip(self):
        return
    
    def clear(self):
        self.writecsv([])
            
    def new(self,sname):
        pass
    
    def ls(self):
        pass

    
