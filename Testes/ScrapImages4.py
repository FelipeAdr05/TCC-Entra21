import requests
from bs4 import BeautifulSoup
from operator import itemgetter

#py -m pip install beatfulsoup4
#py -m pip install requests

produtos = []
valores = []
imagens = []
geral = []
geral2 = []

alvo = f'https://www.samsclub.com.br/feijao?_q=Feijao&map=ft'

response = requests.get(alvo)

html = BeautifulSoup(response, 'html.parser')
#print(html)
for produto in html.select('.vtex-product-summary-2-x-image'):
    produtos.append(produto.text.strip())

print(produtos)

