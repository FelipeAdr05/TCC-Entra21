
from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep
  
htmldata = urlopen('https://www.minhacooper.com.br/loja/garcia-bnu/produto/busca?q=feijao')
soup = BeautifulSoup(htmldata, 'html.parser')
sleep(2)
images = soup.find_all('img')
  
for item in images:
    print(item['src'])