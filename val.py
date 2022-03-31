from cgitb import html
from bs4 import BeautifulSoup
import requests

# input player name
x = input()


try:
    source = requests.get('https://www.vlr.gg/stats')
    source.raise_for_status()
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.find("table", {"class": "wf-table mod-stats"}))
except Exception as e:
    print(e)
