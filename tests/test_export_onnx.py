import pytest
import joblib
import pandas as pd
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
from src.models.export_onnx import export_to_onnx

def test_export_to_onnx(tmp_path):
    # Dummy model and data
    class DummyModel:
        def fit(self, X, y): pass
    model = DummyModel()
    X = pd.DataFrame([[0.1, 0.2], [0.2, 0.3]])
    onnx_path = tmp_path / "model.onnx"
    export_to_onnx(model, X, onnx_path)
    assert onnx_path.exists()