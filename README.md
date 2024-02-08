# aaiotrello
Async Trello API Client

Python 3.6+

## Install

```bash
pip install aaiotrello
```

## Auth

#### TRELLO_APP_KEY: https://trello.com/app-key/
#### TRELLO_APP_TOKEN:

First you need gen auth url:
```python
from aaiotrello import TrelloApi

trello = TrelloApi(config.TRELLO_KEY)
trello.set_token(config.TRELLO_TOKEN)
```
Than you need copy value of token_url and auth your trello account in webbrowser
After that you will get token

#### Apply token in your app:
```python
trello_app.set_token(TRELLO_APP_TOKEN)
```

#### Sample usage

Get board info:
```python
board = await trello_app.boards.get("5c49c07e48557d4e29414936")
```
