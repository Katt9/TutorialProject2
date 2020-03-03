from data_explorer.data.schema import Schema
import pandas as pd
from data_explorer.data.seed import load_schema
#import json

# with open('./seed/schemas/test_schema.json', 'r') as json_file:
#     json_data = json.load(json_file)

def setup():
    data_dict = {
        'entrsize': ['1', '2', '3', '4'],
        'firm': [1, 2, 3, 4],
        'payr': [1, 2, 3, 4]
    }
    filename = './seed/schemas/test_schema.json'
    test_df = pd.DataFrame(data_dict)
    # load test_schema.json using function in seed.py
    test_schema = load_schema(filename)
    return test_schema, test_df

def test_init():
    # print(json_data)
    test_schema = Schema('test cols', 'test rules')
    assert test_schema.num_of_columns == 'test cols'
    assert test_schema.rules == 'test rules'

def test_check_dataframe(): # complete test_schema
    test_schema, test_df = setup()
    # call check_dataframe with test_df
    ch_df = test_schema.check_dataframe(test_df)
    # assert result is True
    assert ch_df is True

def test_check_greater_equal():
    test_schema, test_df = setup()
    ch_ge = test_schema.check_greater_equal(test_schema.rules[2], test_df)
    assert ch_ge is True

    test_df.payr = [-2, -1, 0, 1]
    ch_ge = test_schema.check_greater_equal(test_schema.rules[2], test_df)
    assert ch_ge is False

def test_check_type():
    test_schema, test_df = setup()
    ch_t = test_schema.check_type(test_schema.rules[1], test_df)
    assert ch_t is True
