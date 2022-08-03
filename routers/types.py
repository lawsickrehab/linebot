from __main__ import handler,line_bot_api

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from linebot.models import *

@handler.default()
def default(event):
    print(event)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

@handler.add(MessageEvent, message=ImageMessage)
def handle_image(event):
    uid=event.source.user_id
    profile=line_bot_api.get_profile(uid)
    name=profile.display_name
    url=profile.picture_url
    ret=name+" your ID is \""+uid+"\", and your profile picture is at "+url
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=ret))
    line_bot_api.push_message(
        uid,
        TextSendMessage(text="Push message again"))
    line_bot_api.push_message(
        uid,
        TextSendMessage(text="We can response many times"))

@handler.add(MessageEvent, message=VideoMessage)
def hendle_video(event):
    url="https://animecorner.me/wp-content/uploads/2022/05/Spy-x-family-06-31.png"

    line_bot_api.reply_message(
        event.reply_token,
        ImageSendMessage(original_content_url=url,preview_image_url=url))
    
        
        
@handler.add(MessageEvent, message=LocationMessage)
def handle_location(event):
    line_bot_api.broadcast(TextSendMessage(text="broadcast test"))

