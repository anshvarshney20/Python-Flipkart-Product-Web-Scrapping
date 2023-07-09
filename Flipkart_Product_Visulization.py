import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

search_term = input("Enter Name")
fetch = requests.get(f'https://www.flipkart.com/search?q={search_term}')
html = fetch.content
soup = BeautifulSoup(html, 'lxml')
tags = soup.find('div', class_='_1YokD2 _3Mn1Gg')

star_ratings = []
names = []

for tag in tags:
    name = tags.find_all('div', class_='_4rR01T')
    stars = tags.find_all('div', class_='_3LWZlK')
    
    for i in range(len(name)):
        names.append(name[i].text)
        star_ratings.append(float(stars[i].text))
        print("Name:", name[i].text)
        print("Star Rating:", stars[i].text)

# Create the bar graph
plt.bar(names, star_ratings)
plt.xlabel('Product')
plt.ylabel('Star Rating')
plt.title('Star Ratings of Products')
plt.xticks(rotation=90)
plt.show()
