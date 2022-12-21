# Trabalho 1 - 2022-2 - FSE

Repositório focado no trabalho 1 da matéria de Fundamentos de Sistemas Embarcados feito utilizando a Raspberry Pi.


## Autor

Guilherme de Morais Richter.
Matrícula 180101617.

## Objetivo

Este trabalho tem por objetivo a criação de um sistema distribuído de automação predial para monitoramento e acionamento de sensores e dispositivos de um prédio com múltiplas salas. O sistema deve ser desenvolvido para funcionar em um conjunto de placas Raspberry Pi com um servidor central responsável pelo controle e interface com o usuário e servidores distribuídos para leitura e acionamento dos dispositivos. Dentre os dispositivos envolvidos estão o monitoramento de temperatura e umidade, sensores de presença, sensores de fumaça, sensores de contagem de pessoas, sensores de abertura e fechamento de portas e janelas, acionamento de lâmpadas, aparelhos de ar-condicionado, alarme e aspersores de água em caso de incêndio. Para um entendimento completo do projeto, sua descrição e requisitos podem ser vistos [aqui](https://gitlab.com/fse_fga/trabalhos-2022_2/trabalho-1-2022-2)


## Descrição

Utilizando a linguagem Python (versão 3) foi criado um Servidor Distribuído e um Servidor Central.

## Principais bibliotecas utilizadas

- RPi.GPIO (Link da documentação [aqui](https://pypi.org/project/RPi.GPIO/), não vem por padrão no Python 3)
- socket
- threading

# **Requisitos**

Para executar o código necessita-se de um ambiente raspbian, por isso é necessário conectar-se as Raspberry Pi, cujas quais foram utilizadas para desenvolver este projeto.

Além do que precisa-se executar os códigos da **maneira** que é explicado na seção 'Uso' (abaixo).

## **Uso**

Para executar os comandos abaixo, primeiro precisa-se clonar este repositório e copiá-lo para as duas rasp's, posteriormente acessá-las via conexão 'ssh' e entrar na pasta do projeto transferido.

Trabalhando com duas rasp's, uma delas servirá como Servidor Central, logo, o IP dessa Rasp terá que ser passado como parâmetro de inicialização nos scripts

Nos outros scripts, é necessário passar o parâmetro de qual cruzamento está sendo ativado, e o IP que está sendo executado o Servidor Central
Possíveis parâmetros de sala:
```
sala_1
sala_2
```

- **1°**: Executar o Servidor Central
    - No primeiro terminal, na rasp, execute o comando passando o IP :

```
python3 servidor_central.py numero_IP_da_rasp
```
Exemplo

```
python3 servidor_central.py 164.41.98.29
```

- **2°**: Executar o primeiro Cruzamento como cliente do Servidor Distribuído
    - No segundo terminal, na rasp, execute o comando passado os parâmetros 'sala' e 'IP' de onde está rodando o Servidor Central:

```
python3 main.py sala_1 IP_rasp_servidor_central
```
Exemplo

```
python3 main.py sala_1 164.41.98.29
```

- **3°**: Executar o segundo Cruzamento como cliente do Servidor Distribuído
    - No terceiro terminal, na rasp, execute o comando passado os parâmetros 'sala' e 'IP' de onde está rodando o Servidor Central:

```
python3 main.py sala_2 IP_rasp_servidor_central
```
Exemplo

```
python3 main.py sala_2 164.41.98.29
```


No Servidor Central, quando ele é executado, uma lista de interações aparece no terminal, mostrando os comandos:

```
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
0 - Voltar a mostrar os dados das Salas
```

Feito todos os comandos acima na **ordem**, basta interagir no simulador que se encontra na página do trabalho no aprender, conforme os IPs e rasps utilizados.


### Observações

- Alguns requisitos não foram cumpridos, como acionar equipamentos específicos e gerar log em CSV.
