def velocidade_media_ultimo_trecho(distancia_total, distancia_primeiro, velocidade_primeiro, distancia_segundo, velocidade_segundo, tempo_total):
    tempo_primeiro = distancia_primeiro / velocidade_primeiro
    tempo_segundo = distancia_segundo / velocidade_segundo
    tempo_ultimo = tempo_total - tempo_primeiro - tempo_segundo
    distancia_ultimo = distancia_total - distancia_primeiro - distancia_segundo
    velocidade_media_ultimo = distancia_ultimo / tempo_ultimo
    return velocidade_media_ultimo

distancia_total = float(input("Digite a distância total da viagem " ))
distancia_primeiro = float(input("Digite a distância percorrida no primeiro trecho " ))
velocidade_primeiro = float(input("Digite a velocidade do veiculo do primeiro trecho " ))
distancia_segundo = float(input("Digite a distância do segundo trecho " ))
velocidade_segundo = float(input("Digite a velocidade do veiculo do segundo trecho " ))
tempo_total = float(input("Digite o tempo total da viagem " ))

velocidade_media = velocidade_media_ultimo_trecho(distancia_total, distancia_primeiro, velocidade_primeiro, distancia_segundo, velocidade_segundo, tempo_total)
print("A velocidade media do carro no ultimo trecho é ", velocidade_media," km/h.")