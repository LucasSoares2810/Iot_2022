import weather


def temperatura():
    temperatura = weather.temperatura_atual()
    return temperatura


def umidade():
    umidade = weather.umidade_atual()
    return umidade


def aquecedor():
    aquecendo = temperatura()
    if temperatura() <= 30:
        aquecendo += 1




temp = temperatura()

umid = umidade()
