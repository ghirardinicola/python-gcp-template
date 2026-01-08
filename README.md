# Python GCP Template

Template per applicazioni Python deployate su Google Cloud Run con CI/CD automatizzato.

## Caratteristiche

- **FastAPI** come framework web
- **CI/CD** con GitHub Actions:
  - `ci.yml`: lint, test, build Docker
  - `deploy.yml`: build + push GCR + deploy Cloud Run
- **Workflow di sviluppo** strutturato (vedi [WORKFLOW.md](./WORKFLOW.md))

## Struttura

```
python-gcp-template/
├── .github/workflows/
│   ├── ci.yml          # Lint, test, Docker build
│   └── deploy.yml      # Deploy su Cloud Run
├── src/my_app/
│   ├── __init__.py
│   └── main.py         # FastAPI app con /health
├── tests/
│   └── test_main.py
├── Dockerfile
├── pyproject.toml      # Python 3.10+, FastAPI, Ruff, Pytest
├── WORKFLOW.md         # Workflow di sviluppo
├── CLAUDE.md           # Contesto per Claude
├── README.md
└── .gitignore
```

## Uso del Template

1. Vai su GitHub e clicca **"Use this template"**
2. Configura le variabili in `.github/workflows/deploy.yml`:
   - `PROJECT_ID`: il tuo GCP project ID
   - `REGION`: la region Cloud Run (default: europe-west1)
   - `SERVICE_NAME`: nome del servizio
3. Aggiungi il secret `GCP_SA_KEY` nelle settings del repo (vedi Setup GCP)

## Sviluppo Locale

```bash
# Installa dipendenze
pip install -e ".[dev]"

# Avvia server di sviluppo
uvicorn my_app.main:app --reload

# Esegui test
pytest -v

# Lint
ruff check src/
ruff format src/
```

## Setup GCP

1. Crea un progetto GCP
2. Abilita le API:
   - Cloud Run API
   - Container Registry API
3. Crea un Service Account con i ruoli:
   - Cloud Run Admin
   - Storage Admin
   - Service Account User
4. Scarica la JSON key e aggiungila come GitHub Secret `GCP_SA_KEY`

## License

MIT
