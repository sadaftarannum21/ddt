import os
from pathlib import Path
import pandas as pd
from pandas import DataFrame
import numpy as np
from datetime import datetime as stamp
import json
import random as rnd

from src.data.models.predictions.ModelMthValueUser import ModelMthValueUser
from src.data.models.predictions.ModelNthUserChurn import ModelNthUserChurn
from src.framework.infra.tools.definitions.definitions import Definitions as D


class SandBox:
    """
    SandBox is an entity that
    , is contained and ideally should be its own unit
    , it should be called only "as needed"
    , it allows trying stuff
    """

    def __init__(self):
        print(r'DEBUG:sandbox.py,SandBox __init__')
        datasource = self.read_json_dump()
        if datasource is not None:
            datadestination = self.modify_json_dump(datasource)
            self.write_json_dump(datadestination)
        else:
            print(f'DEBUG:EXPERIMENTAL:sandbox.py,SandBox datasource is ${datasource}')

    """
        TODO: sandbox.py, speed the eda process by modifying the ds json dump 
        with ml data while the components are achieved to "good enough"
    """

    def read_json_dump(self) -> DataFrame:
        # TODO:sandbox.py, read_json_dump(...), join the file_name = 'zzz'
        print(r'DEBUG:EXPERIMENTAL:sandbox.py,SandBox read_json_dump(...)')
        df = None
        root = os.path.abspath(os.curdir)
        path = f'{root}' + r'\data\dumps - rideshare-mocked\2024-08-22_15-46-19 - dump.json'
        if Path(path).exists():
            try:
                df = pd.read_json(path)
                # for col_i, col in df.items():
                #     for row_j, val in col.items():
                #         print(f'df[   col:[{col_i}],row:[{row_j}],value:[{val}]   ]')
            except ValueError as exception:
                print(f'exception: {exception}')
        return df

    def modify_json_dump(self, ds: DataFrame) -> DataFrame:
        """
        Create a replica of 'ds' DataFrame, initialize with NaN values, and spoof data.
        """
        print(r'DEBUG:EXPERIMENTAL:sandbox.py,SandBox modify_json_dump(...)')

        def fill_data(col_prefix, fill_method, attributes):
            df_list = []
            for attr in attributes:
                col_name = f"{col_prefix}_{attr}"
                df = DataFrame(index=ds.index, columns=[col_name])
                df[:] = np.nan
                data_list = []
                for _ in range(len(df)):
                    data = fill_method()
                    # Check if the attribute is callable and call it
                    # , otherwise access it directly
                    value = getattr(data, attr)
                    if callable(value):
                        value = value()
                    data_list.append(value)
                df[col_name] = data_list
                df_list.append(df)
            return df_list
        p_cols = ['churn_rate', 'users_lost_during_period', 'users_at_start_of_period', 'percent_of_all_users']
        q_cols = ['customer_lifetime_value', 'number_of_customers', 'number_of_purchases',
                  'number_of_unique_customers', 'sum_of_customer_lifespans', 'total_number_of_purchases',
                  'total_revenue']
        # Generate DataFrames for 'Nth(_user_churn)' and 'Mth(_value_user)'
        # with unique column names then concatenate all DataFrames horizontally
        # and finally join with the original DataFrame
        p_dfs = fill_data('Nth', self.fill_N_user_churn, p_cols)
        q_dfs = fill_data('Mth', self.fill_M_value_user, q_cols)
        all_data = pd.concat(p_dfs + q_dfs, axis=D.PANDA_HORIZONTAL_OPERATION)
        result = ds.join(all_data)
        return result

    def write_json_dump(self, dd: DataFrame):
        print(r'DEBUG:EXPERIMENTAL:sandbox.py,SandBox write_json_dump(...)')
        root = os.path.abspath(os.curdir)
        ts = stamp.now().strftime('%Y-%m-%d_%H-%M-%S')
        path = Path(root) / 'data' / 'staged - client'
        path.mkdir(parents=True, exist_ok=True)
        json_file_path = path / f'{ts} - dump.json'
        csv_file_path = path / f'{ts} - dump.csv'
        try:
            with open(json_file_path, 'w') as jsonfile:
                json.dump(dd.to_json(), jsonfile, indent=4)
                dd.to_csv(csv_file_path)
        except (IOError, ValueError) as exception:
            print(f'Exception: {exception}')

    @staticmethod
    def fill_N_user_churn() -> ModelNthUserChurn:
        _N = ModelNthUserChurn()
        _N.users_lost_during_period = rnd.uniform(D.USER_MIN_LOST_DURING, D.USER_MAX_LOST_DURING)
        _N.users_at_start_of_period = rnd.uniform(D.USER_MIN_AT_START, D.USER_MAX_AT_START)
        _N.percent_of_all_users = rnd.uniform(D.USER_MIN_PERCENT_OF_ALL, D.USER_MAX_PERCENT_OF_ALL)
        return _N

    @staticmethod
    def fill_M_value_user() -> ModelMthValueUser:
        _M = ModelMthValueUser()
        _M.total_revenue = rnd.randint(D.USER_MIN_TOTAL_REVENUE, D.USER_MAX_TOTAL_REVENUE)
        _M.number_of_purchases = rnd.randint(D.USER_MIN_PURCHASES, D.USER_MAX_PURCHASES)
        # _M.average_purchase_value()
        _M.total_number_of_purchases = rnd.randint(D.USER_MIN_PURCHASES, D.USER_MAX_PURCHASES)
        _M.number_of_unique_customers = rnd.randint(D.USER_MIN_NUM_UNIQUE, D.USER_MAX_NUM_UNIQUE)
        # _M.average_purchase_frequency()
        _M.sum_of_customer_lifespans = rnd.randint(D.USER_MIN_SUM_LIFESPAN, D.USER_MAX_SUM_LIFESPAN)
        _M.number_of_customers = rnd.randint(D.USER_MIN_NUM_OF_CUSTOMERS, D.USER_MAX_NUM_OF_CUSTOMERS)
        # _M.customer_lifespan()
        return _M
