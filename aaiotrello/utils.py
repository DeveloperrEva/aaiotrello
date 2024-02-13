from aiohttp import ClientSession


class AsyncRequest(object):

    def clear(self, data):
        result = {}
        for k, v in data.items():
            if isinstance(v, dict):
                result[k] = self.clear(v)
            elif v:
                result[k] = v
        return result

    async def get(self, *args, **kwargs):
        kwargs = self.clear(kwargs)
        kwargs['ssl'] = False
        async with ClientSession() as session:
            async with session.get(*args, **kwargs) as resp:
                resp.raise_for_status()
                return await resp.json()

    async def post(self, *args, **kwargs):
        kwargs = self.clear(kwargs)
        kwargs['ssl'] = False
        async with ClientSession() as session:
            async with session.post(*args, **kwargs) as resp:
                resp.raise_for_status()
                return await resp.json()

    async def put(self, *args, **kwargs):
        kwargs = self.clear(kwargs)
        kwargs['ssl'] = False
        async with ClientSession() as session:
            async with session.put(*args, **kwargs) as resp:
                resp.raise_for_status()
                return await resp.json()

request = AsyncRequest()
