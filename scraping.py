## Scraping a new single page
## 4 points
## WIKIPEDIA : List of United States cities by population

from bs4 import BeautifulSoup
import requests
import time

WIKI_URL = "https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population"


def city(num):
    city = []
    url_text = requests.get(WIKI_URL).text
    soup = BeautifulSoup(url_text, 'html.parser')
    list = soup.find('table', class_='wikitable sortable').find('tbody').find_all('tr')[1:]
    for i in range(num):
        td_list = list[i].find_all('td')
        th_list = list[i].find_all('th')
        
        rank=int(th_list[0].text.strip())
        
        city_list=str(td_list[0].find('a').text.strip())
        
        try:
            state=str(td_list[1].find('a').text.strip())
        except:
            state=td_list[1].text.strip()
            
        population = int(td_list[2].text.strip().replace(',', ''))
        # print(td_list[:])
        # print(td_list[-1].find("span",class_="latitude").text.split()[0][:2])
        latitude = float(td_list[-1].find("span",class_="latitude").text.split()[0][:2])
        longitude = float(td_list[-1].find("span",class_="longitude").text.split()[0][:2])
        area = float(td_list[5].text.strip().split('\xa0')[0].replace(',', ''))
        time.sleep(0.1)
        city_list = {"rank": rank, "name":city_list, "state":state, "population": population, "area":area, "latitude":latitude, "longitude": longitude}
        city.append(city_list)
    
    return city
