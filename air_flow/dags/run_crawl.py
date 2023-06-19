from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

# Define the DAG
dag = DAG(
    'bash_script',
    description='DAG to run a Bash script',
    start_date=datetime(2023, 6, 18),
    schedule_interval=None
)

run_bash_script = BashOperator(
    task_id='run_bash_script',
    bash_command='pwd && cd ../crawler && scrapy crawl crawler2',
    dag=dag
)

run_bash_script
