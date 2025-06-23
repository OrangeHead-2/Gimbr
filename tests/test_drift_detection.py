import pytest
import pandas as pd
from src.drift.detection import compute_ks_drift

def test_compute_ks_drift_detects_drift():
    ref = pd.Series([1] * 100)
    prod = pd.Series([10] * 100)
    stat, p = compute_ks_drift(ref, prod)
    assert stat > 0
    assert p < 0.05

def test_compute_ks_drift_no_drift():
    ref = pd.Series([1, 2, 3, 4, 5] * 20)
    prod = pd.Series([1, 2, 3, 4, 5] * 20)
    stat, p = compute_ks_drift(ref, prod)
    assert p > 0.05