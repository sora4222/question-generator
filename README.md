# Question Generator

Generates questions from the information that the user provides.

Run the API with one of the following commands (the project uses a `src/` layout):

- Using Uvicorn (module path):

```bash
uvicorn src.main:app --reload
```

- Or using the FastAPI CLI pointing at the file path:

```bash
fastapi dev src/main.py
```

If your IDE or environment doesn't resolve imports from the `src/` directory, set `PYTHONPATH=src` (see `.env` and `.vscode/settings.json`).
