sala_1 = {
    'Lampada_1': 18,
    'Lampada_2': 23,
    'Projetor': 25,
    'Ar_condicionado': 24,
    'Alarme': 8,
    'Sensor_presenca': 7,
    'Sensor_fumaca': 1,
    'Sensor_janela': 12,
    'Sensor_porta': 16,
    'Sensor_entrada': 20,
    'Sensor_saida': 21,
    'Sensor_temperatura': 4
}

sala_2 = {
    'Lampada_1': 26,
    'Lampada_2': 19,
    'Projetor': 6,
    'Ar_condicionado': 13,
    'Alarme': 5,
    'Sensor_presenca': 0,
    'Sensor_fumaca': 11,
    'Sensor_janela': 9,
    'Sensor_porta': 10,
    'Sensor_entrada': 22,
    'Sensor_saida': 27,
    'Sensor_temperatura': 18
}

infos_servidor_central = {
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
}

sensor_fumaca = False
sensor_janela = False
sensor_porta = False
sensor_presenca = False
sensor_umidade = False
sensor_temperatura = False
modo_alarme_ativo = False
modo_incendio_ativo = False
sensor_entrada = False
sensor_saida = False
ocupacao_sala = 0
projetor = False
ar_condicionado = False
lampadas = False
desligar_cargas = False
estado_lampada_1 = False
estado_lampada_2 = False
estado_projetor = False
estado_ar_condicionado = False
estado_alarme = False
