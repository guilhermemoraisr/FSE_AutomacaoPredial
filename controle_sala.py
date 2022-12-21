from datetime import datetime

from comportamento_sala import *
from entrada_saida import *

        
def rotina_sala(sala):

    global sensor_fumaca
    global sensor_janela
    global sensor_porta
    global sensor_presenca
    global sensor_umidade
    global sensor_temperatura
    global sensor_entrada
    global sensor_saida
    global modo_alarme_ativo
    global modo_incendio_ativo
    global ocupacao_sala

    while True:

        if sensor_entrada:
            sensor_entrada = False
            infos_servidor_central['Ocupação'] += 1
        if sensor_saida:

            sensor_saida = False
            if infos_servidor_central['Ocupação'] > 0:
                infos_servidor_central['Ocupação'] -= 1

        if not modo_alarme_ativo and sensor_presenca:

            acende_lampadas_sensor(sala)
            
        if sensor_fumaca and modo_incendio_ativo:
            controlar_incendio(sala)
            
        if modo_alarme_ativo and (sensor_presenca or sensor_porta or sensor_janela):
            dispara_alarme(sala)
            
        if not modo_alarme_ativo and not modo_incendio_ativo:
            desliga_alarme(sala)

        if lampadas:
            liga_lampadas(sala)

        if ar_condicionado:
            liga_ar_condicionado(sala)

        if projetor:
            liga_projetor(sala)

        if desligar_cargas:
            desliga_todas_cargas(sala)
            

def verifica_modo_servidor(modo):

    global modo_alarme_ativo
    global modo_incendio_ativo
    global projetor
    global ar_condicionado
    global lampadas
    global desligar_cargas

    if modo == '11' or modo == '12' or modo == '13':
        print('Acender lâmpadas')
        lampadas = True
    elif modo == '21' or modo == '22':
        print('Ligar ar-condicionado')
        ar_condicionado = True        
    elif modo == '31' or modo == '32':
        print('Ligar projetor')
        projetor = True        
    elif modo == '4':
        print('Sistema de alarme ativo')
        modo_alarme_ativo = True        
    elif modo == '5':
        print('Sistema de alarme inativo')
        modo_alarme_ativo = False        
    elif modo == '6':
        print('Sistema de incendio ativo')
        modo_incendio_ativo = True        
    elif modo == '7':
        print('Sistema de incendio inativo')
        modo_incendio_ativo = False        
    elif modo == '81' or modo == '82' or modo == '83':
        print('Desligar cargas')
        desligar_cargas = True
    

def ativa_sensor_entrada(channel):
    global sensor_entrada
    sensor_entrada = True
    infos_servidor_central['Sensor de entrada'] += 1
    print(f"Sensor entrada: {channel}")

def ativa_sensor_saida(channel):
    global sensor_saida
    sensor_saida = True
    infos_servidor_central['Sensor de saída'] += 1
    print(f"Sensor saida: {channel}")


def ativa_sensor_presenca(channel):
    global sensor_presenca
    if GPIO.input(channel):
        sensor_presenca = True
        infos_servidor_central['Sensor de presença'] = 'ligado'
    if not GPIO.input(channel):
        sensor_presenca = False
        infos_servidor_central['Sensor de presença'] = 'desligado'    
    print(f"Sensor presenca: {channel}")


def ativa_sensor_fumaca(channel):
    global sensor_fumaca
    if GPIO.input(channel):
        sensor_fumaca = True
        infos_servidor_central['Sensor de fumaça'] = 'ligado'
    if not GPIO.input(channel):
        sensor_fumaca = False
        infos_servidor_central['Sensor de fumaça'] = 'desligado'    
    print(f"Sensor fumaça: {channel}")


def ativa_sensor_janela(channel):
    global sensor_janela
    if GPIO.input(channel):
        sensor_janela = True
        infos_servidor_central['Sensor de janela'] = 'ligado'
    if not GPIO.input(channel):
        sensor_janela = False
        infos_servidor_central['Sensor de janela'] = 'desligado'    
    print(f"Sensor janela: {channel}")


def ativa_sensor_porta(channel):
    global sensor_porta
    if GPIO.input(channel):
        sensor_porta = True
        infos_servidor_central['Sensor de porta'] = 'ligado'
    if not GPIO.input(channel):
        sensor_porta = False
        infos_servidor_central['Sensor de porta'] = 'desligado'    
    print(f"Sensor porta: {channel}")

def verifica_lampada_1(channel):
    global estado_lampada_1
    if GPIO.input(channel):
        estado_lampada_1 = True
        infos_servidor_central['Lâmpada 1'] = 'ligado'
    if not GPIO.input(channel):
        estado_lampada_1 = False
        infos_servidor_central['Lâmpada 1'] = 'desligado'    

def verifica_lampada_2(channel):
    global estado_lampada_2
    if GPIO.input(channel):
        estado_lampada_2 = True
        infos_servidor_central['Lâmpada 2'] = 'ligado'
    if not GPIO.input(channel):
        estado_lampada_2 = False
        infos_servidor_central['Lâmpada 2'] = 'desligado'    

def verifica_projetor(channel):
    global estado_projetor
    if GPIO.input(channel):
        estado_projetor = True
        infos_servidor_central['Projetor'] = 'ligado'
    if not GPIO.input(channel):
        estado_projetor = False
        infos_servidor_central['Projetor'] = 'desligado'    

def verifica_ar_condicionado(channel):
    global estado_ar_condicionado
    if GPIO.input(channel):
        estado_ar_condicionado = True
        infos_servidor_central['Ar-Condicionado'] = 'ligado'
    if not GPIO.input(channel):
        estado_ar_condicionado = False
        infos_servidor_central['Ar-Condicionado'] = 'desligado'    

def verifica_alarme(channel):
    global estado_alarme
    if GPIO.input(channel):
        estado_alarme = True
        infos_servidor_central['Alarme'] = 'ligado'
    if not GPIO.input(channel):
        estado_alarme = False
        infos_servidor_central['Alarme'] = 'desligado'    


def ativa_sensor_umidade(channel):
    global sensor_umidade
    sensor_umidade = True
    print(f"Sensor umidade: {channel}")


def enviando_informacoes(tempo):
    global infos_servidor_central
    global ocupacao_sala
    infos_servidor_central['Temporizador'] += tempo
    return infos_servidor_central
