from data_explorer.data.schema import Schema
import pandas as pd
#import json

# with open('./seed/schemas/test_schema.json', 'r') as json_file:
#     json_data = json.load(json_file)


def test_init():
    # print(json_data)
    test_schema = Schema('test cols', 'test rules')
    assert test_schema.num_of_columns == 'test cols'
    assert test_schema.rules == 'test rules'


def test_check_dataframe():
    data_dict = {
        'entrsize': ['1', '2', '3', '4'],
        'firm': [1, 2, 3, 4],
        'payr': [1, 2, 3, 4]
    }

    test_df = pd.DataFrame(data_dict)
    # load test_schema.json using function in seed.py
    # call check_dataframe with test_df
    # assert result is True
