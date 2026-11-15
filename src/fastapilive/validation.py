# Manuale 5. Validation

from typing import Annotated

from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field

app = FastAPI()


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
