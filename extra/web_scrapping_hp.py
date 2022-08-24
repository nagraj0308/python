import pandas as pd
import requests
from bs4 import BeautifulSoup
from word2number import w2n


# First website
def web_scrap(url):
    site = requests.get(url)
    soup = BeautifulSoup(site.content, 'html.parser')
    table = soup.find('table')
    # print(table)
    headers = []
    for i in table.find_all('th'):
        title = i.text.strip()
        headers.append(title)
        # print(title)
    mydata = pd.DataFrame(columns=headers)

    for j in table.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [i.text.strip() for i in row_data]
        length = len(mydata)
        mydata.loc[length] = row

    return mydata


url = 'https://dot.ca.gov/programs/procurement-and-contracts/contracts-out-for-bid'
df1 = web_scrap(url)
df1.to_csv('file1.csv')


# second site(https://opentender.eu/all/search/tender) with huge data
def web_scrap_new(url):
    site = requests.get(url)
    soup = BeautifulSoup(site.content, 'html.parser')
    table = soup.find('table')
    # print(table)
    headers = []
    for i in table.find_all('th'):
        title = i.text.strip()
        headers.append(title)
        # print(title)
    mydata = pd.DataFrame(columns=headers)

    num = soup.select("pagination div")[1].text.split("Entries:")[1].strip().split(" ")

    pages = w2n.word_to_num(num[1])
    pages = int(pages * float(num[0]))
    pages = 100
    for p in range(0, pages):
        soup = BeautifulSoup(requests.get(url.format(p)).content)
        table = soup.find('table')

        for j in table.find_all('tr')[1:]:
            row_data = j.find_all('td')
            row = [i.text.strip() for i in row_data]
            length = len(mydata)
            # print(length)
            mydata.loc[length] = row
            print(row)
        print(p, "/", pages-1)

    return mydata


df2 = web_scrap_new('https://opentender.eu/all/search/tender')
df2.to_csv('file2.csv')
