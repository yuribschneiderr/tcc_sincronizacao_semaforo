# import pandas
import pandas as pd
import numpy as np
import time

data = pd.read_csv('./data/sincro.csv', sep = ';', encoding='latin-1')

# velocidade media sensor
velocidade = 'velocidade aleatoria'
dia = 'dia aleatorio'

def stage(velocidade, dia):
    # define intervalo de velocidade para horario de pico
    intervalo = list(range(41))

    # retorna hora e dia da semana baseado na velocidade
    consulta = data.query('v_media == "{}" & dia_semana == "{}"'.format(velocidade, dia))

    # print("\n Dia: {}, hora: {}".format(consulta.dia_semana.item(), consulta.hora_dia.item()))

    # define paramentros para calculo de temporização
    if velocidade in intervalo:
        calc_horaria_velocidade(0, (max(intervalo)/3.6), 1)
    else:
        calc_horaria_velocidade(0, (60/3.6), 1)

def calc_horaria_velocidade(velocidade_inicial, velocidade_final, aceleracao):
    # tempo até o veiculo atigir a velocidade maxima
    tempo = (velocidade_final - velocidade_inicial)/aceleracao

    # calculo da distancia até atingir a velocidade maxima.
    calc_horaria_posicao(velocidade_inicial, velocidade_final, aceleracao, tempo)

def calc_horaria_posicao(velocidade_inicial, velocidade_final, aceleracao, tempo):
    # distancia até o veiculo atingir a velocidade maxima
    delta_s0 = velocidade_inicial * tempo + (aceleracao * tempo**2/2)

    # calculo do tempo restante para a primeira meta de abertura
    calc_movimento_uniforme_s1(delta_s0, velocidade_final, tempo)

    # calculo do tempo restante para segunda meta de abertura
    calc_movimento_uniforme_s2(velocidade_final)

def calc_movimento_uniforme_s1(delta_s0, velocidade_final, tempo):
    # distancia (em metros) do semáforo 0 até a meta de abertura de s1
    distancia = 140

    # distancia restante ate o veiculo atingir a primeira meta de abertura.
    delta_s1 = distancia - delta_s0

    # tempo restante até o veiculo atingir a primeira meta de abertura.
    delta_t = delta_s1/velocidade_final


    # tempo total para abertura do primeiro semáforo.
    resultado_s1 = tempo + delta_t

    print("\n Resultado tempo 1: {0:f}".format(resultado_s1))

def calc_movimento_uniforme_s2(velocidade_final):
    # distancia (em metros) da meta de abertura de s1 até a meta de abertura de s2
    distancia = 82

    # tempo restante até o veiculo atingir a segunda meta de abertura a partir da primeira meta
    tempo = distancia/velocidade_final

    print("\n Resultado tempo 2: {0:f}".format(tempo))
