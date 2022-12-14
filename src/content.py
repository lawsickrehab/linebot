from question import Question
from definition import Definition
from linebot.models import * 

ASK_DEF="請問什麼是"
UNDERSTAND="懂"
UNUNDERSTAND="不懂"
class Content:
    def __init__(self):
        self.dic=Definition()
    
    def ask(self,qid,definition=False):
        qid=str(qid)
        self.q=Question(qid)
        options=[QuickReplyButton(action=MessageAction(label=opt, text=opt)) for opt in self.q.options]
        if definition:
            for vol,df in self.dic.dic.items():
                if vol in self.q.question:
                    options.extend([self.button("什麼是"+vol+"？",ASK_DEF+vol)])
        text_message=TextSendMessage(text=self.q.question,
            quick_reply=QuickReply(items=options))
        return text_message

    def define(self,key):
        return TextSendMessage(text=self.dic.search(key)+"",
            quick_reply=QuickReply(items=[self.button(UNDERSTAND,UNDERSTAND)]))

    def button(self,lbl,txt):
        return QuickReplyButton(action=MessageAction(label=lbl,text=txt))

    def history(self,ans):
        out=""
        for qid,rep in ans.items():
            out+=Question(qid).short+"："+rep+"\n"
        return TextSendMessage(text=out[:-1])
