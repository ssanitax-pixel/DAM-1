import requests

url = "https://jocarsa.com/

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    html = response.text
    print(html)
except requests.exceptions.RequestException as e:
    print("Error fetching the page:", e)
