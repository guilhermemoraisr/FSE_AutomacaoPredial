import socket
from _thread import *
from threading import Thread
import json
from time import sleep
import sys
import os

HOST = sys.argv[-1]
PORT = 10481
server_socket = socket.socket()

server_socket.bind((HOST, PORT))
server_socket.listen(5)

lista_address = []

dict_dados = {
    'Sala 1':
        {
        'Sala': 1,
        'Sensor de entrada': 0,
        'Sensor de saída': 0,
        'Sensor de presença': 'desligado',
        'Sensor de fumaça': 'desligado',
        'Sensor de janela': 'desligado',
        'Sensor de porta': 'desligado',
        'Temperatura': 0,
        'Umidade': 0,
        'Ocupação': 0,
        'Lâmpada 1': 'desligado',
        'Lâmpada 2': 'desligado',
        'Projetor': 'desligado',
        'Ar-Condicionado': 'desligado',
        'Temporizador': 0.1
        },
    'Sala 2':
        {
        'Sala': 2,
        'Sensor de entrada': 0,
        'Sensor de saída': 0,
        'Sensor de presença': 'desligado',
        'Sensor de fumaça': 'desligado',
        'Sensor de janela': 'desligado',
        'Sensor de porta': 'desligado',
        'Temperatura': 0,
        'Umidade': 0,
        'Ocupação': 0,
        'Lâmpada 1': 'desligado',
        'Lâmpada 2': 'desligado',
        'Projetor': 'desligado',
        'Ar-Condicionado': 'desligado',
        'Temporizador': 0.1
        }
}

dict_salas = {
    'sala_1': False,
    'sala_2': False
}

tecla_pressionada = False

def recebe_dados_client(conn):

    global dict_dados
    conn.send(str.encode('Entrou no servidor central'))
    while True:
        b = b''
        if not conn.recv(1024):
            break
        b += conn.recv(1024)
        dados = json.loads(b.decode('utf-8'))
        if dados['Sala'] == 1:
            dict_dados['Sala 1'] = dados
        elif dados['Sala'] == 2:
            dict_dados['Sala 2'] = dados

    conn.close()

def envia_dados_client():

    while True:

        mostra_dados_client()

        print('''Opcoes:
        11 - Acionar Lâmpadas (Sala 1)
        12 - Acionar Lâmpadas (Sala 2)
        13 - Acionar Lâmpadas (Prédio inteiro)
        21 - Acionar Ar-Condicionado (Sala 1)
        22 - Acionar Ar-Condicionado (Sala 2)
        31 - Acionar Projetores (Sala 1)
        32 - Acionar Projetores (Sala 2)
        4 - Acionar Sistema de Alarme
        5 - Desligar Sistema de Alarme
        6 - Acionar Sistema de Incêndio
        7 - Desligar Sistema de Incêndio
        81 - Desligar Cargas (Sala 1)
        82 - Desligar Cargas (Sala 2)
        83 - Desligar Cargas (Prédio inteiro)
        0 - Voltar a mostrar os dados das Salas''')        
        msg = input('Digite a opcao: ')

        print(msg)

        if msg != 8:
            for addr in lista_address:
                addr.sendall(str.encode(msg))
    
        elif msg == '8':
            os.system('cls' if os.name == 'nt' else 'clear')
            mostra_dados_client()
        os.system('cls' if os.name == 'nt' else 'clear')


def verifica_tecla(s):

    global tecla_pressionada
    while True:
        if input() == '0':
            tecla_pressionada = True
            break

def mostra_dados_client():

    global dict_dados, tecla_pressionada
    d = start_new_thread(verifica_tecla, ('',))
    print(d)
    while not tecla_pressionada:
        for infos in dict_dados.values():

            print(f"Sala {infos['Sala']}:")
            print(f"\nEstado das entradas")
            print(f"Sensor de entrada: {infos['Sensor de entrada']}")
            print(f"Sensor de saída: {infos['Sensor de saída']}")
            print(f"Sensor de presença: {infos['Sensor de presença']}")
            print(f"Sensor de fumaça: {infos['Sensor de fumaça']}")
            print(f"Sensor de janela: {infos['Sensor de janela']}")
            print(f"Sensor de porta: {infos['Sensor de porta']}")
            print(f"Temperatura: {infos['Temperatura']}")
            print(f"Umidade: {infos['Temperatura']}")
            print(f"\nEstado das saídas")
            print(f"Lâmpada 1: {infos['Lâmpada 1']}")
            print(f"Lâmpada 2: {infos['Lâmpada 2']}")
            print(f"Projetor: {infos['Projetor']}")
            print(f"Ar-Condicionado: {infos['Ar-Condicionado']}")
            print(f"Ocupação da sala:{infos['Ocupação']}")
            print(f"Tempo:{infos['Temporizador']}")
            print(f"=========================================================")

        print('Digite 0 para ir ao menu de comandos e aguarde ser redirecionado.')
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    tecla_pressionada = False
        
try:
    print('Servidor central iniciado!')
    thread_envia_dados = Thread(target=envia_dados_client) 
    thread_envia_dados.start()
    while True:
        conn, addr = server_socket.accept()
        lista_address.append(conn)
        print('\nConexão realizada por:', addr[0] + ':' + str(addr[1]))
        dict_salas[conn.recv(1024).decode('utf-8')] = conn

        start_new_thread(recebe_dados_client, (conn,))
except KeyboardInterrupt:
    print('\nServidor encerrado')
    server_socket.close()
    exit()
