import requests
from bs4 import BeautifulSoup

url = "https://one-name.org/modern-british-surnames/statistics/top-surnames/england-wales/top-500-names/"
req = requests.get(url)
data = BeautifulSoup(req.text, features="html.parser")
table = data.find("table")
results = []
for tr in table.find_all("tr"):
    row = []
    for td in tr.find_all("td"):
        row.append(td.text)
    results.append(row)
for row_results in results:
    print(f"{row_results[1]}")