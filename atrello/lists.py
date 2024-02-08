import json
from .utils import request


class Lists(object):
    __module__ = 'atrello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    async def get(self, list_id, cards=None, card_fields=None, fields=None):
        resp = await request.get("https://api.trello.com/1/lists/%s" % (list_id), params=dict(key=self._apikey, token=self._token, cards=cards, card_fields=card_fields, fields=fields), data=None)
        return resp

    async def get_field(self, field, list_id):
        resp = await request.get("https://api.trello.com/1/lists/%s/%s" % (list_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        return resp

    async def get_action(self, list_id, filter=None, fields=None, limit=None, page=None, idModels=None):
        resp = await request.get("https://api.trello.com/1/lists/%s/actions" % (list_id), params=dict(key=self._apikey, token=self._token, filter=filter, fields=fields, limit=limit, page=page, idModels=idModels), data=None)
        return resp

    async def get_board(self, list_id, fields=None):
        resp = await request.get("https://api.trello.com/1/lists/%s/board" % (list_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        return resp

    async def get_board_field(self, field, list_id):
        resp = await request.get("https://api.trello.com/1/lists/%s/board/%s" % (list_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        return resp

    async def get_card(self, list_id, actions=None, attachments=None, members=None, checkItemStates=None, checklists=None, filter=None, fields=None):
        resp = await request.get("https://api.trello.com/1/lists/%s/cards" % (list_id), params=dict(key=self._apikey, token=self._token, actions=actions, attachments=attachments, members=members, checkItemStates=checkItemStates, checklists=checklists, filter=filter, fields=fields), data=None)
        return resp

    async def get_card_filter(self, filter, list_id):
        resp = await request.get("https://api.trello.com/1/lists/%s/cards/%s" % (list_id, filter), params=dict(key=self._apikey, token=self._token), data=None)
        return resp

    async def update(self, list_id, name=None, closed=None):
        resp = await request.put("https://api.trello.com/1/lists/%s" % (list_id), params=dict(key=self._apikey, token=self._token), data=dict(name=name, closed=closed))
        return resp

    async def update_closed(self, list_id, value):
        resp = await request.put("https://api.trello.com/1/lists/%s/closed" % (list_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        return resp

    async def update_name(self, list_id, value):
        resp = await request.put("https://api.trello.com/1/lists/%s/name" % (list_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        return resp

    async def new(self, name, idBoard):
        resp = await request.post("https://api.trello.com/1/lists" % (), params=dict(key=self._apikey, token=self._token), data=dict(name=name, idBoard=idBoard))
        return resp

    async def new_card(self, list_id, name, desc=None):
        resp = await request.post("https://api.trello.com/1/lists/%s/cards" % (list_id), params=dict(key=self._apikey, token=self._token), data=dict(name=name, desc=desc))
        return resp
    
    async def move_list_to_board(self, list_id, value):
        resp = await request.get("https://api.trello.com/1/lists/%s/idBoard" % (list_id), params=dict(value=value, key=self._apikey, token=self._token), data=None)
        return resp

    
