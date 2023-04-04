import warnings 
warnings.filterwarnings('ignore')
import pandas as pd
import datetime as dt
"""coverting object into datetime"""


def check_dates(df):
    for col in df.columns:
        if df[col].dtype == 'object':
            try:
                df[col] = pd.to_datetime(df[col])
            except ValueError:
                pass
