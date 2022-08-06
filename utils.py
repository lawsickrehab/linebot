import requests

from __main__ import ACCESS_TOKEN

def requestFile(mid,ack=ACCESS_TOKEN):
    url=f'https://api-data.line.me/v2/bot/message/{mid}/content'
    headers={
        "Authorization": "Bearer "+ack
    }
    return requests.get(url,headers=headers)

