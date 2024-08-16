import json

json_file = open("data-engineering-essentials/035 Python Essentials for Data Engineers/04 Data Processing using Pandas/data/retail_db/schemas.json", 'r')
data_json_fmt = json.load(json_file)

print(data_json_fmt)
print(data_json_fmt['categories'])
print(sorted(data_json_fmt['categories'], key=lambda col_pos: col_pos['column_position'], reverse=True))

print('------------ Sort the selected schema\'s column ------------')
schema_name = input('Enter a schema name that you want to sort: ')
schema_to_sort = data_json_fmt[schema_name]

sorting_key = input('Enter a key to sort: ')
print(sorted(schema_to_sort, key=lambda col_name: col_name[sorting_key], reverse=True))
