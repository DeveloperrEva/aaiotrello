import json
from .utils import request


class Checklists(object):
    __module__ = 'atrello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    async def get(self, checklist_id, cards=None, card_fields=None, checkItems=None, checkItem_fields=None, fields=None):
        resp = await request.get("https://api.trello.com/1/checklists/%s" % (checklist_id), params=dict(key=self._apikey, token=self._token, cards=cards, card_fields=card_fields, checkItems=checkItems, checkItem_fields=checkItem_fields, fields=fields), data=None)
        return resp

    async def get_field(self, field, checklist_id):
        resp = await request.get("https://api.trello.com/1/checklists/%s/%s" % (checklist_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        return resp

    async def get_board(self, checklist_id, fields=None):
        resp = await request.get("https://api.trello.com/1/checklists/%s/board" % (checklist_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        return resp

    async def get_board_field(self, field, checklist_id):
        resp = await request.get("https://api.trello.com/1/checklists/%s/board/%s" % (checklist_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        return resp

    async def get_card(self, checklist_id, actions=None, attachments=None, members=None, checkItemStates=None, checklists=None, filter=None, fields=None):
        resp = await request.get("https://api.trello.com/1/checklists/%s/cards" % (checklist_id), params=dict(key=self._apikey, token=self._token, actions=actions, attachments=attachments, members=members, checkItemStates=checkItemStates, checklists=checklists, filter=filter, fields=fields), data=None)
        return resp

    async def get_card_filter(self, filter, checklist_id):
        resp = await request.get("https://api.trello.com/1/checklists/%s/cards/%s" % (checklist_id, filter), params=dict(key=self._apikey, token=self._token), data=None)
        return resp

    async def get_checkItem(self, checklist_id, filter=None, fields=None):
        resp = await request.get("https://api.trello.com/1/checklists/%s/checkItems" % (checklist_id), params=dict(key=self._apikey, token=self._token, filter=filter, fields=fields), data=None)
        return resp

    async def update(self, checklist_id, name=None):
        resp = await request.put("https://api.trello.com/1/checklists/%s" % (checklist_id), params=dict(key=self._apikey, token=self._token), data=dict(name=name))
        return resp

    async def update_name(self, checklist_id, value):
        resp = await request.put("https://api.trello.com/1/checklists/%s/name" % (checklist_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        return resp

    async def new(self, name, idBoard):
        resp = await request.post("https://api.trello.com/1/checklists" % (), params=dict(key=self._apikey, token=self._token), data=dict(name=name, idBoard=idBoard))
        return resp

    async def new_checkItem(self, checklist_id, name):
        resp = await request.post("https://api.trello.com/1/checklists/%s/checkItems" % (checklist_id), params=dict(key=self._apikey, token=self._token), data=dict(name=name))
        return resp

    async def delete_checkItem_idCheckItem(self, idCheckItem, checklist_id):
        resp = await request.delete("https://api.trello.com/1/checklists/%s/checkItems/%s" % (checklist_id, idCheckItem), params=dict(key=self._apikey, token=self._token), data=None)
        return resp

    
