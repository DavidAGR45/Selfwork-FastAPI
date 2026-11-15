# Manuale 1. Introduzione FastAPI
# from fastapi import FastAPI importa la classe.
# app = FastAPI() crea l'istanza su cui si definiscono i percorsi.
# @app.get("/") collega la funzione alle richieste GET su / (la homepage).
# async indica che la funzione può lavorare in modo asincrono.
# Il dizionario viene convertito in JSON.

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Ciao Mondo"}
