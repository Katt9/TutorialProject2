import json
from data_explorer.data.schema import Schema

class InvalidJSONError(Exception):
    pass

def load_schema(filename):
    #1. Load json file that is passed in
    with open(filename, 'r') as json_file:
        json_content = json.load(json_file)
    #2. Check "meta" attribute to make sure it is type "schema"
    json_type = json_content["meta"]["type"]
    json_data = json_content["data"]
    if json_type != "schema":
        raise InvalidJSONError(f"Invalid JSON type in meta. Expected 'schema', got '{json_type}'")
    #3. Create schema object from json "data" attribute
    schema = Schema(len(json_data), json_data)
    #4 Return schema object
    return schema