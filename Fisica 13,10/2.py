def velocidade_caminhao(distancia_entre_marcas):
  distancia_percorrida = distancia_entre_marcas
  tempo = 1 / 2 
  velocidade = distancia_percorrida / tempo
  return velocidade

distancia_entre_marcas = float(input("Digite a distância das marcas das gotas " ))

velocidade_do_caminhao = velocidade_caminhao(distancia_entre_marcas)
print("A velocidade do caminhão é ", velocidade_do_caminhao," metros por segundo.")