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

## 🚀 Esecuzione

I cinque manuali stanno in `src/fastapilive/main.py`. Dalla cartella `fastapilive`:

```bash
poetry run uvicorn src.fastapilive.main:app --reload
```

## 📖 Documentazione Interattiva delle API

Ogni volta che uno dei moduli è in esecuzione su `http://127.0.0.1:8000`, FastAPI genera automaticamente la documentazione interattiva:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
  *Interfaccia grafica interattiva per visualizzare gli endpoint, verificare gli schemi e testare le richieste direttamente dal browser.*
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  
  *Documentazione alternativa formattata e dettagliata.*
