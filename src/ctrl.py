from session import Session
from message import Message
from logic import react,welcome

def txtio(event):
    uid=event.source.user_id
    session=Session(uid,"s1.csv")
    nlp=Session(uid,"nlp.csv")
    txt=event.message.text
    if txt=='刪光光':
        session.clear()
        ret=Message()
        return ret.text("History deleted!")
    elif txt=='幫助':
        return welcome() 
    elif txt=='歷史紀錄':
        ret=Message()
        hist=session.readcsv()
        if not len(hist):
            return ret.text("History empty!")
        msg='\n'.join(hist)
        return ret.text(msg)
    else:
        session.push_back(txt)

    act=react(session.readcsv(),nlp)
    return act


    if act['type']=="FLEX":
        if 'qr' in act:
            line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text=act['alt'],
                    contents=act['contents'],
                    quick_reply=QuickReply(act['qr'])
                )
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(
                    alt_text=act['alt'],
                    contents=act['contents'],
                )
            )
    elif act['type']=="TEXT":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text=act['content']
            )
        )
    elif act['type']=="FLEXQR":
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(
                alt_text=act['alt'],
                contents=act['contents'],
                quick_reply=QuickReply(act['qr'])
            )
        )
    elif act['type']=="TEXTQR":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text=act[0],
                quick_reply=QuickReply(act[1])
            )
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            SendMessage(act['contents']))
    return


    
    
        
    
