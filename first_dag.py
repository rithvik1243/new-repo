from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator  

default_args = {
    'owner': 'rithvik',  # Updated the owner name
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}
# hi rithvik
def greet(ti, **kwargs):
    conf = kwargs.get('dag_run').conf
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    if conf:
        print(f"Received configuration in get_name: {conf}")
    print(f"My name is {first_name} {last_name}, and I am {age} years old!")

def get_name(ti):
    first_name = ti.xcom_push(key='first_name', value='rithvik')  # Updated name
    last_name = ti.xcom_push(key='last_name', value='modak')  # Updated name

def get_age(ti):
    age = ti.xcom_push(key='age', value=24)  # Updated age

with DAG(
    dag_id='dag_python_operator_v0',
    description='This is our first DAG',
    default_args=default_args,
    start_date=datetime(2025,2, 17),
    schedule_interval='@daily'
) as dag:

    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet
    )
    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )
    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )

    [task3, task2] >> task1
