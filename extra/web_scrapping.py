from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

URL = "https://www.industrybuying.com/agriculture-garden-landscaping-2384/all-products/"
p = '[\d]+[.,\d]+|[\d]*[.][\d]+|[\d]+'

r = requests.get(URL)
soup = BeautifulSoup(r.content,
                     'html5lib')  # If this line causes an error, run 'pip install html5lib' or install html5lib

data = [["ProductId", "ProductName", "Price"]]
table = soup.find('div', attrs={'class': 'AH_ProductListInner d-flex removeSpanDiv'})


def get_price(ss):
    s = str(ss)
    if re.search(p, s) is not None:
        for catch in re.finditer(p, s):
            return catch[0]


for row in table.findAll('div',
                         attrs={'class': 'AH_ProductView col-lg-3 col-md-3 col-sm-6 col-xs-6 productThumbnails'}):
    product_id = row.find('div', attrs={'class': 'yotpo bottomLine'}).get('data-product-id')
    product_name = row.find('a', attrs={'class': 'prFeatureName'}).text
    price = get_price(row.find('span', attrs={'class': 'rs'}))
    data.append([product_id, product_name, price])

f = pd.DataFrame(data)
f.to_csv("WebScrapingIB.csv", index=False, header=False)
