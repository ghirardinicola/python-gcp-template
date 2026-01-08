# Python GCP Template

Template per applicazioni Python deployate su Google Cloud Run con CI/CD automatizzato.

## Caratteristiche

- **FastAPI** come framework web
- **CI/CD** con GitHub Actions:
  - `ci.yml`: lint, test, build Docker
  - `deploy.yml`: build + push GCR + deploy Cloud Run
- **Workflow di sviluppo** strutturato (vedi [WORKFLOW.md](./WORKFLOW.md))

## Uso del Template

1. Clicca "Use this template" su GitHub
2. Configura le variabili in `.github/workflows/deploy.yml`:
   - `PROJECT_ID`: il tuo GCP project ID
   - `REGION`: la region Cloud Run (default: europe-west1)
   - `SERVICE_NAME`: nome del servizio

3. Configura i GitHub Secrets:
   - `GCP_SA_KEY`: JSON key del service account GCP

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

## Struttura Progetto

```
├── .github/workflows/
│   ├── ci.yml          # CI: lint, test, build
│   └── deploy.yml      # Deploy su Cloud Run
├── src/my_app/
│   ├── __init__.py
│   └── main.py         # FastAPI app
├── tests/
│   └── test_main.py
├── Dockerfile
├── pyproject.toml
├── WORKFLOW.md         # Workflow di sviluppo
└── README.md
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
