import requests
import os

if __name__ == "__main__":
    api_url = os.environ.get("GIMBR_API_DOCS", "http://localhost:8080/openapi.json")
    output_path = "docs/openapi.json"
    r = requests.get(api_url)
    if r.status_code == 200:
        with open(output_path, "w") as f:
            f.write(r.text)
        print(f"Downloaded current OpenAPI spec to {output_path}")
    else:
        print(f"Failed to fetch {api_url}: {r.status_code} {r.text}")