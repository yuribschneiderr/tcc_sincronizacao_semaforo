# import pandas
import pandas as pd
import numpy as np

#csv = pd.read_csv('sincro.csv', sep = ';', encoding='latin-1')

#print(csv.head(50))

def func_horaria_velocidade(v_0, v_f, aceleracao):
    tempo = (v_f - v_0)/aceleracao

    func_horaria_posicao(v_0, v_f, aceleracao, tempo)

def func_horaria_posicao(v_0, v_f, aceleracao, tempo):
    delta_s_0 = v_0 * tempo + (aceleracao * tempo**2/2)

    movimento_uniforme(delta_s_0, v_f, tempo)
    movimento_uniforme_2(v_f)

def movimento_uniforme(delta_s_0, v_f, tempo):
    distancia = 140 # em metros

    delta_s_1 = distancia - delta_s_0
    delta_t = delta_s_1/v_f
    result = tempo + delta_t

    print("Resultado tempo 1: {0:f}".format(result))

def movimento_uniforme_2(v_f):
    distancia = 82 # em metros

    tempo = distancia/v_f

    print("Resultado tempo 2: {0:f}".format(tempo))

velocidade = 60/3.6

func_horaria_velocidade(0, velocidade, 1)
