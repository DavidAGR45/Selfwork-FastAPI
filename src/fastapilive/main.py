# Manuale 1. Introduzione FastAPI
# Manuale 2. Path Parameters
# Manuale 3. Query Parameters
# Manuale 4. Request Body
# Manuale 5. Validation

from enum import Enum
from typing import Annotated

from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field

app = FastAPI()


# Manuale 1. Introduzione FastAPI
# from fastapi import FastAPI importa la classe.
# app = FastAPI() crea l'istanza su cui si definiscono i percorsi.
# @app.get("/") collega la funzione alle richieste GET su / (la homepage).
# async indica che la funzione può lavorare in modo asincrono.
# Il dizionario viene convertito in JSON.

@app.get("/")
async def root():
    return {"message": "Ciao Mondo"}


# Manuale 2. Path Parameters
# {item_id} nell'URL è un parametro variabile, passato a read_item come item_id.
# /items/foo risponde {"item_id": "foo"}.
#
# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}


# item_id: int dice a FastAPI di convertire il valore del percorso in un intero (parsing).
# /items/3 risponde {"item_id": 3}.
# Stessa route di Manuale 3 e Manuale 5: resta attiva l'ultima, in Validation.
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}


# /users/me va dichiarato prima di /users/{user_id}.
# Se l'ordine è invertito, "me" viene letto come valore di user_id.

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "utente corrente"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


# ModelName eredita da str ed Enum: il percorso accetta solo alexnet, resnet e lenet.

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}


# {file_path:path} mette nel parametro l'intero percorso, per esempio /files/home/utente/file.txt.

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# Manuale 3. Query Parameters
# skip e limit non stanno nel path: FastAPI li legge come query parameters.
# Vanno nell'URL dopo ?, separati da &: /items/?skip=0&limit=10.
# I default sono 0 e 10, quindi /items/ equivale a /items/?skip=0&limit=10.
# Stessa route di Manuale 5: resta attiva l'ultima, con FilterParams.
#
# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
#
# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]


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
# Stessa route di Manuale 5: resta attiva l'ultima, con Path.
#
# @app.get("/items/{item_id}")
# async def read_user_item(
#     item_id: str, needy: str, skip: int = 0, limit: int | None = None
# ):
#     item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
#     return item


# Manuale 4. Request Body
# Il body si dichiara con un modello Pydantic che estende BaseModel.
# name e price sono obbligatori. description e tax sono opzionali (None).
# Il parametro item: Item fa leggere il JSON, convertire i tipi e validarli.
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#
# @app.post("/items/")
# async def create_item(item: Item):
#     return item


# model_dump() converte il modello in un dizionario.
# Se tax è presente, alla risposta si aggiunge price_with_tax.
#
# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.model_dump()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict


# Field aggiunge metadati e vincoli: max_length sulla descrizione, gt=0 sul prezzo.
# .dict() converte il modello in un dizionario.

class Item(BaseModel):
    name: str
    description: str | None = Field(
        None, title="Descrizione dell'elemento", max_length=300
    )
    price: float = Field(
        ..., gt=0, description="Il prezzo dell'elemento, deve essere maggiore di zero"
    )
    tax: float | None = None


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        item_dict.update({"price_with_tax": item.price + item.tax})
    return item_dict


# Il body si combina con il path parameter. **item.dict() espande i campi del modello.
#
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}


# Il body si combina con path e query. q è opzionale.

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


# Manuale 5. Validation
# Query(max_length=50): q è opzionale e, se c'è, non supera i 50 caratteri.
#
# @app.get("/items/")
# async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# min_length=3: almeno 3 caratteri.
# pattern="^fixedquery$": q deve valere esattamente "fixedquery".
#
# @app.get("/items/")
# async def read_items(
#     q: Annotated[
#         str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")
#     ] = None,
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# Senza default, o con ... (Ellipsis), il query parameter è obbligatorio.
#
# @app.get("/items/")
# async def read_items(q: Annotated[str, Query(min_length=3)] = ...):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# Path aggiunge metadati e vincoli numerici. ge=1: item_id è almeno 1.
# I path parameters sono sempre obbligatori.
#
# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="ID dell'elemento", ge=1)],
# ):
#     return {"item_id": item_id}


# gt=0: maggiore di 0. le=1000: minore o uguale a 1000.

@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="ID dell'elemento", gt=0, le=1000)],
):
    return {"item_id": item_id}


# I query parameters collegati stanno in un modello Pydantic, riusabile.
# Field mette i vincoli sui campi: gt=0 e le=100 su limit, ge=0 su offset.
#
# class FilterParams(BaseModel):
#     limit: int = Field(100, gt=0, le=100)
#     offset: int = Field(0, ge=0)
#     order_by: str = "created_at"
#     tags: list[str] = []
#
# @app.get("/items/")
# async def read_items(filter_query: Annotated[FilterParams, Query()]):
#     return filter_query


# extra=forbid rifiuta i query parameters che non sono nel modello.

class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}

    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: str = "created_at"
    tags: list[str] = []


@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query
