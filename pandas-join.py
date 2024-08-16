import pandas as pd

customers_file = 'data-engineering-essentials/035 Python Essentials for Data Engineers/03 Python Collections for Data Engineering/data/retail_db/customers/part-00000'
orders_file = 'data-engineering-essentials/035 Python Essentials for Data Engineers/03 Python Collections for Data Engineering/data/retail_db/orders/part-00000'

customers_file_column_names = ['customer_id', 'first_name', 'last_name', 'unknown_1', 'unknown_2', 'street_address', 'city', 'state', 'postal_code']
orders_file_column_names = ['order_id', 'order_date_timestamp', 'order_customer_id', 'order_status']

# load file into dataframe
def read_file(filename, column_names):
    return pd.read_csv(filename, names=column_names, header=None)

#print(read_file(customers_file, customers_file_column_names))
#print(read_file(orders_file, orders_file_column_names))

customers_df = read_file(customers_file, customers_file_column_names)
orders_df = read_file(orders_file, orders_file_column_names)

print(customers_df)
print(orders_df)


# set the index for joining the dataframes
def set_up_index(df, index_key):
    return df.set_index(index_key)

customers_df_indexed = set_up_index(customers_df, 'customer_id')
orders_df_indexed = set_up_index(orders_df, 'order_id')

customers_with_orders_df = customers_df_indexed.join(orders_df_indexed, on='customer_id', how='inner')

# sort by column
print(customers_with_orders_df.sort_values(by='order_status', ascending=True))

# aggregation - count per order status
count_per_order_status_df = customers_with_orders_df.reset_index(names='customer_id').groupby('order_status')['order_status'].agg(order_status_count='count')

# write to csv
import os

fpath = 'data-engineering-essentials/035 Python Essentials for Data Engineers/03 Python Collections for Data Engineering/data/retail_db'
os.makedirs(fpath, exist_ok=True)
count_per_order_status_df.to_csv(f'{fpath}/out.csv')




