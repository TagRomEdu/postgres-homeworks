import psycopg2
import os

customers_data = os.path.join(os.path.dirname(__file__), 'north_data', 'customers_data.csv')
employees_data = os.path.join(os.path.dirname(__file__), 'north_data', 'employees_data.csv')
orders_data = os.path.join(os.path.dirname(__file__), 'north_data', 'orders_data.csv')

with psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="Tyjnbr888"
) as conn:
    with conn.cursor() as cur:
        cur.execute(f"COPY customers FROM '{customers_data}' DELIMITERS ',' CSV")
        cur.execute(f"COPY employees FROM '{employees_data}' DELIMITERS ',' CSV")
        cur.execute(f"COPY orders FROM '{orders_data}' DELIMITERS ',' CSV")
