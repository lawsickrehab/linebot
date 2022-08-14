import json

from __main__ import handler,line_bot_api

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)

from linebot.models import *

# from misc.fileHandler import *
#from session import Session
#from logic import react
from ctrl import txtio

@handler.default()
def default(event):
    ret="This type of event is not defined yet. Please contact the developer.\n\n"+str(event)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=ret))

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    ret=txtio(event)
    line_bot_api.reply_message(event.reply_token,ret)
    return
