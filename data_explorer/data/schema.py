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

    def check_num_of_columns(self, num_dataframe_cols):
        return self.num_of_columns == num_dataframe_cols

    def check_type(self, rule, dataframe):
        name = rule['name']
        data_type = rule['type']
        return dataframe[name].dtype == data_type

    def check_greater_equal(self, rule, dataframe):
        if 'greater_equal' in rule.keys():
            name = rule['name']
            value = rule['greater_equal']
            if (dataframe[name] >= value).all():
                return True
            else:
                return False
        else:
            return True

    def check_dataframe(self, dataframe):
        num_dataframe_cols = dataframe.shape[1]
        if self.check_num_of_columns(num_dataframe_cols):
            return self.check_dataframe_columns(dataframe)
        else:
            print("Dataframe does not contain correct number of columns!")
            return False

    def check_dataframe_columns(self, dataframe):
        for rule in self.rules:
            if self.check_type(rule, dataframe):
                if not self.check_greater_equal(rule, dataframe):
                    print(f"Dataframe failed greater equal check on column {rule['name']}")
                    return False
            else:
                print(f"Dataframe failed type check on column {rule['name']}")
                return False
        return True