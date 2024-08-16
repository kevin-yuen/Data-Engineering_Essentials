import pandas as pd

order_columns = ['order_id', 'order_date', 'order_customer_id', 'order_status']

df = pd.read_csv(
    'data-engineering-essentials/035 Python Essentials for Data Engineers/03 Python Collections for Data Engineering/data/retail_db/orders/part-00000',
    header=None,
    names=order_columns)
#print(df)

# query data
result = df.query('order_date == "2013-07-25 00:00:00.0" and order_status == ["COMPLETE", "CLOSED"]')
print(result)

# get column names
print(df.columns)

# aggregation - count how many order status
count_result = df.groupby("order_status")["order_id"].agg(order_count="count")
print(count_result)

# aggregation - get count by order month and then by order status
print('---------- aggregation - get count by order month and then by order status ----------')
order_month_result = df.apply(lambda order: order.order_date[:7], axis=1)
count_by_date_result = df.groupby([order_month_result, "order_status"])["order_id"].agg(order_count="count")
print(count_by_date_result)


