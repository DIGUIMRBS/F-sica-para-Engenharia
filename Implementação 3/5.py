def forca_normal(m, a):
    g = 10
    return m * (g + a)

massa = float(input("Digite a massa do objeto em kg: "))
aceleracao = float(input("Digite a aceleração do elevador em m/s²: "))

forca = forca_normal(massa, aceleracao)

print("A força normal exercida sobre o objeto é de aproximadamente", forca," N.")
