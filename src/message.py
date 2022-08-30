import json
from linebot.models import *

class Message:
    def __init__(self):
        self.ret={
            'type': 'not-defined',
            'contents': 'blank'
        }

    def read_json(fname):
        with open(fname,'r') as jfile:
            contents=json.load(jfile)
        return contents
    def read_txt(fname):
        with open(fname,'r') as tfile:
            contents=tfile.read()
        return contents[:-1]

    def text(self,contents):
        if contents[-4:]==".txt":
            contents=Message.read_txt('resources/text/'+contents)
        return TextSendMessage(text=contents)
        self.ret['type']="TEXT"
        self.ret['contents']=contents
        return self.ret

    def flex(self,fname):
        self.ret['type']="FLEX"
        self.ret['contents']=Message.read_json('resources/flex/'+fname)
        self.ret['alt']=fname
        return FlexSendMessage(
            alt_text=self.ret['alt'],
            contents=self.ret['contents']
        )
        return self.ret

    def textqr(self,contents,qrname):
        self.ret['type']="TEXTQR"
        self.ret['contents']=contents
        self.ret['qr']=Message.read_json('resources/quickReply/'+qrname)
        return TextSendMessage(
            text=self.ret['contents'],
            quick_reply=QuickReply(self.ret['qr'])
        )
        return self.ret

    def flexqr(self,fname,qrname):
        self.ret['type']="FLEXQR"
        self.ret['contents']=Message.read_json('resources/flex/'+fname)
        self.ret['qr']=Message.read_json('resources/quickReply/'+qrname)
        self.ret['alt']=fname
        return FlexSendMessage(
            alt_text=self.ret['alt'],
            contents=self.ret['contents'],
            quick_reply=QuickReply(self.ret['qr'])
        )
        return self.ret
    
    def zip(self,zname):
        pass
