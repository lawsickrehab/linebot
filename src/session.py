import csv
import os
from pathlib import Path

class Session:
    def __init__(self,_uid,_sid='s1.csv'):
        self.sdir='session/'
        self.uid=_uid
        self.sid=_sid

        self.sd=os.path.join(self.sdir,self.uid)
        self.ss=os.path.join(self.sdir,self.uid,self.sid)

        os.makedirs(self.sd,exist_ok=True)
        Path(self.ss).touch()
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

    def read(self):
        ret=[]
        with open(self.ss,'r') as csvfile:
            scsv=csv.reader(csvfile)
            for i in scsv:
                ret.extend(i)
        return ret

    def write(self,lst):
        with open(self.ss,'w') as csvfile:
            scsv=csv.writer(csvfile)
            scsv.writerow(lst)

    def push_back(self,data):
        cur=self.read()
        cur.extend([data])
        self.write(cur)
    
    def zip(self):
        return
    
    def clear(self):
        self.write([])
            
    def new(self,sname):
        pass
    
    def ls(self):
        pass

    
