import json
from requests import Request

def add_chat_members(self, chat_id, members):
    return self.http_session.get(
        url=f"{self.api_base_url}/chats/members/add",
        params={
            "token": self.token,
            "chatId": chat_id,
            "members": json.dumps([{"sn": m} for m in members]),
        },
    )

def create_chat(self, name, about="", rules="", members=[], public=False, join_moderation=False, default_role="member"):
    return self.http_session.get(
        url=f"{self.api_base_url}/chats/createChat",
        params={
            "token": self.token,
            "name": name,
            "about": about,
            "rules": rules,
            "members": json.dumps([{"sn": m} for m in members]),
            "public": "true" if public else "false",
            "defaultRole": default_role,
            "joinModeration": "true" if join_moderation else "false",
        },
    )
