from data_explorer.seed.schema import Schema
import json

with open('./tests/seed/test_schema.json', 'r') as json_file:
    json_data = json.load(json_file)

def test_init():
    print(json_data)
    test_schema = Schema('test cols', 'test types')
    assert test_schema.num_of_columns == 'test cols'
    assert test_schema.types == 'test types'