from typing import List

import aiohttp

from . import base


class Handler(base.Handler):
    """Added possibility to send logs for multiple chats"""
    def __init__(self, token, chats, disable_notification=False, **kwargs):
        super().__init__(**kwargs)
        self.chats: List[str] = [chat.strip() for chat in chats.split(',')]
        self.disable_notification = disable_notification
        self.url = "https://api.telegram.org/bot{}/sendMessage".format(token)

    async def store(self, entries):
        async with aiohttp.ClientSession() as session:
            for chat in self.chats:
                data = {
                    "chat_id": chat,
                    "text": "```\n{}\n```".format("\n".join(entries)),
                    "parse_mode": "markdown",
                    "disable_notification": self.disable_notification,
                    "disable_web_page_preview": True,
                }
                async with session.post(self.url, data=data):
                    pass
