import pandas as pd

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

    # def check_dataframe_old(self):
    #     if self.check_num_of_columns:
    #         for self.rule in self.rules:
    #             self.name = self.rule['name']
    #             self.type = self.rule['type']
    #             if self.check_type:
    #                 greater_equal = self.rule['greater_equal']
    #                 if not (self.dataframe[greater_equal] >= greater_equal).all():
    #                     return False

    def check_dataframe(self, dataframe):
        num_dataframe_cols = dataframe.shape[1]
        if self.check_num_of_columns(num_dataframe_cols):
            return self.check_dataframe_columns(dataframe)
        else:
            return False

    def check_dataframe_columns(self, dataframe):
        for rule in self.rules:
            if self.check_type(rule, dataframe):
                if not self.check_greater_equal(rule, dataframe):
                    return False
            else:
                return False
        return True

        #dataframe_columns = self.dataframe.columns
        #for df_col in dataframe_columns:
            #1. check data_type
        #    if not self.check_type:
        #        pass
            #2. check additional rules
        #    if not self.check_greater_equal: # complete conditions
        #        pass

    # # def check_dataframe(self, dataframe): # restructure func. into multi. smaller funcs.
    #     # 1. check if number of columns in dataframe == self.num_of_columns
    #     if self.num_of_columns == self.dataframe.shape[1]:
    #     #   1.1. if true, iterate through rules
    #         for rule in self.rules:
    #     #       1.1.1. for each rule, check that type matches dataframe column type
    #     #               e.g. dataframe[<name>].dtype == <type>
    #             name = rule['name']
    #             type = rule['type']
    #             if self.dataframe[name].dtype == type:
    #         #       1.1.2. if rule contains "greater_equal" key, check that all values
    #                 if 'greater_equal' in rule.keys():
    #                     greater_equal = rule['greater_equal']
    #                     if not (self.dataframe[greater_equal] >= greater_equal).all():
    #                         return False
    #             else:
    #                 return False
    #         return True
    #     else:
    #         return False
    #
    #
    #     #               in dataframe column are greater than or equal to the
    #     #               given value
    #     #               e.g. (dataframe[<name>] >= <value>).all()
    #     #       1.1.3. if either of the above is false, return False
    #     #               otherwise, return true
    #     #   1.2. if false, return False
    #     # take list of types and process data from list
    #     dataframe_columns = self.dataframe.columns
    #     for df_col in dataframe_columns:
    #         #1. check data_type
    #         if not self.check_type():
    #             pass
    #         #2. check additional rules
    #         if not self.check_greater_equal(): # complete conditions
    #             pass