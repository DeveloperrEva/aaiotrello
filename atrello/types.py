import json
from .utils import request


class Types(object):
    __module__ = 'atrello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    async def get(self, id):
        resp = await request.get("https://trello.com/1/types/%s" % (id), params=dict(key=self._apikey, token=self._token), data=None)
        return resp
