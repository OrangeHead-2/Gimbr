.PHONY: all test lint format dvc-pull dvc-add train export-onnx serve-api serve-dashboard clean

all: test lint

install:
	pip install -r requirements.txt

test:
	pytest tests/ --maxfail=1 --disable-warnings -v

lint:
	flake8 src/ tests/

format:
	black src/ tests/

dvc-pull:
	dvc pull

dvc-add:
	dvc add data/processed/features.csv

train:
	python src/models/train.py --config configs/model_config.yaml

export-onnx:
	python src/models/export_onnx.py --config configs/model_config.yaml

serve-api:
	uvicorn src.serve.ray_app:app --host 0.0.0.0 --port 8000

serve-dashboard:
	streamlit run src/dashboard/streamlit_dashboard.py

clean:
	find . -type f -name "*.pyc" -delete
	rm -rf __pycache__ .pytest_cache .mypy_cache .dvc/tmp