from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="exo1_taches_dependnates",
    start_date=datetime(2026, 11, 8),
    schedule=None,
    catchup=False,
) as dag:

# tache2 , avec echo 
    task2 = BashOperator(
        task_id="tache_2",
        bash_command='echo "tache 2"',
    )
# tache1, avec echo
    task1 = BashOperator(
        task_id="tache_1",
        bash_command='echo "tache 1"',
    )

    # task1(tache1) s'exécute uniquement si task2(tache2) est en succès
    task2 >> task1