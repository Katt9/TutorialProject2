class Schema:
    def __init__(self, num_of_columns, rules):
        self.num_of_columns = num_of_columns
        self.rules = rules

    ####################################################################
    # Input
    #   dataframe: pandas DataFrame object
    # Output
    #   boolean based on whether or not dataframe passes schema rules
    ####################################################################
    def check_dataframe(self, dataframe):
        # 1. check if number of columns in dataframe == self.num_of_columns
        self.num_of_columns == dataframe.shape[1]
        #   1.1. if true, iterate through rules
        #       1.1.1. for each rule, check that type matches dataframe column type
        #               e.g. dataframe[<name>].dtype == <type>
        #       1.1.2. if rule contains "greater_equal" key, check that all values
        #               in dataframe column are greater than or equal to the
        #               given value
        #               e.g. (dataframe[<name>] >= <value>).all()
        #       1.1.3. if either of the above is false, return False
        #               otherwise, return true
        #   1.2. if false, return False
        # take list of types and process data from list
        dataframe_columns = dataframe.columns
        for df_col in dataframe_columns:
            #1. check data_type
            if not self.check_type():
                pass
            #2. check additional rules
            if not self.check_greater_equal(): # complete conditions
                pass