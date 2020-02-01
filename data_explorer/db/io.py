import pandas as pd


def read_file(filename):
    df = pd.read_csv(filename, encoding='ISO-8859-1')
    return df


def validate_data(dataframe, schema):
    pass
    # 1. create schema object from file (function in seed.py)
    # 2. check dataframe using schema class function
    # 3. return true or false based on result


# this function assumes that data has passed validation
def load_data(dataframe, connection):
    pass
    # 1. set query
    # 2. run query through connection
