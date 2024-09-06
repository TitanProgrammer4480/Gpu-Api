from bs4 import BeautifulSoup
import requests

def sort(list):
	return list["price"]

def get_price(search_term):
	url = f"https://www.newegg.ca/p/pl?d={search_term}&Order=1"
	page = requests.get(url).text
	doc = BeautifulSoup(page, "html.parser")

	page_text = doc.find(class_="list-tool-pagination-text").strong
	pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])

	items_found = []

	for page in range(1, pages + 1):
		url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131&page={page}"
		page = requests.get(url).text
		doc = BeautifulSoup(page, "html.parser")

		div = doc.find(class_="item-cells-wrap border-cells short-video-box items-list-view is-list")
		items = div.find_all("div", "item-cell")

		for item in items:
			outer_div = item.div
			link = outer_div.find("a", "item-img")
			price = outer_div.find("li", "price-current")
			items_found.append({"price": price.text, "link": link.get("href")})

	items_found.sort(key=sort)
	return items_found