import RPi.GPIO as GPIO
import sys
from threading import Thread
import socket
import json
import time
import sys
import Adafruit_DHT

from entrada_saida import sala_1, sala_2, infos_servidor_central
from comportamento_sala import lista_sala
from controle_sala import *

sala = {}


if sys.argv[1] == 'sala_1' or sys.argv[1] == 'sala_3':
    sala = sala_1.copy()
elif sys.argv[1] == 'sala_2' or sys.argv[1] == 'sala_4':
    sala = sala_2.copy()


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(lista_sala(sala), GPIO.OUT)

sensor_temp = Adafruit_DHT.DHT22

GPIO.setup(sala['Sensor_presenca'], GPIO.IN)
GPIO.setup(sala['Sensor_fumaca'], GPIO.IN)
GPIO.setup(sala['Sensor_janela'], GPIO.IN)
GPIO.setup(sala['Sensor_porta'], GPIO.IN)
GPIO.setup(sala['Sensor_entrada'], GPIO.IN)
GPIO.setup(sala['Sensor_saida'], GPIO.IN)
GPIO.setup(sala['Lampada_1'], GPIO.IN)
GPIO.setup(sala['Lampada_2'], GPIO.IN)
GPIO.setup(sala['Projetor'], GPIO.IN)
GPIO.setup(sala['Ar_condicionado'], GPIO.IN)
GPIO.setup(sala['Alarme'], GPIO.IN)
GPIO.setup(sala['Sensor_temperatura'], GPIO.IN)

HOST = sys.argv[-1]
PORT = 10481

try:
    client_socket = socket.socket()
    client_socket.connect((HOST, PORT))
    client_socket.sendall(str.encode(sys.argv[1]))

    def enviar_dados():
                
        while True:
            tempo_inicial = time.perf_counter()
            sleep(1)
            tempo_final = time.perf_counter()
            infos_servidor_central_enviado = enviando_informacoes(tempo_final - tempo_inicial)
            infos_servidor_central_enviado['Sala'] = int(sys.argv[1][-1])
            infos_servidor_central_enviado = json.dumps(infos_servidor_central_enviado).encode('utf-8')
            client_socket.sendall(infos_servidor_central_enviado)


    def receber_dados():
        
        while True:
            msg = client_socket.recv(1024)
            msg = msg.decode('utf-8')
            print(msg)
            verifica_modo_servidor(msg)

    def rotina_temperatura_umidade():

        while True:

            umid, temp = Adafruit_DHT.read_retry(sensor_temp, sala['Sensor_temperatura']);
            infos_servidor_central['Temperatura'] = temp
            infos_servidor_central['Umidade'] = umid

    GPIO.add_event_detect(sala['Sensor_presenca'], GPIO.BOTH, callback=ativa_sensor_presenca)
    GPIO.add_event_detect(sala['Sensor_fumaca'], GPIO.BOTH, callback=ativa_sensor_fumaca)
    GPIO.add_event_detect(sala['Sensor_janela'], GPIO.BOTH, callback=ativa_sensor_janela)
    GPIO.add_event_detect(sala['Sensor_porta'], GPIO.BOTH, callback=ativa_sensor_porta)
    GPIO.add_event_detect(sala['Sensor_entrada'], GPIO.RISING, callback=ativa_sensor_entrada)
    GPIO.add_event_detect(sala['Sensor_saida'], GPIO.RISING, callback=ativa_sensor_saida)
    GPIO.add_event_detect(sala['Lampada_1'], GPIO.BOTH, callback=verifica_lampada_1)
    GPIO.add_event_detect(sala['Lampada_2'], GPIO.BOTH, callback=verifica_lampada_2)
    GPIO.add_event_detect(sala['Projetor'], GPIO.BOTH, callback=verifica_projetor)
    GPIO.add_event_detect(sala['Ar_condicionado'], GPIO.BOTH, callback=verifica_ar_condicionado)
    GPIO.add_event_detect(sala['Alarme'], GPIO.BOTH, callback=verifica_alarme)

  
    thread_sala = Thread(target=rotina_sala, args=(sala,))
    thread_sala.start()

    thread_envia_dados = Thread(target=enviar_dados) 
    thread_envia_dados.start()

    thread_recebe_dados = Thread(target=receber_dados) 
    thread_recebe_dados.start()

    thread_temperatura_umidade = Thread(target=rotina_temperatura_umidade)
    thread_temperatura_umidade.start()


except KeyboardInterrupt:
    print("Saindo...")
    client_socket.close()
    sys.exit()
