import RPi.GPIO as GPIO
from time import sleep
from entrada_saida import *

def lista_sala(sala):
    return [sala['Lampada_1'],
            sala['Lampada_2'],
            sala['Projetor'],
            sala['Ar_condicionado'],
            sala['Alarme']]

def acende_lampadas_sensor(sala):
    print('Acende lampadas por presença')
    GPIO.setup(sala['Lampada_1'], GPIO.OUT)
    GPIO.setup(sala['Lampada_2'], GPIO.OUT)
    GPIO.output(sala['Lampada_1'], GPIO.HIGH)
    GPIO.output(sala['Lampada_2'], GPIO.HIGH)
    infos_servidor_central['Lâmpada 1'] = 'ligado'
    infos_servidor_central['Lâmpada 2'] = 'ligado'
    sleep(15)
    GPIO.output(sala['Lampada_1'], GPIO.LOW)
    GPIO.output(sala['Lampada_2'], GPIO.LOW)
    infos_servidor_central['Lâmpada 1'] = 'desligado'
    infos_servidor_central['Lâmpada 2'] = 'desligado'

    GPIO.setup(sala['Lampada_1'], GPIO.IN)
    GPIO.setup(sala['Lampada_2'], GPIO.IN)

def controlar_incendio(sala):
    GPIO.setup(sala['Alarme'], GPIO.OUT)
    GPIO.output(sala['Alarme'], GPIO.HIGH)
    infos_servidor_central['Alarme'] = 'ligado'
    
    GPIO.setup(sala['Alarme'], GPIO.IN)

def liga_lampadas(sala):
    GPIO.setup(sala['Lampada_1'], GPIO.OUT)
    GPIO.setup(sala['Lampada_2'], GPIO.OUT)
    GPIO.output(sala['Lampada_1'], GPIO.HIGH)
    GPIO.output(sala['Lampada_2'], GPIO.HIGH)
    infos_servidor_central['Lâmpada 1'] = 'ligado'
    infos_servidor_central['Lâmpada 2'] = 'ligado'
    
    GPIO.setup(sala['Lampada_1'], GPIO.IN)
    GPIO.setup(sala['Lampada_2'], GPIO.IN)

def liga_ar_condicionado(sala):
    GPIO.setup(sala['Ar_condicionado'], GPIO.OUT)
    GPIO.output(sala['Ar_condicionado'], GPIO.HIGH)
    infos_servidor_central['Lâmpada 1'] = 'ligado'

    GPIO.setup(sala['Ar_condicionado'], GPIO.IN)

def liga_projetor(sala):
    GPIO.setup(sala['Projetor'], GPIO.OUT)
    GPIO.output(sala['Projetor'], GPIO.HIGH)
    infos_servidor_central['Projetor'] = 'ligado'

    GPIO.setup(sala['Projetor'], GPIO.IN)

def desliga_todas_cargas(sala):    
    
    GPIO.setup(sala['Lampada_1'], GPIO.OUT)
    GPIO.setup(sala['Lampada_2'], GPIO.OUT)
    GPIO.setup(sala['Alarme'], GPIO.OUT)
    GPIO.setup(sala['Ar_condicionado'], GPIO.OUT)
    GPIO.setup(sala['Projetor'], GPIO.OUT)
    GPIO.output(sala['Lampada_1'], GPIO.LOW)
    GPIO.output(sala['Lampada_2'], GPIO.LOW)
    GPIO.output(sala['Alarme'], GPIO.LOW)
    GPIO.output(sala['Ar_condicionado'], GPIO.LOW)
    GPIO.output(sala['Projetor'], GPIO.LOW)
    infos_servidor_central['Lâmpada 1'] = 'desligado'
    infos_servidor_central['Lâmpada 2'] = 'desligado'
    infos_servidor_central['Alarme'] = 'desligado'
    infos_servidor_central['Ar-Condicionado'] = 'desligado'
    infos_servidor_central['Projetor'] = 'desligado'

    
    GPIO.setup(sala['Lampada_1'], GPIO.IN)
    GPIO.setup(sala['Lampada_2'], GPIO.IN)
    GPIO.setup(sala['Alarme'], GPIO.IN)
    GPIO.setup(sala['Ar_condicionado'], GPIO.IN)
    GPIO.setup(sala['Projetor'], GPIO.IN)

def dispara_alarme(sala):

    GPIO.setup(sala['Alarme'], GPIO.OUT)
    GPIO.output(sala['Alarme'], GPIO.HIGH)    
    infos_servidor_central['Alarme'] = 'ligado'

    GPIO.setup(sala['Alarme'], GPIO.IN)

def desliga_alarme(sala):

    GPIO.setup(sala['Alarme'], GPIO.OUT)
    GPIO.output(sala['Alarme'], GPIO.LOW)
    infos_servidor_central['Alarme'] = 'desligado'

    GPIO.setup(sala['Alarme'], GPIO.IN)
