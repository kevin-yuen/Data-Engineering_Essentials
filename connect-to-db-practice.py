import pandas as pd
import sqlalchemy as sa
import psycopg2 as pc

conn_uri = 'postgresql://postgres:T%40lipz123@localhost:5432/itversity_retail_db'

output = pd.read_sql('orders', conn_uri)
print(output)