import requests
import lxml
from bs4 import BeautifulSoup
def get_link_data(url):
      dicto = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73",
            "Accept-Language": "en",
            }
      r = requests.get(url, headers=dicto)
      soup = BeautifulSoup(r.text, "lxml")
      # print(soup.prettify())
      name1 = soup.select_one(selector="#productTitle")
      #print(name1)
      name2 = soup.select_one(selector="#productTitle").get_text()
      name3 = name2.strip()
      #print(name2)
      #print('--------------------')
      #print(name3)
      price1 = soup.select_one(selector="#priceblock_ourprice")
      #print(price1)
      #print('----------------')
      price2 = soup.select_one(selector="#priceblock_ourprice").get_text()
      #print(price2)
      #print('--------------------')
      price3 = price2[1:]
      #print(price3)
      #print('--------------------')
      price4 = float(price3)
      #print(price4)
      return(name3,price4)