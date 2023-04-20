import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from get_env import get_env_data_as_dict

env = get_env_data_as_dict('../.env')

engine = create_engine(f'postgresql+psycopg2://{env["PG_USER"]}:{env["PG_PWD"]}@127.0.0.1/hh_data')

df = pd.read_csv('/usr/project_looker_bi/misc/hh_test_data.csv', sep='\t')

df = df.rename(columns={
    'name':'cluster_name',
    'url':'cluster_url',
    'count':'cluster_count',
    'request_dt':'request_time',
    'attribute':'attribute_name',
    })

df.to_sql('clusters', con=engine, if_exists='append', schema='dev', index=False)