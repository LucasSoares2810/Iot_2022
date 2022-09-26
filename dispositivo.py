import paho.mqtt.client as mqtt
import time
from hal import *
from configuracoes import user, password, server, port, client_id

habilita = False


def mensagem(client, userdata, msg):
    vetor = msg.payload.decode().split(',')
    client.publish(f'v1/{user}/things/{client_id}/response', f'ok,{vetor[0]}')
    aquecedor('on' if vetor[1] == '1' else 'off')
    global habilita
    if vetor[1] == '1':
        habilita = True
    elif vetor[1] == '0':
        habilita = False
    print(vetor)


client = mqtt.Client(client_id)
client.username_pw_set(user, password)
client.connect(server, port)

client.on_message = mensagem
client.subscribe(f'v1/{user}/things/{client_id}/cmd/2')
client.loop_start()

x = round(temperatura())
d = habilita

while True:
    if habilita:
        temp = x
        if temp <= 35:
            while temp <= 35 and habilita == True:
                temp += 1
                client.publish('v1/' + user + '/things/' + client_id + '/data/0', temp)
                time.sleep(2)
            x = temp

        elif temp >= 35:
            while temp >= 30:
                temp -= 1
                client.publish('v1/' + user + '/things/' + client_id + '/data/0', temp)
                time.sleep(2)
            x = temp
    elif habilita == False:
        if x != temperatura():
            while x != temperatura() and habilita == False:
                x -= 1
                client.publish('v1/' + user + '/things/' + client_id + '/data/0', x)
                time.sleep(2)
        else:
            client.publish('v1/' + user + '/things/' + client_id + '/data/0', x)
    client.publish('v1/' + user + '/things/' + client_id + '/data/1', umidade())
    time.sleep(5)
