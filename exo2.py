from datetime import datetime

from airflow import DAG
from airflow.models import Variable
from airflow.operators.python import PythonOperator


def afficher_variables():
    environment = Variable.get("environment")
    data_path = Variable.get("data_path")

    print(f"Environment : {environment}")
    print(f"Data Path   : {data_path}")


with DAG(
    dag_id="exercice_6",
    start_date=datetime(2026, 11, 8),
    schedule=None,
    catchup=False,
    tags=["formation"],
) as dag:

    lecture_variables = PythonOperator(
        task_id="lecture_variables",
        python_callable=afficher_variables,
    )
