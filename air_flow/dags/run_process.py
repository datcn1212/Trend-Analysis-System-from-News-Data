from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

dag = DAG(
    'run_process',
    description='DAG to run a Bash script',
    start_date=datetime(2023, 7, 23),
    schedule_interval='50 7 * * *', 
    catchup=False, 
)

run_bash_script = BashOperator(
    task_id='run_bash_script',
    bash_command='cd /home/canada/DATN_CND/DATN && ',
    dag=dag
)
