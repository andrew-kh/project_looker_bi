import os
import re
import pandas as pd

folder_path = '/mnt/c/Users/koval/vs-projects/hh_data/new_csvs'

file = 'df_cluster_experiences_1681710832.txt'

df = pd.read_csv(folder_path + '/' + file, sep = '\t')

pattern = r"df_cluster_(.*?)_(?=\d)"
result = re.search(pattern, file)
attribute = result.group(1)
df['attribute'] = attribute
print(df.head(3))