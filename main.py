from bs4 import BeautifulSoup
import requests
req = "https://www.baltmaximus.com/?utm_source=inside&utm_medium=banner&utm_campaign=top_logo"
request = requests.get(req)
soup = BeautifulSoup(request.text, "lxml")
catalogs = soup.find("div", class_="catalog_menu")
for i in catalogs:
    data = i.find_("a", class_=" ")
    print(data)