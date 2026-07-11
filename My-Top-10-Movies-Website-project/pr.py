import requests
import os

api_key = os.environ.get("TMDB_API_KEY")
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
response = requests.get(
    url="https://api.themoviedb.org/3/search/movie",
    params={"query": "batman", "api_key": api_key, "language": "en-US"},
    timeout=10,
    headers=headers
)
print(response.status_code)
print(response.text)
