from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.utils.task_group import TaskGroup
from airflow.utils.trigger_rule import TriggerRule

# Updated employee data with 5 rows
employee_data = [
    {'name': 'Rithvik Modak', 'age': 24, 'city': 'Hyderabad', 'state': 'Telangana', 'country': 'India', 'salary': 12000},
    {'name': 'Kiran Patil', 'age': 29, 'city': 'Mumbai', 'state': 'Maharashtra', 'country': 'India', 'salary': 15000},
    {'name': 'Arjun Patel', 'age': 35, 'city': 'Bengaluru', 'state': 'Karnataka', 'country': 'India', 'salary': 250000},
    {'name': 'Neha Agarwal', 'age': 27, 'city': 'Pune', 'state': 'Maharashtra', 'country': 'India', 'salary': 18000},
    {'name': 'Ravi Kumar', 'age': 32, 'city': 'Chennai', 'state': 'Tamil Nadu', 'country': 'India', 'salary': 22000},
]

def setup_task():
    print("Setting up the environment: Loading initial data or configurations.")

def transform_employee_data():
    global employee_data
    transformed_data = [{'name': employee['name'].upper(), 'age': employee['age'], 'city': employee['city'], 
                         'state': employee['state'], 'country': employee['country'], 
                         'salary': employee['salary'] * 1.10} for employee in employee_data]
    print(f"Transformed employee data: {transformed_data}")
    return transformed_data

def calculate_average_salary():
    global employee_data
    average_salary = sum(employee['salary'] for employee in employee_data) / len(employee_data)
    print(f"Average Salary of Employees: {average_salary}")
    return average_salary

def teardown_task():
    print("Cleaning up the environment: closing resources or sending notifications.")

default_args = {
    'owner': 'rithvik',  # Updated owner name
    'retries': 0,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='employee_data_processing_v5',
    description='Set up and Tear down Tasks',
    default_args=default_args,
    start_date=datetime(2025, 1, 21),
    schedule_interval='@daily',
    catchup=False,
) as dag:

    setup = PythonOperator(
        task_id='setup_task',
        python_callable=setup_task,
    )
    transform_data = PythonOperator(
        task_id='transform_employee_data',
        python_callable=transform_employee_data,
    )

    calculate_avg_salary = PythonOperator(
        task_id='calculate_average_salary',
        python_callable=calculate_average_salary,
    )

    teardown = PythonOperator(
        task_id='teardown_task',
        python_callable=teardown_task,
        trigger_rule=TriggerRule.ALL_DONE, 
    )

    setup >> transform_data >> calculate_avg_salary >> teardown
