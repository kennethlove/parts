import requests
from bs4 import BeautifulSoup
from sys import argv

script, url = import argv

r = requests.get(url)
soup = BeautifulSoup(r.content)
g_data = str(soup.find('article')).split['<h']
