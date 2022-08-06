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

ACCESS_TOKEN=str(os.environ.get("ACCESS_TOKEN"))
SECRET=str(os.environ.get("SECRET"))

assert ACCESS_TOKEN, "ACCESS_TOKEN not set"
assert SECRET, "SECRET not set"

line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(SECRET)

from routers.types import *
from utils import *

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/callback", methods=['POST'])
def callback():
    print()
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



if __name__ == "__main__":
    PORT=int(str(os.environ.get("PORT")))
    assert PORT, "PORT not set" 
    certDir='../../crt/'
    app.run(host='0.0.0.0',port=PORT,ssl_context=(certDir+'tonych.me.chained.crt',certDir+'private.key'),debug=True)
