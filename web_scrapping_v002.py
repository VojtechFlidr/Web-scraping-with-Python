from bs4 import BeautifulSoup
import requests
from csv import writer

url= "https://www.sreality.cz/hledani/prodej/komercni/cinzovni-domy/praha,plzensky-kraj,olomoucky-kraj,jihomoravsky-kraj,kralovehradecky-kraj"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_="ng-binding")

with open('housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Location', 'Price', 'Area']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('span', class_="name ng-binding").text.replace('\n', '')
        location = list.find('span', class_="locality ng-binding").text.replace('\n', '')
        price = list.find('span', class_="norm-price ng-binding").text.replace('\n', '')
        area = list.find('span', class_="locality ng-binding").text.replace('\n', '')
        info = [title, location, price, area]
        thewriter.writerow(info)
