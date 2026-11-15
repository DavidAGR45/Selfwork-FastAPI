# Manuale 2. Path Parameters

from enum import Enum

from fastapi import FastAPI

app = FastAPI()


# {item_id} nell'URL è un parametro variabile, passato a read_item come item_id.
# /items/foo risponde {"item_id": "foo"}.
#
# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}


# item_id: int dice a FastAPI di convertire il valore del percorso in un intero (parsing).
# /items/3 risponde {"item_id": 3}.

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


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
