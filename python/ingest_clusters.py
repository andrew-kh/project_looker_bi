#! /usr/bin python3
import requests
import pandas as pd
from sqlalchemy import create_engine
from get_env import get_env_data_as_dict

env = get_env_data_as_dict('/usr/project_looker_bi//.env')
engine = create_engine(f'postgresql+psycopg2://{env["PG_USER"]}:{env["PG_PWD"]}@127.0.0.1/hh_data')

VACANCIES_LINK = 'https://api.hh.ru/vacancies'
VACANCIES_PARAMS = {
    'page': 0, # max 20
    'per_page': 0, # max 100
    'clusters': 'true',
    'locale': 'EN'
}
employer_vacancies_r = requests.get(VACANCIES_LINK, VACANCIES_PARAMS)
employer_vacancies = employer_vacancies_r.json()
clusters = employer_vacancies['clusters']
clusters_map = {
    'item': 0,
    'specialization': 2,
    'industry': 3,
    'experience': 4,
    'employment': 5,
    'schedule': 6,
    'label': 7,
    'professional_role': 8
}
df_base = pd.DataFrame()
for cluster_key in clusters_map.keys():
    cluster_items = clusters[clusters_map[cluster_key]]['items']
    df = pd.DataFrame(cluster_items)
    df['attribute'] = cluster_key
    df_base = pd.concat([df_base, df], ignore_index=True)

df = df.rename(columns={
    'name':'cluster_name',
    'url':'cluster_url',
    'count':'cluster_count',
    'request_dt':'request_time',
    'attribute':'attribute_name',
    })

df.to_sql('clusters', con=engine, if_exists='append', schema='dev', index=False)