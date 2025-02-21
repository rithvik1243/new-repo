from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime,timedelta

default_args={
    'owner':'rithvik',
    'retries':5,
    'retry_delay':timedelta(minutes=2)
}

with DAG(
    dag_id='postgres_example_v2',
    default_args=default_args,
    start_date=datetime(2025, 2, 17),
    schedule_interval='@daily',
    catchup=False,
) as dag:
    
    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgres',  # Connection ID from Airflow UI
        sql="""
        CREATE TABLE IF NOT EXISTS mt24061_example_table (
            id SERIAL PRIMARY KEY,
            name varchar NOT NULL
        );
        """,
    )

    create_table
