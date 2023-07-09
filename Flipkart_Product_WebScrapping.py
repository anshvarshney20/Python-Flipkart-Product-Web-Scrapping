import requests
from bs4 import BeautifulSoup
import pandas as pd

search_term = input("Enter Name")
fetch = requests.get(f'https://www.flipkart.com/search?q={search_term}')
html = fetch.content
soup = BeautifulSoup(html, 'lxml')
tags = soup.find('div', class_='_1YokD2 _3Mn1Gg')

data = []
for tag in tags:
    name = tags.find_all('div', class_="_4rR01T")
    stars = tags.find_all('div', class_="_3LWZlK")
    rating = tags.find_all('span', class_="_2_R_DZ")
    specification = tags.find_all('ul', class_="_1xgFaf")
    original_price = tags.find_all('div', class_="_3I9_wc _27UcVY")
    current_price = tags.find_all('div', class_="_30jeq3 _1_WHN1")
    percent_off = tags.find_all('div', class_="_3Ay6Sb")

    # Check length of lists
    length = min(len(name), len(stars), len(rating), len(specification), len(original_price), len(current_price), len(percent_off))

    for i in range(length):
        data.append({
            'Name': name[i].text if i < len(name) else None,
            'Star Rating': stars[i].text if i < len(stars) else None,
            'Rating': rating[i].text if i < len(rating) else None,
            'Specifications': specification[i].text if i < len(specification) else None,
            'Original Price': original_price[i].text if i < len(original_price) else None,
            'Current Price': current_price[i].text if i < len(current_price) else None,
            'Percent Off': percent_off[i].text if i < len(percent_off) else None
        })

df = pd.DataFrame(data)
df.to_csv('scraped_datas.csv', index=False)
print("Data saved successfully to scraped_dataz.csv")
