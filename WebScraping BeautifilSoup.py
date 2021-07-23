import requests
from bs4 import BeautifulSoup
import json
import datetime
import investpy

listaAcoes = ['https://www.google.com/finance/quote/AZUL4:BVMF', 'https://www.google.com/finance/quote/CVCB3:BVMF', 'https://www.google.com/finance/quote/HCTR11:BVMF',
              'https://www.google.com/finance/quote/URPR11:BVMF']

nomeAcao = ['Azul', 'CVC', 'HCTR11', 'URPR11']


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Coletar e analisar a primeira página
"""
Implimentação #
pageAzul = requests.get()
soupAzul = BeautifulSoup(pageAzul.text, 'html.parser')

# Pegar todo o texto da div BodyText
cotacaoAtual = soupAzul.find(class_='kf1m0')

# Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
artist_name_list_items = cotacaoAtual.find_all('div')

nomeString = str(artist_name_list_items[0])

print(nomeString[27:34])

"""
i = 0
"""
for acao in listaAcoes:
    page = requests.get(acao)

    #Verifica cotação atual
    soup = BeautifulSoup(page.text, 'html.parser')
    cotacaoAtual = soup.find(class_='kf1m0')
    cotacaoAtualFind = cotacaoAtual.find_all()

    #Verifica Variação atual





    nomeString = str(cotacaoAtualFind)
    print(f'{nomeAcao[i]} {nomeString[28:36]}')
    i+=1

acao = 0
"""
"""
for acao in listaAcoes:
    print(acao)
    page = requests.get(acao)
    soup = BeautifulSoup(page.text, 'html.parser')
    variacao = soup.find(class_='zWwE1')
    variacaoFind = variacao.find_all()
    print(variacao)
"""

"""
page = requests.get('https://finance.yahoo.com/quote/AZUL4.SA?p=AZUL4.SA&.tsrc=fin-srch')
soup = BeautifulSoup(page.text, 'html.parser')
variacao = soup.select('span.Trsdu\(0\.3s\):nth-child(2)')
# variacaoFind = variacao.find_all(id='32')
print(variacao)


page = requests.get('https://www.google.com/finance/quote/HCTR11:BVMF')
soup = BeautifulSoup(page.text, 'html.parser')
variacao = soup.find(class_='zWwE1')
variacaoFind2 = soup.find_all('div', class_='zWwE1')
variacaoFind2String = str(variacaoFind2)
# JwB6zf zWwE1
variacaoFind3 = soup.select('.AHmHk')
print(variacaoFind3)
print(variacaoFind2)
print(variacaoFind2String[3865:3870])
"""
"""
page = requests.get('https://finance.yahoo.com/quote/AAPL/financials?p=AAPL%27')
soup = BeautifulSoup(page.text, 'html.parser')

variacao = soup.findAll('div')
close_price = [entry.text for entry in soup.find_all('span', {'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})]

print(close_price)
"""
"""
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=HCTR&apikey=3R9BRA1CF7XYQDLY'
r = requests.get(url)
data = r.json()

print(data)
"""



"""
search_result = investpy.search_quotes(text='HCTR11', products=['stocks'],
                                       countries=['brazil'], n_results=1)

prevClose = search_result.retrieve_information().get('prevClose')
print(prevClose)
# print(search_result.retrieve_information())

recent_data = search_result.retrieve_recent_data()
# print(recent_data.head(-1))


df = investpy.get_stock_recent_data('HCTR11', 'brazil', as_json=False, order='descending', interval='Daily')

abertura = list(df['Open'])
fechamento = list(df['Close'])

print(f'Abertura: {round(abertura[0], 2)}')
print(f'Fechamento: {round(fechamento[0], 2)}')

variacaoPorcentagem = round((float(prevClose) - float(fechamento[0])), 2)


if fechamento[0] < prevClose:
    print(f'-{variacaoPorcentagem}')
else:
    print(f'+{variacaoPorcentagem}')
"""

# df = investpy.get_stock_recent_data('AZUL4', 'brazil', as_json=False, order='descending', interval='Daily')

fundos = ['HCTR11', 'URPR11', 'AZUL4', 'CVCB3', 'RECT11', 'TECN3', 'EQPA3', 'TAEE11']


def textoFormatado(nomeFundo, fechamentoAnterior,
                   fechamento, variacaoReal,
                   variacaoPorcentagem):
    """Função para formatação da string"""

    if(variacaoPorcentagem>0):
        print(f'{nomeFundo}: PrevClose: {fechamentoAnterior} / '
                f'Candle: {fechamento} / Variação Real: {bcolors.OKGREEN}R${variacaoReal}{bcolors.ENDC} / '
                 f'{bcolors.OKGREEN}{variacaoPorcentagem}%{bcolors.ENDC}')

    else:
        print(f'{nomeFundo}: PrevClose: {fechamentoAnterior} / '
                f'Candle: {fechamento} / Variação Real: {bcolors.FAIL}-R${variacaoReal}{bcolors.ENDC} / '
                 f'{bcolors.FAIL}{variacaoPorcentagem}%{bcolors.ENDC}')


while True:
    for fundo in fundos:
        try:
            search_result: object = investpy.search_quotes(text=fundo, products=['stocks'],
                                                       countries=['brazil'], n_results=1)
            prevClose = search_result.retrieve_information().get('prevClose')
        # print(f'PrevClose {fundo}: {prevClose}')
        except:
            print('Falha Conexão')
        try:
            df = investpy.get_stock_recent_data(fundo, 'brazil', as_json=False, order='descending', interval='Daily')
            abertura = list(df['Open'])
            fechamento = list(df['Close'])
            # print(f'Fechamento: {round(fechamento[0], 2)}')

            Porcentagem = round(100-((float(prevClose)*100)/float(fechamento[0])), 2)
            # stocksList = investpy.get_stocks_list(country='Brazil')
            # print(stocksList)

            if float(prevClose) > float(fechamento[0]):
                variacaoPorcentagem = round((float(prevClose) - float(fechamento[0])), 2)
                textoFormatado(fundo, prevClose, fechamento[0], variacaoPorcentagem, Porcentagem)
            else:
                variacaoPorcentagem = round((float(fechamento[0]) - float(prevClose)), 2)
                textoFormatado(fundo, prevClose, fechamento[0], variacaoPorcentagem, Porcentagem)


# print(f'{fundo}: PrevClose: {prevClose} / Candle: {bcolors.BOLD}{fechamento[0]}{bcolors.ENDC} / Variação R$: -{bcolors.FAIL}{variacaoPorcentagem}{bcolors.ENDC}, Variação: {Porcentagem}% ')


# print(f'{fundo}: PrevClose: {prevClose} / Candle: {bcolors.OKGREEN}{fechamento[0]}{bcolors.ENDC} / Variação: +{bcolors.OKGREEN}{-1 * variacaoPorcentagem}{bcolors.ENDC}, Variação: {Porcentagem}%')

        except Exception as name:
            print(f'{fundo} não tem stock disponivel')
            print(name)


        print('')
    print('############### Fim Cabeçalho ##################')
    print('')



