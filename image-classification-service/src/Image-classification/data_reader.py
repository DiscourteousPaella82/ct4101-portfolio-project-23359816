import json

def read_json(pathname):
    with open(pathname, 'r') as file:
        data = json.load(file)
    return data