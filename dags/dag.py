from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from prediction import NewsPredictor
from webscrapping import WebScraper
from report import DataReporter
from database import DataBase

default_args = {
    'owner': 'tu_nombre',
    'start_date': datetime(2023, 9, 12, 6, 0, 0),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'web_scraping_and_prediction',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    catchup=False,
)

def run_web_scraper():
    WebScraper()

web_scraping_task = PythonOperator(
    task_id='web_scraping_task',
    python_callable=run_web_scraper,
    dag=dag,
)

def run_prediction():
    NewsPredictor()

prediction_task = PythonOperator(
    task_id='prediction_task',
    python_callable=run_prediction,
    dag=dag,
)

def run_database():
    DataBase()

database_task = PythonOperator(
    task_id='database_task',
    python_callable=run_database,
    dag=dag,
)

def run_report():
    DataReporter()

report_task = PythonOperator(
    task_id='report_task',
    python_callable=run_report,
    dag=dag,
)

web_scraping_task >> prediction_task  >> database_task >> report_task

if __name__ == "__main__":
    dag.cli()