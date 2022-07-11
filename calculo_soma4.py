# Usuario atribui os valores para x

def calcular_soma(x, cont):
    soma = 0
    cont = 0

    numeros = list()

    while x != -1:
        if x >= 0:
            cont = x
            soma = soma + cont
            x = int(input("Digite valores para x: "))
            numeros.append(x)
        else:
            x = int(input("Valor Invalido! Digite outro numero: "))

    print(f"Valores digitados {numeros}")

    return soma


# Funcao Principal

x=0
cont=x

somaTotal = calcular_soma(x, cont)
print("Resultado = ", somaTotal)
