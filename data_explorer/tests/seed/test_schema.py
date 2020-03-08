from data_explorer.data.schema import Schema
import pandas as pd
from data_explorer.data.seed import load_schema
import pytest
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

    test_df['firm'] = ['1', '2', '3', '4']
    ch_df = test_schema.check_dataframe(test_df)
    assert ch_df is False

    test_df['new_col'] = ['a', 'b', 'c', 'd']
    ch_df = test_schema.check_dataframe(test_df)
    assert ch_df is False

def test_check_greater_equal():
    test_schema, test_df = setup()
    ch_ge = test_schema.check_greater_equal(test_schema.rules[2], test_df)
    assert ch_ge is True

    test_df.payr = [-2, -1, 0, 1]
    ch_ge = test_schema.check_greater_equal(test_schema.rules[2], test_df)
    assert ch_ge is False

@pytest.mark.parametrize("rule,  result", [
    pytest.param(dict(name='entrsize', type='object'), True),
    pytest.param(dict(name='entrsize', type='int64'), False),
    pytest.param(dict(name='firm', type='int64'), True)])

def test_check_type(rule, result):
    test_schema, test_df = setup()
    ch_t = test_schema.check_type(rule, test_df)
    assert ch_t is result

@pytest.mark.parametrize("num_cols,  result", [
    pytest.param(3, True),
    pytest.param(4, False)])

def test_check_num_of_columns(num_cols, result):
    test_schema, test_df = setup()
    ch_c = test_schema.check_num_of_columns(num_cols)
    assert ch_c is result

@pytest.mark.parametrize("col, col_value,  result", [
    pytest.param("payr", [-2, -1, 0, 1], False),
    pytest.param("firm", ['1', '2', '3', '4'], False),
    pytest.param("firm", [1, 2, 3, 4], True)])

def test_check_dataframe_columns(col, col_value, result):
    test_schema, test_df = setup()
    test_df[col] = col_value
    ch_t = test_schema.check_dataframe_columns(test_df)
    assert ch_t is result