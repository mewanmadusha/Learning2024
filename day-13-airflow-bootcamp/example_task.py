from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'mewan',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'my_dag_id',
    default_args=default_args,
    description='My example DAG',
    schedule_interval=timedelta(days=1),
)

def my_python_function():
    print("Hello, Airflow!")

run_this = PythonOperator(
    task_id='example_task',
    python_callable=my_python_function,
    dag=dag,
)
