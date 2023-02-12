from google.cloud import bigquery
import pandas as pd

def test_load(request):
  
  df = pd.DataFrame(
      {
          "emp_id": ["t1", "t2"],
          "emp_name": ["a1", "a1"],
          "count": [1, 2],
          "insert_dt": [pd.Timestamp.now(), pd.Timestamp.now()]
      }
  )


  table_id = "project_id.dataset_id.table_id"

  client = bigquery.Client()
  table = client.get_table(table_id)
  errors = client.insert_rows_from_dataframe(table, df)

  if errors == []:
    return('ok', 200)
  else:
    return('error', 400)
