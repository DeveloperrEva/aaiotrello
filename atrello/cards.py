import json
from .utils import request


class Cards(object):
    __module__ = 'atrello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    async def get(self, card_id, actions=None, action_fields=None, action_limit=None, attachments=None, attachment_fields=None, members=None, member_fields=None, checkItemStates=None, checkItemState_fields=None, checklists=None, checklist_fields=None, fields=None):
        resp = await request.get("https://api.trello.com/1/cards/%s" % (card_id), params=dict(key=self._apikey, token=self._token, actions=actions, action_fields=action_fields, action_limit=action_limit, attachments=attachments, attachment_fields=attachment_fields, members=members, member_fields=member_fields, checkItemStates=checkItemStates, checkItemState_fields=checkItemState_fields, checklists=checklists, checklist_fields=checklist_fields, fields=fields), data=None)
        return resp

    async def get_field(self, field, card_id):
        resp = await request.get("https://api.trello.com/1/cards/%s/%s" % (card_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        return resp

    async def get_action(self, card_id, filter=None, fields=None, limit=None, page=None, idModels=None):
        resp = await request.get("https://api.trello.com/1/cards/%s/actions" % (card_id), params=dict(key=self._apikey, token=self._token, filter=filter, fields=fields, limit=limit, page=page, idModels=idModels), data=None)
        return resp

    async def get_attachment(self, card_id, fields=None):
        resp = await request.get("https://api.trello.com/1/cards/%s/attachments" % (card_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        return resp

    async def get_board(self, card_id, fields=None):
        resp = await request.get("https://api.trello.com/1/cards/%s/board" % (card_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        return resp

    async def get_board_field(self, field, card_id):
        resp = await request.get("https://api.trello.com/1/cards/%s/board/%s" % (card_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        return resp

    async def get_checkItemState(self, card_id, fields=None):
        resp = await request.get("https://api.trello.com/1/cards/%s/checkItemStates" % (card_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        return resp

    async def get_checklist(self, card_id, cards=None, card_fields=None, checkItems=None, checkItem_fields=None, filter=None, fields=None):
        resp = await request.get("https://api.trello.com/1/cards/%s/checklists" % (card_id), params=dict(key=self._apikey, token=self._token, cards=cards, card_fields=card_fields, checkItems=checkItems, checkItem_fields=checkItem_fields, filter=filter, fields=fields), data=None)
        return resp

    async def get_list(self, card_id, fields=None):
        resp = await request.get("https://api.trello.com/1/cards/%s/list" % (card_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        return resp

    async def get_list_field(self, field, card_id):
        resp = await request.get("https://api.trello.com/1/cards/%s/list/%s" % (card_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        return resp

    async def get_member(self, card_id, fields=None):
        resp = await request.get("https://api.trello.com/1/cards/%s/members" % (card_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        return resp

    async def update(self, card_id, name=None, desc=None, closed=None, idList=None, due=None):
        resp = await request.put("https://api.trello.com/1/cards/%s" % (card_id), params=dict(key=self._apikey, token=self._token), data=dict(name=name, desc=desc, closed=closed, idList=idList, due=due))
        return resp

    async def update_closed(self, card_id, value):
        resp = await request.put("https://api.trello.com/1/cards/%s/closed" % (card_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        return resp

    async def update_desc(self, card_id, value):
        resp = await request.put("https://api.trello.com/1/cards/%s/desc" % (card_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        return resp

    async def update_due(self, card_id, value):
        resp = await request.put("https://api.trello.com/1/cards/%s/due" % (card_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        return resp

    async def update_idList(self, card_id, value):
        resp = await request.put("https://api.trello.com/1/cards/%s/idList" % (card_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        return resp

    async def update_name(self, card_id, value):
        resp = await request.put("https://api.trello.com/1/cards/%s/name" % (card_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        return resp

    async def new(self, name, idList, desc=None):
        resp = await request.post("https://api.trello.com/1/cards" % (), params=dict(key=self._apikey, token=self._token), data=dict(name=name, idList=idList, desc=desc))
        return resp

    async def new_action_comment(self, card_id, text):
        resp = await request.post("https://api.trello.com/1/cards/%s/actions/comments" % (card_id), params=dict(key=self._apikey, token=self._token), data=dict(text=text))
        return resp

    async def new_attachment(self, card_id, url, name):
        resp = await request.post("https://api.trello.com/1/cards/%s/attachments" % (card_id), params=dict(key=self._apikey, token=self._token), data=dict(url=url, name=name))
        return resp

    async def new_checklist(self, card_id, value):
        resp = await request.post("https://api.trello.com/1/cards/%s/checklists" % (card_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        return resp

    async def new_label(self, card_id, value):
        resp = await request.post("https://api.trello.com/1/cards/%s/labels" % (card_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        return resp

    async def new_member(self, card_id, value):
        resp = await request.post("https://api.trello.com/1/cards/%s/members" % (card_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        return resp

    async def new_membersVoted(self, card_id, value):
        resp = await request.post("https://api.trello.com/1/cards/%s/membersVoted" % (card_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        return resp

    async def delete(self, card_id):
        resp = await request.delete("https://api.trello.com/1/cards/%s" % (card_id), params=dict(key=self._apikey, token=self._token), data=None)
        return resp

    async def delete_checklist_idChecklist(self, idChecklist, card_id):
        resp = await request.delete("https://api.trello.com/1/cards/%s/checklists/%s" % (card_id, idChecklist), params=dict(key=self._apikey, token=self._token), data=None)
        return resp

    async def delete_label_color(self, color, card_id):
        resp = await request.delete("https://api.trello.com/1/cards/%s/labels/%s" % (card_id, color), params=dict(key=self._apikey, token=self._token), data=None)
        return resp

    async def delete_member_idMember(self, idMember, card_id):
        resp = await request.delete("https://api.trello.com/1/cards/%s/members/%s" % (card_id, idMember), params=dict(key=self._apikey, token=self._token), data=None)
        return resp

    async def delete_membersVoted_idMember(self, idMember, card_id):
        resp = await request.delete("https://api.trello.com/1/cards/%s/membersVoted/%s" % (card_id, idMember), params=dict(key=self._apikey, token=self._token), data=None)
        return resp
