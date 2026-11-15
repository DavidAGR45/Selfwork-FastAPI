# FastAPI Live 🚀
## 📋 Requisiti di Sistema

- **Python**: `>= 3.14`
- **Poetry**: `>= 2.0.0`

---

## 🛠️ Installazione e Configurazione

1. Posizionarsi nella cartella del progetto:
   ```bash
   cd fastapilive
   ```

2. Installare le dipendenze con Poetry:
   ```bash
   poetry install
   ```

L'ambiente virtuale isolato verrà configurato automaticamente con tutte le dipendenze necessarie (`fastapi`, `uvicorn`).

---

## 🚀 Esecuzione dei Moduli

Ciascun file all'interno di `src/fastapilive/` rappresenta un'applicazione FastAPI autonoma focalizzata su un argomento specifico.

Per avviare un modulo con ricaricamento automatico al salvataggio (`--reload`), eseguire il rispettivo comando dalla directory `fastapilive`:

### 1. Introduzione a FastAPI
Concetti base: istanza dell'applicazione, definizione di route con `@app.get("/")`, funzioni asincrone e serializzazione automatica in formato JSON.
```bash
poetry run uvicorn src.fastapilive.introduzione:app --reload
```

### 2. Path Parameters (Parametri di Percorso)
Parametri dinamici nell'URL, parsing e validazione dei tipi (`int`), ordine di definizione delle route (`/users/me` prima di `/users/{user_id}`), gestione di valori predefiniti tramite `Enum` (`ModelName`) e acquisizione di percorsi completi (`{file_path:path}`).
```bash
poetry run uvicorn src.fastapilive.path_parameters:app --reload
```

### 3. Query Parameters (Parametri di Query)
Parametri opzionali (`str | None`), valori di default e paginazione (`skip`, `limit`), parsing di valori booleani (`short`), parametri obbligatori e combinazione simultanea di Path e Query Parameters.
```bash
poetry run uvicorn src.fastapilive.query_parameters:app --reload
```

### 4. Request Body (Corpo della Richiesta)
Definizione di schemi dati complessi con modelli Pydantic (`BaseModel`), validazione e metadati con `Field`, conversione del modello a dizionario (`model_dump` / `dict`), e combinazione di Body con parametri di percorso e query.
```bash
poetry run uvicorn src.fastapilive.request_body:app --reload
```

### 5. Validation (Validazione Avanzata)
Utilizzo di `Annotated`, validazione stringhe con vincoli di lunghezza e regex (`min_length`, `max_length`, `pattern`), vincoli numerici sui parametri di percorso (`ge`, `gt`, `le`), e mapping di filtri avanzati tramite modelli Pydantic con blocco di campi extra (`extra = "forbid"`).
```bash
poetry run uvicorn src.fastapilive.validation:app --reload
```

## 📖 Documentazione Interattiva delle API

Ogni volta che uno dei moduli è in esecuzione su `http://127.0.0.1:8000`, FastAPI genera automaticamente la documentazione interattiva:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
  *Interfaccia grafica interattiva per visualizzare gli endpoint, verificare gli schemi e testare le richieste direttamente dal browser.*
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  
  *Documentazione alternativa formattata e dettagliata.*
