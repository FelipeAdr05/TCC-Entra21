import requests 
from bs4 import BeautifulSoup 
    
def getdata(url): 
    r = requests.get(url) 
    return r.text 
    
htmldata = getdata("https://www.minhacooper.com.br/loja/garcia-bnu/produto/busca?q=feijao") 
soup = BeautifulSoup(htmldata, 'html.parser') 
for a in soup.find_all('a'):
    if a.img:
        print(a.img['src'])
    