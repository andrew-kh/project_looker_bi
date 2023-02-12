from google.cloud import bigquery
import pandas as pd

def load_clusters(request):
    df = pd.DataFrame(
        {
            "emp_id": ["a"],
            "emp_name": ["b"],
            "count": [1],
            "insert_dt": [pd.Timestamp.now()]
        }
    )

    print('created df\n')

    client = bigquery.Client()
    table_id = ''

    job_config = bigquery.LoadJobConfig(schema=[
        bigquery.SchemaField("emp_id", "STRING"),
        bigquery.SchemaField("emp_name", "STRING"),
        bigquery.SchemaField("insert_dt", "TIMESTAMP")
    ])

    job = client.load_table_from_dataframe(
        df, table_id, job_config=job_config
    )

    return('ok', 200)
