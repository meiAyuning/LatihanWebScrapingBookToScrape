from bs4 import BeautifulSoup
import requests
import pandas as panda


def cekStar(kata):
    if kata == 'One':
        return 1
    elif(kata == 'Two'):
        return 2
    elif(kata == 'Three'):
        return 3
    elif(kata == 'Four'):
        return 4
    else:
        return 5


req = requests.get('https://books.toscrape.com/catalogue/page-1.html')
html = BeautifulSoup(req.content, 'lxml')
section = html.find('section')
ol = section.find('ol', class_='row')
li = ol.findAll('li')
data = []
for items in li:
    article = items.find('article')
    star = items.find('p').attrs['class'][1]
    h3 = article.find('h3').find('a').text
    price = items.find('div', class_='product_price').find(
        'p', class_='price_color').text

    data.append({
        'books': h3,
        'star': cekStar(star),
        'price': price
    })
frame = panda.DataFrame(data)
frame.to_csv('books.csv', index=False, encoding='utf-8')