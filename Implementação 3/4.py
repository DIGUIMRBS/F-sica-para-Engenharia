def coeficiente_atrito(atrito, normal):
    return atrito / normal

peso = float(input("Digite o peso do objeto em N: "))
atrito = float(input("Digite a força de atrito necessária para manter o objeto em movimento constante em N: "))
normal = peso

coeficiente = coeficiente_atrito(atrito, normal)

print("O coeficiente de atrito entre as duas superfícies é de aproximadamente", coeficiente,".")
