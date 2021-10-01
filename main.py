# import pandas
import pandas as pd
import numpy as np

data = pd.read_csv('./data/sincro.csv', sep = ';', encoding='latin-1')

print(data.query('dia_semana == 35'))

# mocks
# TODO
# Criar mocks para os dados abaixo

dia = 'dia aleatorio'
hora = 'hora aleatoria'

# TODO
#def get_stage
#    if hora >= 12
#        stage_1(dia, hora)
#
#    if hora < 12
#        stage_2(dia, hora)

#def stage_1(dia, hora)
#    velocidade = data.query('dia_semana == $dia and hora_dia == $hora')
#
#    velocidade = range(35..60)
#
#    calc_horaria_velocidade(0, velocidade, 1)

#def stage_2(dia, hora)
#    velocidade = data.query('dia_semana == dia and hora_dia == hora')
#
#    calc_horaria_velocidade(0, velocidade, 1)

def calc_horaria_velocidade(velocidade_inicial, velocidade_final, aceleracao):
    # tempo até o veiculo atigir a velocidade maxima
    tempo = (velocidade_final - velocidade_inicial)/aceleracao

    # calculo da distancia até atingir a velocidade maxima.
    calc_horaria_posicao(velocidade_inicial, velocidade_final, aceleracao, tempo)

def calc_horaria_posicao(velocidade_inicial, velocidade_final, aceleracao, tempo):
    # Distancia até o veiculo atingir a velocidade maxima
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

    print("Resultado tempo 1: {0:f}".format(resultado_s1))

def calc_movimento_uniforme_s2(velocidade_final):
    # distancia (em metros) da meta de abertura de s1 até a meta de abertura de s2
    distancia = 82

    # tempo restante até o veiculo atingir a segunda meta de abertura a partir da primeira meta
    tempo = distancia/velocidade_final

    print("Resultado tempo 2: {0:f}".format(tempo))

#calc_horaria_velocidade(0, velocidade, 1)
