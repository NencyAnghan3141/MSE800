import pandas as pd

df = pd.read_parquet('/Users/nencyanghan/Desktop/MSE800/week4/Sample_data_2.parquet')
print(df.head())  # View first few rows
print(f"Total number of records: {len(df)}")

