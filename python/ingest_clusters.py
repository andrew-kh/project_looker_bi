#! /usr/bin python3
import requests
import time
import pandas as pd
from sqlalchemy import create_engine
from get_env import get_env_data_as_dict

env = get_env_data_as_dict('/usr/project_looker_bi/.env')
engine = create_engine(f'postgresql+psycopg2://{env["PG_USER"]}:{env["PG_PWD"]}@127.0.0.1/hh_data')

VACANCIES_LINK = 'https://api.hh.ru/vacancies'
VACANCIES_PARAMS = {
    'page': 0, # max 20
    'per_page': 0, # max 100
    'clusters': 'true',
    'locale': 'EN'
}

request_dt = int(time.time())
employer_vacancies_r = requests.get(VACANCIES_LINK, VACANCIES_PARAMS)
employer_vacancies = employer_vacancies_r.json()
clusters = employer_vacancies['clusters']

list_dfs = []

for i in clusters:
    cluster_items = i['items']
    df_cluster = pd.DataFrame(cluster_items)
    df_cluster['attribute'] = i['id']
    df_cluster['request_dt'] = request_dt
    list_dfs.append(df_cluster)

df = pd.concat(list_dfs)

df = df.rename(columns={
    'name':'cluster_name',
    'url':'cluster_url',
    'count':'cluster_count',
    'request_dt':'request_time',
    'attribute':'attribute_name',
    })

df.to_sql('clusters', con=engine, if_exists='append', schema='dev', index=False)

with engine.connect() as con:
    con.execute("update dev.clusters set request_timestamp = to_timestamp(request_time) at time zone 'msk' where request_timestamp is null")