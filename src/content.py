from question import Question
from linebot.models import * 

class Content:
    def __init__(self,qid):
        self.q=Question(qid)
    
    def ask(self):
        text_message=TextSendMessage(text=self.q.question,
            quick_reply=QuickReply(items=
                [QuickReplyButton(action=MessageAction(label=opt, text=opt)) for opt in self.q.options]
            ))
        return text_message

