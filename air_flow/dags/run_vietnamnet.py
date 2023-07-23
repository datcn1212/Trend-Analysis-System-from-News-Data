from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

dag = DAG(
    'run_vietnamnet',
    description='DAG to run a Bash script',
    start_date=datetime(2023, 7, 23),
    schedule_interval='30 0 * * *',  
    catchup=False, 
)

run_bash_script = BashOperator(
    task_id='run_bash_script',
    bash_command='cd /home/canada/DATN_CND/DATN/crawler && scrapy crawl vietnamnet_main --logfile log_vietnamnet.txt',
    dag=dag
)
