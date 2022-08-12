import requests
from bs4 import BeautifulSoup
from operator import itemgetter

#py -m pip install beatfulsoup4
#py -m pip install requests

produtos = []
valores = []
geral = []

alvo = f'https://www.minhacooper.com.br/loja/garcia-bnu/produto/busca?q=feijao'

response = requests.get(alvo)

html = BeautifulSoup(response.text, 'html.parser')
#print(html)
for produto in html.select('.product-variation__name'):
    produtos.append(produto.text.strip())

for produto in html.select('.no-sprecial .price-wrapper .price , .special-price .price'):
    valores.append(float(produto.text.strip().replace('R$','').replace(',','.')))

for i in range(len(produtos)):
    dic = {'Produto': produtos[i], 'Valores': valores[i]}
    geral.append(dic)

for i in geral:
    print(i)