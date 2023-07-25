from bs4 import BeautifulSoup
import requests
import numpy as np
import csv
from datetime import datetime

print("Welcome to the eBay Price Tracker!")
print("Enter an eBay link to find the average price for the product! ")
LINK = input("Input here: ")

def get_prices_by_link(link):
    r = requests.get(link)
    page_parse = BeautifulSoup(r.text, 'html.parser')
    search_results = page_parse.find("ul", {"class": "srp-results"}).find_all("li", {"class": "s-item"})
    item_prices = []

    for result in search_results:
        price_as_text = result.find("span", {"class": "s-item__price"}).text
        if "to" in price_as_text:
            continue
        price = float(price_as_text[1:].replace(",", ""))
        item_prices.append(price)
    return item_prices

def getProductName(link):
    r = requests.get(link)
    page_parse = BeautifulSoup(r.text, 'html.parser')
    input_tag = page_parse.find("input", {"class": "gh-tb ui-autocomplete-input"})
    product_name = input_tag["value"]
    return product_name

def remove_outliers(prices, m=2):
    data = np.array(prices)
    return data[abs(data - np.mean(data)) < m * np.std(data)]


def get_avg(prices):
    return np.mean(prices)


def save_to_file(prices):
    fields = ["Date: "+datetime.today().strftime("%d-%m-%y"),
              "Product name: "+getProductName(LINK),
              "Average price: "+str(np.around(get_avg(prices), 2))]
    with open('prices.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)


if __name__ == "__main__":
    prices = get_prices_by_link(LINK)
    without_outliers = remove_outliers(prices)
    print("Product name: "+getProductName(LINK))
    print("Average Price: "+str(np.around(get_avg(without_outliers), 2)))
    save_to_file(without_outliers)
