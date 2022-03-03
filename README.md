# BigQuery-GoogleStorageBucketCSV

This file was created to be a Google Cloud Function that takes data from BigQuery and exports it into a CSV file in a Google Cloud Storage Bucket
All you have to change is the following
  - Replace your-gcp-project with your project
  - Enter your query in the sql variable
  - In the df_file variable, replace with your "gs://gcp-bucket/filename.csv"

It can be run on a schedule using Google Cloud Scheduler
