import requests
import time
import pandas as pd

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

cluster_items = clusters[clusters_map['item']['cluster_id']]['items']
cluster_specializations = clusters[clusters_map['specialization']['cluster_id']]['items']
cluster_items_industries = clusters[clusters_map['industry']['cluster_id']]['items']
cluster_experiences = clusters[clusters_map['experience']['cluster_id']]['items']
cluster_employment_types = clusters[clusters_map['employment']['cluster_id']]['items']
cluster_schedules = clusters[clusters_map['schedule']['cluster_id']]['items']
cluster_labels = clusters[clusters_map['label']['cluster_id']]['items']
cluster_professional_role = clusters[clusters_map['professional_role']['cluster_id']]['items']

df_cluster_items = pd.DataFrame(cluster_items)
df_cluster_specializations = pd.DataFrame(cluster_specializations)
df_cluster_items_industries = pd.DataFrame(cluster_items_industries)
df_cluster_experiences = pd.DataFrame(cluster_experiences)
df_cluster_employment_types = pd.DataFrame(cluster_employment_types)
df_cluster_schedules = pd.DataFrame(cluster_schedules)
df_cluster_labels = pd.DataFrame(cluster_labels)
df_cluster_professional_role = pd.DataFrame(cluster_professional_role)

df_cluster_items['request_dt'] = request_dt
df_cluster_specializations['request_dt'] = request_dt
df_cluster_items_industries['request_dt'] = request_dt
df_cluster_experiences['request_dt'] = request_dt
df_cluster_employment_types['request_dt'] = request_dt
df_cluster_schedules['request_dt'] = request_dt
df_cluster_labels['request_dt'] = request_dt
df_cluster_professional_role['request_dt'] = request_dt

df_cluster_items.to_csv(f'/mnt/c/Users/koval/vs-projects/hh_data/new_csvs/df_cluster_items_{request_dt}.txt', sep = '\t', index=False)
df_cluster_specializations.to_csv(f'/mnt/c/Users/koval/vs-projects/hh_data/new_csvs/df_cluster_specializations_{request_dt}.txt', sep = '\t', index=False)
df_cluster_items_industries.to_csv(f'/mnt/c/Users/koval/vs-projects/hh_data/new_csvs/df_cluster_items_industries_{request_dt}.txt', sep = '\t', index=False)
df_cluster_experiences.to_csv(f'/mnt/c/Users/koval/vs-projects/hh_data/new_csvs/df_cluster_experiences_{request_dt}.txt', sep = '\t', index=False)
df_cluster_employment_types.to_csv(f'/mnt/c/Users/koval/vs-projects/hh_data/new_csvs/df_cluster_employment_types_{request_dt}.txt', sep = '\t', index=False)
df_cluster_schedules.to_csv(f'/mnt/c/Users/koval/vs-projects/hh_data/new_csvs/df_cluster_schedules_{request_dt}.txt', sep = '\t', index=False)
df_cluster_labels.to_csv(f'/mnt/c/Users/koval/vs-projects/hh_data/new_csvs/df_cluster_labels_{request_dt}.txt', sep = '\t', index=False)
df_cluster_professional_role.to_csv(f'/mnt/c/Users/koval/vs-projects/hh_data/new_csvs/df_cluster_professional_role_{request_dt}.txt', sep = '\t', index=False)