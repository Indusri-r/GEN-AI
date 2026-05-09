# GEN-AI

A simple AI-powered SQL agent built with Streamlit, GPT-2, and SQLite.

## Features

- Natural language input for SQL query generation
- Executes generated SQL against a local SQLite database
- Displays results in a clean Streamlit table
- Sample database includes `Employees` and `Departments` for JOIN queries
- Supports additional employee fields: `position`, `hire_date`, and `age`

## Run locally

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

## Notes

- The SQL generation is powered by a local GPT-2 model.
- The database is recreated on startup to load sample data.
- `db.sqlite` and generated Python cache files are ignored by Git.
