'''
|---------------------------------------------------|
| Instalação de pacotes com PIP e SetupTools        |
| External Lybraries > Python 3.9 > sitepackages    |
| No terminal digite pip --help                     |
|---------------------------------------------------|
'''

# Instalando package (biblioteca) Requests
# Endereço https://docs.python-requests.org/en/master/
# Comando no terminal: pip install requests

import requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.json())
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    return(dados_cep)

def retorna_dados_pokemon(pokemon):
    response  = requests.get('http://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    #retorna_dados_cep('22041001')
    #dados_pokemon = retorna_dados_pokemon('pikachu')
    #print(dados_pokemon['sprites']['front_shiny'])
    response = retorna_response('https://www.globallabs.academy/')
    print(response)