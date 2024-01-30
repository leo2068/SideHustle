import requests
from bs4 import BeautifulSoup
import time
import random
from httpx import Client
from collections import defaultdict


# 1. Create HTTP client with headers that look like a real web browser
client = Client(
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,lt;q=0.8,et;q=0.7,de;q=0.6",
    },
    follow_redirects=True,
    http2=True,  # use HTTP/2 
)


query_key = 'tesla'
google_url = 'https://www.google.com/search?hl=en&q={query_key}'
yahoo_url = 'https://search.yahoo.com/search/?&p={query_key}'
size_request =  5
source_key = 'google_search'

url = google_url + (f"&start={0}" if 1 > 1 else "")
print(f"scraping news")
results = defaultdict(list)
response = client.get(url)
assert response.status_code == 200, f"failed status_code={response.status_code}"

html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')
print(soup) #get the google prohibition terms of service