import json
from linebot.models import *

class Question:
    def __init__(self,qid):
        raw=self.get(qid)
        self.id=raw['id']
        self.question=raw['question']
        self.options=raw['options']
        self.key=raw['key']
        

    def read_json(self,fname):
        with open(fname,'r') as jfile:
            contents=json.load(jfile)
        return contents

    def get(self,qid):
        qid=str(qid)
        fname=qid+'.json'
        return self.read_json('resources/questions/'+fname)

