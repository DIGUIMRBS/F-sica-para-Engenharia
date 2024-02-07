def forca_normal(massa, gravidade):
    gravidade = 10
    return massa * gravidade

massa = float(input("Digite a massa do objeto em kg: "))
angulo = float(input("Digite o ângulo de inclinação do plano em graus: "))
forca = forca_normal(massa, angulo)

print("A força normal exercida sobre o objeto é de aproximadamente", forca,"  N.")
