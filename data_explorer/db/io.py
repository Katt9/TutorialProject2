from data_explorer.data.schema import Schema
from data_explorer.data.seed import load_schema
import pandas as pd


def read_file(filename):
    df = pd.read_csv(filename, encoding='ISO-8859-1')
    return df


def validate_data(dataframe, schema_file): # complete, research sql_alchemy
    # 1. create schema object from file (function in seed.py)
    schema = load_schema(schema_file)
    # 2. check dataframe using schema class function

    # 3. return true or false based on result
    return schema.check_dataframe(dataframe)


# this function assumes that data has passed validation
def load_data(dataframe, connection):
    # 1. set query
    query = "select * from tbl"
    # 2. run query through connection
    engine = create_engine('postgresql+psycopg2://aadadey:@localhost/susb')
    result = engine.execute(query)