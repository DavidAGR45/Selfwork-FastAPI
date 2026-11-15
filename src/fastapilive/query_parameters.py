# Manuale 3. Query Parameters

from fastapi import FastAPI

app = FastAPI()

# skip e limit non stanno nel path: FastAPI li legge come query parameters.
# Vanno nell'URL dopo ?, separati da &: /items/?skip=0&limit=10.
# I default sono 0 e 10, quindi /items/ equivale a /items/?skip=0&limit=10.

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


# q ha default None: se manca nell'URL resta None.
# item_id è un path parameter, q è un query parameter.
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}


# short è bool. ?short=1 o ?short=true diventano True; altrimenti il valore è False.
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "Questo è un elemento con una descrizione lunga."}
#         )
#     return item


# user_id e item_id sono path parameters. q e short sono query parameters.
# FastAPI li distingue dal nome.

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "Questo è un elemento con una descrizione lunga."}
        )
    return item


# Senza un valore di default, needy è un query parameter obbligatorio.
#
# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     item = {"item_id": item_id, "needy": needy}
#     return item


# needy è obbligatorio, skip ha default 0, limit è opzionale.

@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item
