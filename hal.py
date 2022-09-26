import time

import weather


def temperatura():
    temperatura = weather.temperatura_atual()
    return temperatura


def umidade():
    umidade = weather.umidade_atual()
    return umidade


def aquecedor(estado: str):
    if estado == 'on':
        print("botão LIGADO")
    else:
        print("Botão Desligado")



