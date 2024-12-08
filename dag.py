from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define Python functions for ETL tasks
def extract_data(**kwargs):
    print("Extracting data...")
    return "Data extracted!"

def transform_data(**kwargs):
    print("Transforming data...")
    return "Data transformed!"

def load_data(**kwargs):
    print("Loading data...")
    return "Data loaded!"

# Define the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}
with DAG(
    dag_id='sample_etl_dag',
    default_args=default_args,
    description='A simple ETL process DAG',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['example', 'etl'],
) as dag:

    # Define tasks
    start = DummyOperator(task_id='start')

    extract = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
    )

    transform = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
    )

    load = PythonOperator(
        task_id='load_data',
        python_callable=load_data,
    )

    end = DummyOperator(task_id='end')

    # Define the task dependencies
    start >> extract >> transform >> load >> end
