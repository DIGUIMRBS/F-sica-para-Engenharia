def aceleracao_plano_inclinado(aplicada, atrito, normal, massa, angulo):
    g = 10
    forca_peso = massa * g
    angulo_rad = angulo * (3.14159 / 180)
    forca_paralela = forca_peso * (angulo_rad)
    forca_resultante = aplicada - atrito - forca_paralela
    aceleracao = forca_resultante / massa
    return aceleracao

aplicada = float(input("Digite a força aplicada em N: "))
atrito = float(input("Digite a força de atrito em N: "))
normal = float(input("Digite a força normal em N: "))
massa = float(input("Digite a massa do objeto em kg: "))
angulo = float(input("Digite o ângulo de inclinação do plano em graus: "))
aceleracao = aceleracao_plano_inclinado(aplicada, atrito, normal, massa, angulo)

print("A aceleração do objeto é de aproximadamente", aceleracao," m/s².")
