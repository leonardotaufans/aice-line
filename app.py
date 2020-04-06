import os
from flask import (
    Flask, request, abort)
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)

CHANNEL_ACCESS_TOKEN = "i/BkxMCXNZjyVfvINPqkvioOxAG4JekP6kV7vKLExUvSKAlNqcVXHzgp6BCRzLhjE14qLGTjLLJNllP2UTN7hZJ0Nrp8sPWVqczZcofccXygaXyReZy1iL7yeRfGR7ri0I/XRn7LxuOLrde/XIXcqAdB04t89/1O/w1cDnyilFU="
CHANNEL_SECRET = "3af3a27eb3ce5ee3fbd3577e28df0920"

app = Flask(__name__)
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
# channel secret:
