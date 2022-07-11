#Usuario atribui os valores para x

def calcular_soma(x, cont):
    
    soma=0
    cont=0
    
    while x != -1:
        cont = x
        soma = soma + cont
		x = int(input("Digite outro valor para x: "))
    
	return soma

#Funcao Principal

x = int(input("Digite um valor para x: "))
cont = x

somaTotal = calcular_soma(x, cont)
print("Resultado = ",somaTotal - 1)


