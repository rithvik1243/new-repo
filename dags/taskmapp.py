from airflow import DAG
from airflow.decorators import task
from datetime import datetime, timedelta

default_args = {
    'owner': 'rithvik',  # Updated owner name
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='dynamic_task_mapping_employee_experience_v3',
    description='This is dynamic task mapping',
    default_args=default_args,
    start_date=datetime(2025, 2, 17),  # Updated start date
    schedule_interval='@daily'
) as dag:

    employees = [
        {"id": 1, "name": "Arjun Desai", "experience": 3, "department": "HR"},  # Updated name
        {"id": 2, "name": "Vishal Gupta", "experience": 8, "department": "Engineering"},  # Updated name
        {"id": 3, "name": "Nikhil Sharma", "experience": 2, "department": "Sales"},  # Updated name
        {"id": 4, "name": "Aaryan Patel", "experience": 10, "department": "Marketing"}  # Updated name
    ]

    @task
    def validate_employee(employee: dict):
        if "id" in employee and "name" in employee and "experience" in employee and "department" in employee:
            return employee
        else:
            raise ValueError(f"Incomplete employee record: {employee}")

    @task
    def categorize_employee(employee: dict):
        category = "Junior" if employee["experience"] < 5 else "Senior"
        return {"name": employee["name"], "category": category}

    @task
    def notify_employee_category(employee_info: dict):
        return f"Notification sent to {employee_info['name']}: You are categorized as {employee_info['category']}."

    validated_employees = validate_employee.expand(employee=employees)
    categorized_employees = categorize_employee.expand(employee=validated_employees)
    notifications = notify_employee_category.expand(employee_info=categorized_employees)
