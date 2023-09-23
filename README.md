# llm-api-server

## Install packages

```shell
pipenv install
```

## Run the app

```shell
pipenv run start
```

サーバー起動後に以下のページから API documents を参照できる。

- http://0.0.0.0:8000/docs
- http://0.0.0.0:8000/redoc

## Call the API

Request

```shell
curl -X 'POST' \
  'http://0.0.0.0:8000/question' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "こんにちは"
}'
```

Response

```shell
{
  "text": "こんにちは！お元気ですか？何かお手伝いできることはありますか？"
}
```

## 参考

- [機能 - FastAPI](https://fastapi.tiangolo.com/ja/features/)