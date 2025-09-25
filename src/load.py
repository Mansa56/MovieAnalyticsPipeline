import pandas as pd
from sqlalchemy import create_engine

def load_to_sqlite(df, db_name='movies.db', table_name='movies'):
    engine = create_engine(f'sqlite:///{db_name}')
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Data loaded into {db_name} in table {table_name}")

if __name__ == "__main__":
    df = pd.read_csv('../data/movies_clean.csv')
    load_to_sqlite(df)
