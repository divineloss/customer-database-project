import requests
from bs4 import BeautifulSoup

url = "https://www.verywellfamily.com/top-1000-baby-boy-names-2757618"
req = requests.get(url)
data = BeautifulSoup(req.text, features="html.parser")
ol = data.find("ol")
file = open("firstnames.txt", "w")
for li in ol.find_all("li"):
    file.write(f"{ol.text}\n")
file.close()    