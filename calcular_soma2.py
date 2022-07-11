#Usuario atribui os valores para x e y

def calcular_soma(x, y):
    soma = x + y
    return soma

#Principal

x = int(input("Digite um valor para x: "))
y = int(input("Digite um valor para y: "))

somaTotal = calcular_soma(x, y)
print("X + Y = ",somaTotal)


