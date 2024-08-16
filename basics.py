orders_file = open(
    'data-engineering-essentials/035 Python Essentials for Data Engineers/03 Python Collections for Data Engineering/data/retail_db/orders/part-00000')
read_orders_file = orders_file.read()
orders_file_list_fmt = read_orders_file.splitlines()

print(orders_file_list_fmt[1:10])

print('---------- COMPLETE ORDERS ONLY ----------')
complete_orders_list = list(filter(lambda order: order.split(",")[-1] == 'COMPLETE',orders_file_list_fmt))
print(complete_orders_list[1:10])

print('--------- UNIQUE ORDER STATUS ---------')
unique_order_status = set(map(lambda order: order.split(',')[-1], orders_file_list_fmt))
print(unique_order_status)

print('--------- SORTED ORDERS LIST ---------')
sorted_orders_list = sorted(orders_file_list_fmt, key=lambda order: order.split(',')[2])
print(sorted_orders_list[:20])

print('--------- REVERSE SORTED ORDERS LIST ---------')
reverse_sorted_orders_list = sorted(orders_file_list_fmt, key=lambda order: order.split(",")[2], reverse=True)
print(reverse_sorted_orders_list[:20])