import paho.mqtt.client as mqtt
from hal import *
from configuracoes import user, password, server, port, client_id
import time


def mensagem(cliente, userdata, msg):
    vetor = msg.payload.decode().split(',')
    aquecedor('on' if vetor[1] == '1' else 'off')
    client.publish(f'v1/{user}/things/{client_id}/response', f'ok,{vetor[0]}')
    print(vetor)


client = mqtt.Client(client_id)
client.username_pw_set(user, password)
client.connect(server, port)

client.on_message = mensagem
client.subscribe('v1/' + user + '/things/' + client_id + '/cmd/2')
client.loop_start()

while True:
    client.publish('v1/' + user + '/things/' + client_id + '/data/0', temp)
    client.publish('v1/' + user + '/things/' + client_id + '/data/1', umid)
    # client.publish('v1/' + user + '/things/' + client_id + '/data/2', aquecedor())

    time.sleep(10)

# client.disconnect()