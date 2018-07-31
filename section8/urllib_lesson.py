"""
REST

HTTPメソッド クライアントが行いたい処理をサーバに伝える。

GET    データの参照
POST データの新規登録
PUT    データの更新
DELETE データの削除

"""

import urllib.request
import json

with urllib.request.urlopen(url) as f:
    print(json.loads(f.read().decode('utf-8')))
