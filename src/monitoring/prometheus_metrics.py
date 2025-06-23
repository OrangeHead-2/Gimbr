from prometheus_client import Counter, Histogram, start_http_server

REQUEST_COUNT = Counter('api_requests_total', 'Total API Requests', ['endpoint', 'method', 'status'])
REQUEST_LATENCY = Histogram('api_request_duration_seconds', 'API Request latency', ['endpoint'])

def start_prometheus(port=9100):
    start_http_server(port)