import requests
import re
from bs4 import BeautifulSoup

url = "https://free-proxy-list.net/"
html_doc = requests.get(url).text
soup = BeautifulSoup(html_doc, 'lxml')


def getProxyList():

	for items in soup.select("#proxylisttable tbody tr"):
		proxy_list = ':'.join([item.text for item in items.select("td")[:2]])
		print(proxy_list)


if __name__ == "__main__":
	getProxyList()
