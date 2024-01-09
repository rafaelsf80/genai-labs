""" Download StackOverflow public data from BigQuery, and create a JSONL file ready to use in tunning as input file 
"""
    
import pandas as pd
from typing import Union

from google.cloud import aiplatform, bigquery

def run_bq_query(sql: str) -> Union[str, pd.DataFrame]:
    """
    Run a BigQuery query and return the job ID or result as a DataFrame
    Args:
        sql: SQL query, as a string, to execute in BigQuery
    Returns:
        df: DataFrame of results from query,  or error, if any
    """

    bq_client = bigquery.Client()

    # Try dry run before executing query to catch any errors
    job_config = bigquery.QueryJobConfig(dry_run=True, use_query_cache=False)
    bq_client.query(sql, job_config=job_config)

    # If dry run succeeds without errors, proceed to run query
    job_config = bigquery.QueryJobConfig()
    client_result = bq_client.query(sql, job_config=job_config)

    job_id = client_result.job_id

    # Wait for query/job to finish running. then get & return data frame
    df = client_result.result().to_arrow().to_pandas()
    print(f"Finished job_id: {job_id}")
    return df

df = run_bq_query(
    """
SELECT
    CONCAT(q.title, q.body) as input_text,
    a.body AS output_text
FROM
    `bigquery-public-data.stackoverflow.posts_questions` q
JOIN
    `bigquery-public-data.stackoverflow.posts_answers` a
ON
    q.accepted_answer_id = a.id
WHERE 
    q.accepted_answer_id IS NOT NULL AND 
    REGEXP_CONTAINS(q.tags, "python") AND
    a.creation_date >= "2020-01-01"
LIMIT 
    50000
"""
)

df.head()

print(len(df))

# For tuning, the training data first needs to be converted into a JSONL format.
df_jsonl = df.to_json(orient="records", lines=True)

print(f"Length: {len(df_jsonl)}")

print(df_jsonl[0:100])

training_data_filename = "training_data_stack_overflow_python_qa.jsonl"

with open(training_data_filename, "w") as f:
    f.write(df_jsonl)

print("DONE: you must now upload the jsonl file to GCS and then proceed for tuning")