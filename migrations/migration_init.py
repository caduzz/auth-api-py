from create_table_user import create_table

def run_migrations():
  print("Executando migration: create_table_user")
  create_table()

if __name__ == "__main__":
  run_migrations()