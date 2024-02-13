import json
from .utils import request


class Tokens(object):
    __module__ = 'aaiotrello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    async def get(self, token, fields=None):
        resp = await request.get("https://trello.com/1/tokens/%s" % (token), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        return resp

    async def get_field(self, field, token):
        resp = await request.get("https://trello.com/1/tokens/%s/%s" % (token, field), params=dict(key=self._apikey, token=self._token), data=None)
        return resp

    async def get_member(self, token, fields=None):
        resp = await request.get("https://trello.com/1/tokens/%s/member" % (token), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        return resp

    async def get_member_field(self, field, token):
        resp = await request.get("https://trello.com/1/tokens/%s/member/%s" % (token, field), params=dict(key=self._apikey, token=self._token), data=None)
        return resp
