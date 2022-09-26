import weather


def temperatura():
    temperatura = weather.temperatura_atual()
    return temperatura


def umidade():
    umidade = weather.umidade_atual()
    return umidade


def aquecedor(estado=str):
    if estado == 'on':
        print("Aquecedor LIGADO")

    elif estado == 'off':
        print("Aquecedor DESLIGADO")

def control(estado=str):
    if estado == '1':
        return 'on'
    elif estado == '0':
        return 'off'

