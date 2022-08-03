import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi(str(os.environ.get("ACCESS_TOKEN")))
handler = WebhookHandler(str(os.environ.get("SECRET")))

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/callback", methods=['POST','GET'])
def callback():
    if request.method == "GET":
        return str(os.environ.get("SECRET"))
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    PORT=int(str(os.environ.get("PORT")))
    certDir='../../crt/'
    app.run(host='0.0.0.0',port=PORT,ssl_context=(certDir+'tonych.me.chained.crt',certDir+'private.key'))
