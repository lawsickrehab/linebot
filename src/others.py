import json

from __main__ import handler,line_bot_api

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, responses,RichMenuSize
)

from linebot.models import *

# from misc.fileHandler import *
from misc.session import Session
from routers.logic import react


@handler.add(MessageEvent, message=ImageMessage)
def handle_image(event):
#    saveEventFile(event)
    return

    ret=name+" your ID is \""+uid+"\", and your profile picture is at "+url
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=ret))
    

@handler.add(MessageEvent, message=VideoMessage)
def handle_video(event):
#    saveEventFile(event)
    return
    uid=event.source.user_id
    mid=event.message.id
    line_bot_api.reply_message(
        event.reply_token,
        ImageSendMessage(original_content_url=url,preview_image_url=url))
    print(requestFile(mid))

@handler.add(MessageEvent, message=AudioMessage)
def handle_audio(event):
#    saveEventFile(event)
    return

@handler.add(MessageEvent, message=FileMessage)
def handle_file(event):
#    saveEventFile(event)
    return
        
@handler.add(MessageEvent, message=LocationMessage)
def handle_location(event):
    uid=event.source.user_id
    profile=line_bot_api.get_profile(uid)
    name=profile.display_name
    ret=name+"sent a test boadcast message, notification off."
    line_bot_api.broadcast(TextSendMessage(text=ret),notification_disabled=True)

@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker(event):
    with open('tmp.json') as f:
        fm=json.load(f)
    line_bot_api.reply_message(
        event.reply_token,
        FlexSendMessage(alt_text='hello',contents=fm))
