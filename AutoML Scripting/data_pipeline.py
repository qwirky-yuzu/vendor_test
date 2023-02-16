import pandas as pd
from pycaret.regression import *

class DataPreprocessing:
    """
      Module takes in 2 pandas dataframe objects, merge them and readies a processed dataframe for AutoML.
    """

    def __init__(self, housing_transactions:pd.Dataframe, postal_code:pd.Dataframe):
        self.housing_transactions = housing_transactions
        self.postal_code = postal_code

    def run_basic_cleaning(self):

        df = self.housing_transactions.copy()

        # Basic data cleaning
        # since we are trying to predict psf, all other price features have to be dropped
        df.drop(columns=['Unit Price ($ psm)',
                         'Transacted Price ($)', 'Nett Price($)'], axis=1, inplace=True)

        # for all the column names, lower and replace space with underscore
        df.columns = [c.lower().replace(' ', '_') for c in df.columns]

        # Rename unit_price_($_psf) to price_psf
        df.rename(columns={'unit_price_($_psf)':'price_psf'}, inplace=True)

        # Convert completion date to numeric
        # All uncompleted and unknown units will have its year set to 2023
        df['completion_date'] = df.completion_date.apply(
            lambda x: 2023 if not x[0].isdigit() else int(x))

        # Convert sale date to a workable format
        df.sale_date = df.sale_date.apply(lambda x: pd.to_datetime(x))

        # Convert sale date to component features
        df['year'] = df.sale_date.apply(lambda x: x.year)
        df['month'] = df.sale_date.apply(lambda x: x.month)
        df['day'] = df.sale_date.apply(lambda x: x.day)
        df['weekday'] = df.sale_date.apply(lambda x: x.weekday())

        # create a date_id which is an integer variable to easily represent the dates
        dates = sorted(df.sale_date.drop_duplicates())

        date_dict = {}
        i = 0
        for date in dates:
            date_dict[date] = i
            i += 1
        df['date_id'] = df.sale_date.apply(lambda x: date_dict[x])

        def is_leasehold(x):
            x = x.split(' ')[0]

            if not x.isdigit():
                return 0
            elif int(x) < 900:
                return 1
            else:
                return 1

        df['is_leasehold'] = df.tenure.apply(is_leasehold)
        
        # Combine the lat lon file
        postal_codes.sort_values(by='postal_code')
        df = pd.merge(df, postal_codes, on='postal_code', how='left')

        return df
      
class AutoML:
    """
      Module takes in a pandas dataframe object and loads it into PyCaret.
    """
    
    def __init__(self,data):
        self.data = data
        
    
    def run_model(self):
        model = setup(
            data=self.data,
            target='price_psf',
            normalize=True,
            normalize_method='zscore
            categorical_features=['postal_district', 'postal_sector', 'completion_date', 'day'],
            ignore_features=['project_name', 'address', 'sale_date', 'tenure', 'postal_code'],
        )
        
        compare_models(include=['rf', 'dt', 'lr', 'lightgbm', 'ridge', 'lasso'],
               sort='MAPE'
               )
