# Deployment Guide

## Docker

```bash
docker build -t gimbr-app .
docker run -p 8050:8050 gimbr-app
```

## API

- `POST /predict`  
  Input: JSON array of infrastructure records  
  Output: Failure probabilities

## CI/CD

- GitHub Actions runs tests, lint, and builds Docker image on push
- Add secrets for DockerHub/registry for production deployments

## Security

- Use API keys for `/predict` endpoint (see `dashboard/security.py`)
- All access logged to `logs/access.log`
- For production, deploy behind HTTPS reverse proxy (e.g., Nginx)

---

For further help, contact devops@gimbr.ai