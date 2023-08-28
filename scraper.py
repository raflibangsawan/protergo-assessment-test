from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

driver = webdriver.Chrome()
url = 'https://e-katalog.lkpp.go.id/id/search/produk/alat-olahraga/72?commodityId=72&order=relevance&limit=12&offset='
driver.get(url)
time.sleep(5)
results = []
# until pagination 229 since the web provide to 229 paginations of datas
for page in range(229):
    driver.get(url + str(page + 1))

    time.sleep(0.7)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    titles = soup.find_all(class_='card-item-title')
    items = soup.find_all(class_='card-item-description')

    for i in range(len(items)):
        title = titles[i*2 + 1].find('a').get_text(strip=True)
        description = items[i].find_all('p')
        store = description[0].get_text(strip=True)
        price = description[-1].get_text(strip=True)
        scraped_item = [title, store, price]
        results.append(scraped_item)

csv_file = "result.csv"

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Store Name", "Price"])
    writer.writerows(results)

print(f"Data has been written to {csv_file}.")