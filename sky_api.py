import requests
import json
import re
from random import choices
from string import ascii_uppercase
from rich import print
from tqdm import tqdm

class SkyAccount:
    def __init__(self, user_id, session):
        self.user_id = user_id
        self.session = session

    def get_headers(self):
        return {
            'Host': 'live.radiance.thatgamecompany.com',
            'User-Agent': 'Sky-Live-com.tgc.sky.android/0.24.5.246913 (Xiaomi MI 9; android 29.0.0; es)',
            'X-Session-ID': self.session,
            'user-id': self.user_id,
            'session': self.session,
            'Content-type': 'application/json'
        }

    def make_post_request(self, url, body):
        headers = self.get_headers()
        response = requests.post(url, headers=headers, json=body)
        return response

    def set_friend_name(self, friend_uuid):
        url = 'https://live.radiance.thatgamecompany.com/account/set_friend_name'
        random_name = ''.join(choices(ascii_uppercase, k=4))

        body = {
            "user": self.user_id,
            "user_id": self.user_id,
            "session": self.session,
            "friend": friend_uuid,
            "name": random_name
        }

        response = self.make_post_request(url, body)
        response_json = json.loads(response.text)

        return response, response_json

    def find_uuids_in_response(self, response_json):
        uuid_pattern = re.compile(r'[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}', re.IGNORECASE)
        uuids = []

        def find_uuids(data):
            if isinstance(data, dict):
                for value in data.values():
                    if isinstance(value, (dict, list)):
                        find_uuids(value)
                    elif isinstance(value, str) and uuid_pattern.match(value):
                        uuids.append(value)
            elif isinstance(data, list):
                for item in data:
                    find_uuids(item)

        find_uuids(response_json)
        return set(uuids)

    def get_all_friends(self):
        url = 'https://live.radiance.thatgamecompany.com/account/get_friend_statues'
        body = {
            "max": 1000,
            "sort_ver": 1
        }

        response = self.make_post_request(url, body)
        response_json = json.loads(response.text)
        friend_uuids = self.find_uuids_in_response(response_json)
        return friend_uuids

    def get_all_blocked_friends(self):
        url = 'https://live.radiance.thatgamecompany.com/account/get_blocked_friends'
        body = {
            "user": self.user_id,
            "user_id": self.user_id,
            "session": self.session,
            "page_max": 1000,
            "page_offset": 0
        }

        response = self.make_post_request(url, body)
        response_json = json.loads(response.text)
        # print(response_json)
        blocked_friend_uuids = self.find_uuids_in_response(response_json)
        return blocked_friend_uuids

    def set_all_friends_blocked(self, set_block):
        while True:
            friend_uuids = self.get_all_friends()

            if not friend_uuids:
                break

            with tqdm(total=len(friend_uuids), desc=f"{'Blocking' if set_block else 'Unblocking'} friends", unit="friend") as pbar:
                for friend_uuid in friend_uuids:
                    # Set the name of each friend to a random name before blocking
                    self.set_friend_name(friend_uuid)
                    self.set_friend_block(friend_uuid, set_block)
                    pbar.update(1)

    def set_all_blocked_friends_unblocked(self):
        while True:
            blocked_friend_uuids = self.get_all_blocked_friends()

            if not blocked_friend_uuids:
                break

            with tqdm(total=len(blocked_friend_uuids), desc="Unblocking friends", unit="friend") as pbar:
                for blocked_friend_uuid in blocked_friend_uuids:
                    self.set_friend_block(blocked_friend_uuid, False)
                    pbar.update(1)

    def set_friend_block(self, target_id, set_block):
        url = 'https://live.radiance.thatgamecompany.com/account/set_friend_block'
        body = {
            "user": self.user_id,
            "user_id": self.user_id,
            "session": self.session,
            "friend": target_id,
            "blocked": set_block
        }

        response = self.make_post_request(url, body)
        response_json = json.loads(response.text)

        return response, response_json
