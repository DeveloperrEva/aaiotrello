import json
from .utils import request


class Webhooks(object):
    __module__ = 'aaiotrello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    async def get(self, webhook_id):
        resp = await request.get("https://api.trello.com/1/webhooks/%s" % (webhook_id), params=dict(key=self._apikey, token=self._token), data=None)
        return resp

    async def create(self, webhook_id, url, idModel, description=None):
        resp = await request.post("https://api.trello.com/1/webhooks/%s" % (webhook_id), params=dict(key=self._apikey, token=self._token), data=dict(callbackURL=url, idModel=idModel, description=description))
        return resp
    
    async def delete(self, webhook_id):
        resp = await request.delete("https://api.trello.com/1/webhooks/%s" % (webhook_id), params=dict(key=self._apikey, token=self._token), data=None)
        return resp