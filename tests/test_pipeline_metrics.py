import pytest
from src.metrics.pipeline_metrics import PipelineMetricsLogger
import tempfile
import os
import json

def test_pipeline_metrics_logger(tmp_path):
    log_path = tmp_path / "metrics.log"
    logger = PipelineMetricsLogger(log_path=str(log_path))
    metrics_dict = {
        "step": "train",
        "roc_auc": 0.88,
        "records": 100
    }
    logger.log(metrics_dict)
    assert os.path.exists(log_path)
    # Check that at least one line is valid JSON and contains our keys
    with open(log_path) as f:
        lines = f.readlines()
    assert any("roc_auc" in json.loads(line) for line in lines)