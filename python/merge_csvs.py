import os
import re
import pandas as pd

folder_path = '' # folder with csvs file

df_base = pd.DataFrame()

for file in os.listdir(folder_path):

    df = pd.read_csv(folder_path + '/' + file, sep = '\t')

    pattern = r"df_cluster_(.*?)_(?=\d)"

    result = re.search(pattern, file)

    attribute = result.group(1)

    df['attribute'] = attribute

    df_base = pd.concat([df_base, df], ignore_index=True)

df_base.to_csv('',                  # path for new file
               sep = '\t',
               index=False,
               index_label=False)
