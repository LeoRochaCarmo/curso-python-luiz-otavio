"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 61
local_carro = 99

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1
vel_carro_radar = velocidade > RADAR_1
carro_passsou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
        local_carro <= (LOCAL_1 + RADAR_RANGE)


if vel_carro_radar:
    print('Passou da velocidade')
    if vel_carro_radar and carro_passsou_radar_1:
        print('Carro multado em radar 1')
        
