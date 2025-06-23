FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV MODEL_PATH=models/trained/model.joblib
ENV SECRET=YOUR_SECRET
ENV SENTRY_DSN=YOUR_SENTRY_DSN

CMD ["uvicorn", "dashboard.api:app", "--host", "0.0.0.0", "--port", "8080"]