# import de bibliotecas
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
    '00:00', '00:30', '01:00', '01:30', '02:00', '02:30',
    '03:00', '03:30', '04:00', '04:30', '05:00', '05:30',
    '06:00', '06:30', '07:00', '07:30', '08:00', '08:30',
    '09:00', '09:30', '10:00', '10:30', '11:00', '11:30',
    '12:00', '12:30', '13:00', '13:30', '14:00', '14:30',
    '15:00', '15:30', '16:00', '16:30', '17:00', '17:30',
    '18:00', '18:30', '19:00', '19:30', '20:00', '20:30',
    '21:00', '21:30', '22:00', '22:30', '23:00', '23:30'
]

soma_total_a = 0
soma_total_b = 0
menor_tempo  = 0

hora = horas[random.randint(0, 47)]
dia  = dias[random.randint(0, 6)]

def stage(dia, hora):
    # define intervalo de velocidade para horários de pico
    intervalo = list(range(31))

    consulta = data.query('dia_semana == "{}" & hora_dia == "{}"'.format(dia, hora))

    # retorna velocidade baseada no dia e hora
    velocidade_media = consulta.v_media.item()

    print("\n - Dia: {}, Hora: {}, Velocidade média: {} km/h".format(dia, hora, velocidade_media))

    # define parâmentros para cálculo de temporização
    if velocidade_media in intervalo:
        calc_horaria_velocidade(0, converte_metros_segundo(max(intervalo)), 1)
    else:
        calc_horaria_velocidade(0, converte_metros_segundo(60), 1)

def converte_metros_segundo(velocidade):
    return velocidade/3.6

def calc_horaria_velocidade(velocidade_inicial, velocidade_final, aceleracao):
    # tempo até o veículo atigir a velocidade máxima
    tempo = (velocidade_final - velocidade_inicial)/aceleracao

    # cálculo da distancia até atingir a velocidade máxima.
    calc_horaria_posicao(velocidade_inicial, velocidade_final, aceleracao, tempo)

def calc_horaria_posicao(velocidade_inicial, velocidade_final, aceleracao, tempo):
    # distância até o veículo atingir a velocidade máxima
    delta_s0 = velocidade_inicial * tempo + (aceleracao * tempo**2/2)

    print("\n ########### RESULTADO SEMÁFORO A ################")

    # cálculo do tempo restante para a primeira meta de abertura
    calc_movimento_uniforme_s1(delta_s0, velocidade_final, tempo)

    # cálculo do tempo restante para segunda meta de abertura
    calc_movimento_uniforme_s2(velocidade_final)

    # cálculo do tempo restante para a terceira meta de abertura
    calc_movimento_uniforme_s3(velocidade_final)

    #---------------------------------------------------------
    print("\n ########### RESULTADO SEMÁFORO B ################")

    # cálculo do tempo restante para a primeira meta de abertura
    calc_movimento_uniforme_t1(delta_s0, velocidade_final, tempo)

    # cálculo do tempo restante para segunda meta de abertura
    calc_movimento_uniforme_t2(velocidade_final)

    # cálculo do tempo restante para a terceira meta de abertura
    calc_movimento_uniforme_t3(velocidade_final)

    print("\n ###################################################")

    print("\n - Tempo total de abertura dos semáforos: {} segundos".format(menor_tempo))

    print("\n - Tempo total A: {} segundos".format(soma_total_a))

    print("\n - Tempo total B: {} segundos".format(soma_total_b))

def calc_movimento_uniforme_s1(delta_s0, velocidade_final, tempo):
    # distância (em metros) de A4 até a meta de abertura de A3
    distancia = 141.62

    # distância restante ate o veiculo atingir a primeira meta de abertura.
    delta_s1 = distancia - delta_s0

    # tempo restante até o veiculo atingir a primeira meta de abertura.
    delta_t = delta_s1/velocidade_final

    # tempo total para abertura do primeiro semáforo.
    resultado_s1 = round(tempo + delta_t, 2)

    global soma_total_a

    soma_total_a += resultado_s1

    print("\n - Resultado tempo 1 (A4 para A3): {} segundos".format(resultado_s1))

def calc_movimento_uniforme_s2(velocidade_final):
    # distância (em metros) da meta de abertura de A3 até a meta de abertura de A2
    distancia = 182.64

    # tempo restante até o veiculo atingir a segunda meta de abertura a partir da primeira meta
    tempo = round(distancia/velocidade_final, 2)

    global soma_total_a

    soma_total_a += tempo

    print("\n - Resultado tempo 2 (A3 para A2): {} segundos".format(tempo))

def calc_movimento_uniforme_s3(velocidade_final):
    # distância (em metros) da meta de abertura de A2 até a meta de abertura de A1
    distancia = 80.28

    # tempo restante até o veiculo atingir a terceira meta de abertura a partir da segunda meta
    tempo = round(distancia/velocidade_final, 2)

    global soma_total_a, menor_tempo

    menor_tempo += tempo * 3
    soma_total_a += tempo

    print("\n - Resultado tempo 3 (A2 para A1): {} segundos".format(tempo))

def calc_movimento_uniforme_t1(delta_s0, velocidade_final, tempo):
    # distância (em metros) de B1 até a meta de abertura de B2
    distancia = 70.40

    # distância restante ate o veiculo atingir a primeira meta de abertura.
    delta_s1 = distancia - delta_s0

    # tempo restante até o veiculo atingir a primeira meta de abertura.
    delta_t = delta_s1/velocidade_final

    # tempo total para abertura do primeiro semáforo.
    resultado_s1 = round(tempo + delta_t, 2)

    global soma_total_b

    soma_total_b += resultado_s1

    print("\n - Resultado tempo 1 (B1 para B2): {} segundos".format(resultado_s1))

def calc_movimento_uniforme_t2(velocidade_final):
    # distância (em metros) da meta de abertura de B2 até a meta de abertura de B3
    distancia = 182.64

    # tempo restante até o veiculo atingir a segunda meta de abertura a partir da primeira meta
    tempo = round(distancia/velocidade_final, 2)

    global soma_total_b

    soma_total_b += tempo

    print("\n - Resultado tempo 2 (B2 para B3): {} segundos".format(tempo))

def calc_movimento_uniforme_t3(velocidade_final):
    # distância (em metros) da meta de abertura de B3 até a meta de abertura de B4
    distancia = 141.62

    # tempo restante até o veiculo atingir a terceira meta de abertura a partir da segunda meta
    tempo = round(distancia/velocidade_final, 2)

    global soma_total_b

    soma_total_b += tempo

    print("\n - Resultado tempo 3 (B3 para B4): {} segundos".format(tempo))

stage(dia, hora)
