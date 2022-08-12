import requests
from bs4 import BeautifulSoup
from operator import itemgetter

produtos = []
valores = []
geral = []



alvo = f'https://www.minhacooper.com.br/loja/garcia-bnu'

response = requests.get(alvo)

html = BeautifulSoup(response.text, 'html.parser')
print(html)

for item in html.find_all('img'):
    print(item['src'])
# for produto in html.select('.vtex-product-summary-2-x-brandName'):
#     produtos.append(produto.text.strip())

# for produto in html.select('.vtex-productShowCasePrice'):
#     valores.append(produto.text.strip().replace('R$','').replace(',','.'))

# for i in range(len(produtos)):
#     dic = {'Produto': produtos[i], 'Preco': valores[i]}
#     geral.append(dic)

# for i in geral:
#     print(i)