# eBayTracker
A Python program that takes an eBay link and returns the average price for the products in that link and stores the average price in a CSV file.

# Requirements
For this program to work properly, you must install the following libraries.
## Beautiful Soup
- BeautifulSoup4 is a HTML parser
```bash
pip install beautifulsoup4
```
## Requests
- Requests is a HTTP library, which is responsible for getting the link that is entered
```bash
pip install requests
```
## Numpy
- Numpy is a mathematical library, responsible for removing outliers and for calculating the average price for the product searched
```bash
pip install numpy
```
## datetime
- This is a library that allows for getting the current data and time for storing the product price in a csv file
```
pip install datetime
```
# Usage
When you start the program, you will be greeted with this in the terminal:
```
Welcome to the eBay Price Tracker!
Enter an eBay link to find the average price for the product! 
Input here: 
```
You can then paste the link from your browser's search bar and press enter to let the program parse the link!
For example, I will look for the average price for an Nvidia RTX 3080 Graphics Card, as shown below!
```
Welcome to the eBay Price Tracker!
Enter an eBay link to find the average price for the product! 
Input here: https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p4432023.m570.l1311&_nkw=nvidia+rtx+3080&_sacat=0
Product name: nvidia rtx 3080
Average Price: 448.46
```
This is the record that is saved in the csv file:
```
Date: 25-07-23,Product name: nvidia rtx 3080,Average price: 448.46
```
