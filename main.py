from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
from pandas_gbq import gbq
from google.oauth2 import service_account
from google.cloud import storage
import os
import io
import pandas as pd


def update_data_file(event):
  project = 'your-gcp-project'
  credentials = GoogleCredentials.get_application_default()
  service = discovery.build('storage', 'v1', credentials=credentials)
  sql = """
        Your Query Here (BigQuery)
          """
  df = gbq.read_gbq(sql, project_id=project)
  df_file = df.to_csv('gs://your-storage-bucket/file.csv', line_terminator="\n")
  return
