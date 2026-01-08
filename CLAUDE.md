# Contesto Progetto per Claude

> **OBBLIGATORIO**: Leggi e segui il [WORKFLOW.md](./WORKFLOW.md) per OGNI task di sviluppo.

## Struttura

Questo è un template Python per applicazioni GCP Cloud Run.

### File Principali

| File | Descrizione |
|------|-------------|
| `src/my_app/main.py` | FastAPI endpoints |
| `.github/workflows/ci.yml` | CI: lint, test, docker build |
| `.github/workflows/deploy.yml` | Deploy su Cloud Run |

### Comandi Utili

```bash
# Test locale
pip install -e ".[dev]"
uvicorn my_app.main:app --reload

# Test
pytest -v

# Lint
ruff check src/
```

### Note

- **MAI committare valori di secret in git** - usare GitHub Secrets
- Lint errors sono warning-only nel CI
