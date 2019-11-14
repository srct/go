import requests
from django.conf import settings
import logging
import sys
import functools
from threading import Thread

logger = logging.getLogger(__name__)

def build_msg(request):
    target = request.POST['target']
    short = f'go.gmu.edu/{request.POST["short"]}'
    return f'Short: {short}\nTarget: {target}'

def send_slack_message(msg):
    # Send slack message
    slack_url = settings.SLACK_URL 
    Thread(target=requests.post, args=(slack_url,), kwargs={ 'json': { 'text': msg }}).start()
