# Manuale 4. Request Body

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


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
