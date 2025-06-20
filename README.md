start = PYTHONPATH=./src uvicorn server:app --reload
migration = python migrations/migration_init.py