import warnings 
warnings.filterwarnings('ignore')
import pandas as pd
""" script to get distance data wanted from the all_records.csv file created in import_clean"""



all = pd.read_csv("apple_health_export/all_records.csv")

## get distances
distance_df = all[all['type'] == 'HKQuantityTypeIdentifierDistanceWalkingRunning']


# convert dates to datetime
for date in ['creationDate', 'startDate', 'endDate']:
    distance_df[date] = pd.to_datetime(distance_df[date])



# make distance counts numeric
distance_df.loc[:, 'value'] = pd.to_numeric(distance_df.loc[:, 'value'])

# distance_df = distance_df[distance_df['sourceName'] == 'Karanâ€™s iPhone']
# drop unnecessary columns (all rows, columns 1-8)
distance_df = distance_df.iloc[:, 1:9]

# group distance by date
distance_date = distance_df.groupby(['creationDate']).sum()

# convert/string replace for easier naming
distance_df['type'] = distance_df['type'].str.replace('HKQuantityTypeIdentifier', '')

# write to csv
distance_df.to_csv("data/dist.csv", index=False)