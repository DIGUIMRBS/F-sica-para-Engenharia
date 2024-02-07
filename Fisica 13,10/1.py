def comprimento_trem(velocidade_trem, comprimento_ponte, tempo_de_travessia):
  velocidade_trem = velocidade_trem * 5/18
  comprimento_trem = velocidade_trem * tempo_de_travessia - comprimento_ponte
  return comprimento_trem


velocidade_trem = float(input("Digite a velocidade atual do trem " ))
comprimento_ponte = float(input("Digite a distância total da ponte " ))
tempo_de_travessia = float(input("Digite o tempo da travessia " ))

comprimento_do_trem = comprimento_trem(velocidade_trem, comprimento_ponte, tempo_de_travessia)
print("O comprimento do trem é", comprimento_do_trem, "metros.")