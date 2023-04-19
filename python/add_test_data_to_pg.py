import psycopg2
from get_env import get_env_data_as_dict

env = get_env_data_as_dict('../.env')

connection = psycopg2.connect(
	user = env['PG_USER'],
	password = env['PG_PWD'],
	host = '127.0.0.1',
	port = '5432',
	database = 'hh_data'
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM fkb_dwh_ml.t_settings_main;")
record = cursor.fetchone()
print(record)