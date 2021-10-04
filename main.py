# import pandas
import random
import pandas as pd

data = pd.read_csv('./data/sincro.csv', sep = ';', encoding='latin-1')

# mocks
dias = [
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-feira',
    'Sexta-feira',
    'Sábado',
    'Domingo'
]

horas = [
    "00:00", "00:30", "01:00", "01:30", "02:00", "02:30",
    "03:00", "03:30", "04:00", "04:30", "05:00", "05:30",
    "06:00", "06:30", "07:00", "07:30", "08:00", "08:30",
    "09:00", "09:30", "10:00", "10:30", "11:00", "11:30",
    "12:00", "12:30", "13:00", "13:30", "14:00", "14:30",
    "15:00", "15:30", "16:00", "16:30", "17:00", "17:30",
    "18:00", "18:30", "19:00", "19:30", "20:00", "20:30",
    "21:00", "21:30", "22:00", "22:30", "23:00", "23:30"
]

hora = horas[random.randint(0, 47)]
dia  = dias[random.randint(0, 6)]

def stage(dia, hora):
    # define intervalo de velocidade para horario de pico
    intervalo = list(range(41))

    consulta = data.query('dia_semana == "{}" & hora_dia == "{}"'.format(dia, hora))

    # retorna velocidade baseado no dia e hora
    velocidade_media = consulta.v_media.item()

    print("\n Dia: {}, hora: {}, velocidade media: {}".format(dia, hora, velocidade_media))

    # define paramentros para calculo de temporização
    if velocidade_media in intervalo:
        calc_horaria_velocidade(0, converte_metros_segundo(max(intervalo)), 1)
    else:
        calc_horaria_velocidade(0, converte_metros_segundo(60), 1)

def converte_metros_segundo(velocidade):
    return velocidade/3.6

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
    resultado_s1 = round(tempo + delta_t, 2)

    print("\n Resultado tempo 1: {} segundos".format(resultado_s1))

def calc_movimento_uniforme_s2(velocidade_final):
    # distancia (em metros) da meta de abertura de s1 até a meta de abertura de s2
    distancia = 82

    # tempo restante até o veiculo atingir a segunda meta de abertura a partir da primeira meta
    tempo = round(distancia/velocidade_final, 2)

    print("\n Resultado tempo 2: {} segundos".format(tempo))

stage(dia, hora)
