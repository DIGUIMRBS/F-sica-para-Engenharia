def forca_atrito(atrito, normal):
    return atrito * normal

coeficiente = float(input("Digite o coeficiente de atrito: "))
forca_normal = float(input("Digite a força normal exercida sobre o objeto: "))
forca_atrito = forca_atrito(coeficiente, forca_normal)

print("A força de atrito necessária para manter o objeto em repouso é de aproximadamente", forca_atrito," N.")
