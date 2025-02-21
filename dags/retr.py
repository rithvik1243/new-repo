import psycopg2
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.hooks.base_hook import BaseHook
from datetime import datetime
 
def fetch_data_from_postgres():
    conn_id = "postgres" 
    
    conn = BaseHook.get_connection(conn_id)
 
    # Connect to PostgreSQL using psycopg2
    connection = psycopg2.connect(
        host=conn.host,         
        database=conn.schema,   
        user=conn.login,        
        password=conn.password  
    )
 
    cursor = connection.cursor()
    
    query = "SELECT * FROM mt24061employee";
    
    cursor.execute(query)
    records = cursor.fetchall()
 
    for record in records:
        print(record)
 
    cursor.close()
    connection.close()
 
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025,2, 17),
    'retries': 3
}

with DAG(
    dag_id='postgres_fetch_dag__v2',
    default_args=default_args,
    schedule_interval='@daily',  
) as dag:
 
    fetch_postgres_data_task = PythonOperator(
        task_id='fetch_postgres_data',
        python_callable=fetch_data_from_postgres,
    )
 
fetch_postgres_data_task
 
 
 