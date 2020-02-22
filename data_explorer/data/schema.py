import pandas as pd

class Schema:
    def __init__(self, dataframe, num_of_columns, rules):
        self.dataframe = dataframe
        self.num_of_columns = num_of_columns
        self.rules = rules
        self.rule = ''
        self.name = ''
        self.type = ''

    ####################################################################
    # Input
    #   dataframe: pandas DataFrame object
    # Output
    #   boolean based on whether or not dataframe passes schema rules
    ####################################################################

    @property
    def check_num_of_columns(self):
        return self.num_of_columns == self.dataframe.shape[1]

   @property
   def check_type(self):
       return self.dataframe[self.name].dtype == self.type

    @property
    def check_greater_equal(self):
        return 'greater_equal' in self.rule.keys()

    def check_dataframe(self):
        if self.check_num_of_columns:
            for self.rule in self.rules:
                self.name = rule['name']
                self.type = rule['type']
                if self.check_type:
                    greater_equal = self.rule['greater_equal']
                    if not (self.dataframe[greater_equal] >= greater_equal).all():
                        return False

    def check_dataframe_columns(self):
        dataframe_columns = self.dataframe.columns
        for df_col in dataframe_columns:
            #1. check data_type
            if not self.check_type:
                pass
            #2. check additional rules
            if not self.check_greater_equal: # complete conditions
                pass

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