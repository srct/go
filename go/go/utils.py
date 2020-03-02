import requests
from django.conf import settings
from threading import Thread

def build_msg(request):
    target = request.POST['target']
    email = request.user.email
    short = f'go.gmu.edu/{request.POST["short"]}'
    return f'User: {email}\nShort: {short}\nTarget: {target}'

def send_slack_message(msg):
    # Send slack message
    slack_url = settings.SLACK_URL 
    Thread(target=requests.post, args=(slack_url,), kwargs={ 'json': { 'text': msg }}).start()
