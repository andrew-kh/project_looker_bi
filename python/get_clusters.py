import requests
import pandas as pd

def return_cluster_df(cluster_key: str) -> pd.core.frame.DataFrame:
    """Return a pd dataframe for a specific cluster by its name"""
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
        'item': {
            'cluster_id': 0
        },
        'specialization': {
            'cluster_id': 2,
            'key_type': 'int'
        },
        'industry': {
            'cluster_id': 3,
            'key_type': 'int'
        },
        'experience': {
            'cluster_id': 4,
            'key_type': 'str'
        },
        'employment': {
            'cluster_id': 5,
            'key_type': 'str'
        },
        'schedule': {
            'cluster_id': 6,
            'key_type': 'str'
        },
        'label': {
            'cluster_id': 7,
            'key_type': 'str'
        },
        'professional_role': {
            'cluster_id': 8,
            'key_type': 'int'
        }
    }
    cluster_items = clusters[clusters_map[cluster_key]['cluster_id']]['items']
    df = pd.DataFrame(cluster_items)
    return(df)

df_items = return_cluster_df('employment')
df_specialization = return_cluster_df('employment')
df_items = return_cluster_df('employment')
df_items = return_cluster_df('employment')
df_items = return_cluster_df('employment')
df_specialization = return_cluster_df('employment')
df_items = return_cluster_df('employment')
df_items = return_cluster_df('employment')