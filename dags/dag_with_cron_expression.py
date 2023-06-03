from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'venkatasatya9',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


with DAG(
    dag_id='dag_with_cron_expression_v04',
    default_args=default_args,
    description='This is the dag with CRON expression.',
    start_date=datetime(2023, 5, 15),
    schedule_interval='0 3 * * Tue-Fri'
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo DAG with CRON expression'
    )
