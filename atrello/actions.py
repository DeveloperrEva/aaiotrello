import json
from .utils import request


class Actions(object):
    __module__ = 'atrello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    async def get(self, action_id, fields=None, member=None, member_fields=None, memberCreator=None, memberCreator_fields=None):
        resp = await request.get("https://api.trello.com/1/actions/%s" % (action_id), params=dict(key=self._apikey, token=self._token, fields=fields, member=member, member_fields=member_fields, memberCreator=memberCreator, memberCreator_fields=memberCreator_fields), data=None)
        return resp

    async def get_field(self, field, action_id):
        resp = await request.get("https://api.trello.com/1/actions/%s/%s" % (action_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        return resp

    async def get_board(self, action_id, fields=None):
        resp = await request.get("https://api.trello.com/1/actions/%s/board" % (action_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        return resp

    async def get_board_field(self, field, action_id):
        resp = await request.get("https://api.trello.com/1/actions/%s/board/%s" % (action_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        return resp

    async def get_card(self, action_id, fields=None):
        resp = await request.get("https://api.trello.com/1/actions/%s/card" % (action_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        return resp

    async def get_card_field(self, field, action_id):
        resp = await request.get("https://api.trello.com/1/actions/%s/card/%s" % (action_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        return resp

    async def get_list(self, action_id, fields=None):
        resp = await request.get("https://api.trello.com/1/actions/%s/list" % (action_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        return resp

    async def get_list_field(self, field, action_id):
        resp = await request.get("https://api.trello.com/1/actions/%s/list/%s" % (action_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        return resp

    async def get_member(self, action_id, fields=None):
        resp = await request.get("https://api.trello.com/1/actions/%s/member" % (action_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        return resp

    async def get_member_field(self, field, action_id):
        resp = await request.get("https://api.trello.com/1/actions/%s/member/%s" % (action_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        return resp

    async def get_memberCreator(self, action_id, fields=None):
        resp = await request.get("https://api.trello.com/1/actions/%s/memberCreator" % (action_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        return resp

    async def get_memberCreator_field(self, field, action_id):
        resp = await request.get("https://api.trello.com/1/actions/%s/memberCreator/%s" % (action_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        return resp

    async def get_organization(self, action_id, fields=None):
        resp = await request.get("https://api.trello.com/1/actions/%s/organization" % (action_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        return resp

    async def get_organization_field(self, field, action_id):
        resp = await request.get("https://api.trello.com/1/actions/%s/organization/%s" % (action_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        return resp

    
