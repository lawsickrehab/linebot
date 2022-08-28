import json
from linebot.models import *

class Question:
    def __init__(self):
        pass

    def read_json(fname):
        with open(fname,'r') as jfile:
            contents=json.load(jfile)
        return contents
    def read_txt(fname):
        with open(fname,'r') as tfile:
            contents=tfile.read()
        return contents

    def get(qid):
        qid=str(qid)
        fname=qid+'.json'
        return Question.read_json('resources/questions/'+fname)


