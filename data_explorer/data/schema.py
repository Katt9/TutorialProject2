class Schema:
    def __init__(self, num_of_columns, rules):
        self.num_of_columns = num_of_columns
        self.rules = rules

    def check_dataframe(self, dataframe):
        # check num cols and col types
        self.num_of_columns == dataframe.shape[1]
        # take list of types and process data from list
        dataframe_columns = dataframe.columns
        for df_col in dataframe_columns:
            #1. check data_type
            if ! self.check_type():
            #2. check additional rules
            if ! self.check_greater_equal(): # complete conditions
                pass