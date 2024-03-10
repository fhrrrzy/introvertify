import requests
import json
from rich import print

user_id = "c41c66d6-989c-4833-8ccf-771f12ef1374"
session = "870ae890684f1ccaa84a62224a6daa0e"

def get_iap():
    url = 'https://live.radiance.thatgamecompany.com/account/collect_collectibles_list'
    body = {
        'user': user_id,
        'session': session,
    }

    headers = {
            'Host': 'live.radiance.thatgamecompany.com',
            'User-Agent': 'Sky-Live-com.tgc.sky.android/0.24.6.250008 (Xiaomi MI 9; android 29.0.0; es)',
            'X-Session-ID': session,
            'user-id': user_id,
            'session': session,
            'Content-type': 'application/json'
        }

    response = requests.post(url, headers=headers, json=body)
    print(response.status_code)
    print(json.loads(response.text))
    # response_json = json.loads(response.text)
    # return response_json

get_iap()