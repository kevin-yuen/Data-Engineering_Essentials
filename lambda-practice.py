# Author: Kevin Yuen
# Github username: kevin-yuen
# Date: 8/15/2024
# Description: Practice filter and sort datasets with lambda function

import json

filepath = 'data-engineering-essentials/035 Python Essentials for Data Engineers/03 Python Collections for Data Engineering/data/retail_db'

# get schemas
schemas_json = json.load(open(f'{filepath}/schemas.json', mode='r'))
schema_names = [schema_name for schema_name in schemas_json]

def verify_directory_name(directory_name):
    if (directory_name in schema_names):
        print(f'directory "{directory_name}" found...opening file...')
    else:
        print('not a valid directory')
        return


if __name__ == '__main__':
    directory_name = input('What data file do you want to open?\n')
    verify_directory_name(directory_name)

    # open the csv file and read it
    data = open(f'{filepath}/{directory_name}/part-00000').read().splitlines()

    # filter data
    last_name_search = input('Enter the customer\'s last name\n')
    output_last_name = list(filter(lambda customer_record: customer_record.split(',')[2] == last_name_search, data))

    if len(output_last_name) > 0:
        print('customers found:')
        print(output_last_name[0:10])
    else:
        print('No customer found')
        print('Exiting the program...')
        exit()

    # sort data
    sort_criteria = input('Enter the column name to sort the table\n')
    sort_method = input('How do you want to sort the table? (ascending/descending)\n')

    for schema in schemas_json:
        if schema == directory_name:
            for metadata in schemas_json[schema]:
                if metadata['column_name'] == sort_criteria:
                    sorted_output = list(sorted(output_last_name, key=lambda customer_record: customer_record.split(',')[1], reverse=True if sort_method == 'descending' else False ))

            print(f'Sorted result: {sorted_output[0:30]}')

    map_output = list(map(lambda record: '1-' + record.split(',')[0], sorted_output))
    print(map_output)

