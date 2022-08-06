import requests

def requestFile(ACCESS_TOKEN, mid):
    url=f'https://api-data.line.me/v2/bot/message/{mid}/content'
    headers={
        "Authorization": "Bearer "+ACCESS_TOKEN
    }
    return requests.get(url,headers=headers)

