import pandas as pd

def read_file(filename):
    df = pd.read_csv(filename, encoding='ISO-8859-1')
    return df

def validate_data(dataset):
    pass
    # check number of columns
    # check that each column meets data requirements
        # check data types
        # check for valid ranges
