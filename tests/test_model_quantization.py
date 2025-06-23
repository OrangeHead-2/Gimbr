import pytest
import numpy as np
from src.models.quantization import quantize_rf

class DummyTree:
    def __init__(self):
        self.value = np.array([[0.1, 0.9], [0.5, 0.5]], dtype=np.float32)
        self.threshold = np.array([1.5, 2.5], dtype=np.float32)

class DummyEstimator:
    def __init__(self):
        self.tree_ = DummyTree()

class DummyRF:
    def __init__(self):
        self.estimators_ = [DummyEstimator() for _ in range(2)]

def test_quantize_rf_changes_dtype():
    rf = DummyRF()
    quantized = quantize_rf(rf)
    for est in quantized.estimators_:
        assert est.tree_.value.dtype == np.float16
        assert est.tree_.threshold.dtype == np.float16