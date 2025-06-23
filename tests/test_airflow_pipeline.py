import pytest
from airflow.models import DagBag

def test_airflow_dag_loaded():
    dag_bag = DagBag(dag_folder="notebooks")  # Adjust path as needed
    dag = dag_bag.get_dag('bridge_failure_batch_pipeline')
    assert dag is not None
    assert len(dag.tasks) >= 3
    assert {"feature_engineering", "model_training", "batch_scoring"}.issubset(set([t.task_id for t in dag.tasks]))