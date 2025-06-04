import pandas as pd

# Read the CSV file
df = pd.read_csv('train_data.csv')

# Compress the CSV file using gzip
df.to_csv('train_data.csv.gzip', compression='gzip', index=False)

# To read the compressed CSV file
# df_compressed = pd.read_csv('test_data.csv.gzip', compression='gzip')