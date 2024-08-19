import sys
import os

args = sys.argv

# print(f'First argument: {args[0]}')
# print(f'Second argument: {args[1]}')
host = os.environ.get('HOST')
print(f'Connected to environment: {host}')