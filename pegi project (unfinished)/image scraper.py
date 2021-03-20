import requests
from bs4 import BeautifulSoup
import time
import urllib.request
import re
import numpy as np



main = requests.get("https://www.go2games.com/catalogsearch/result/index/?category_type=4507&q=VIDEO+GAMES")
soup = BeautifulSoup(main.content, 'html')

toolbar =soup.find_all('span', class_="toolbar-number" )

game_nb = re.findall('class="toolbar-number">(.*?)</span>,',str(toolbar))
game_pg = re.findall('class="toolbar-number toolbar-page">(.*?)</span>,',str(toolbar))

game_per_page = int(game_pg[1])
game_number = int(game_nb[0])


if game_number % game_per_page == 0 :
    windows = game_number/game_per_page
else :
    windows = (game_number//game_per_page) +1

windowss = np.arange(1, windows+1, 1)

img_file =[]

for window in windowss :
    page = requests.get("https://www.go2games.com/catalogsearch/result/index/?category_type=4507&p="+str(window)+"&q=VIDEO+GAMES")
    soup = BeautifulSoup(page.content, "html.parser")
    
    for img in soup.find_all('img', {'class':'product-image-photo'}) :
        img_file.append(img['data-src'])
    

filename = 1

for url in img_file:
    try:
        urllib.request.urlretrieve(url, f'{filename}.jpg')
        filename += 1
    except Exception as exc:
        print(f"Exception occued while downloading image from url {url} {str(exc)}")