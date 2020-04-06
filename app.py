import os
from flask import (
    Flask, request, abort)
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)

CHANNEL_ACCESS_TOKEN = os.environ.get("CHANNEL_ACCESS_TOKEN")
CHANNEL_SECRET = os.environ.get("CHANNEL_SECRET")

app = Flask(__name__)
line_bot_api = LineBotApi("i/BkxMCXNZjyVfvINPqkvioOxAG4JekP6kV7vKLExUvSKAlNqcVXHzgp6BCRzLhjE14qLGTjLLJNllP2UTN7hZJ0Nrp8sPWVqczZcofccXygaXyReZy1iL7yeRfGR7ri0I/XRn7LxuOLrde/XIXcqAdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("3af3a27eb3ce5ee3fbd3577e28df0920")


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    message = event.message.text.lower()
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=message)
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0')
