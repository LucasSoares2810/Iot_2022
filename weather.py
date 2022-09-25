import requests

API_KEY = "0f6b714a491d7e16242f83ffed587054"
cidade = 'curitiba'
link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}'


def temperatura_atual():
    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    temperatura = requisicao_dic['main']['temp'] - 273.15

    return temperatura


def umidade_atual():
    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    umidade = requisicao_dic['main']['humidity']

    return umidade

