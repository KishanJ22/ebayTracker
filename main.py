from bs4 import BeautifulSoup
import requests
import numpy as np
import csv
from datetime import datetime

LINK = input("Enter an eBay link to find the average price for the product! ")

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


def remove_outliers(prices, m=2):
    data = np.array(prices)
    return data[abs(data - np.mean(data)) < m * np.std(data)]


def get_avg(prices):
    return np.mean(prices)


def save_to_file(prices):
    fields = [datetime.today().strftime("%B-%F-%Y"),np.around(get_avg(prices),2)]
    with open('prices.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)


if __name__ == "__main__":
    prices = get_prices_by_link(LINK)
    without_outliers = remove_outliers(prices)
    print(get_avg(without_outliers))
    save_to_file(prices)