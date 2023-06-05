# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.


def obter_menor_maior_soma(numeros):
    menor = float('inf')
    maior = float('-inf')
    soma = 0

    for numero in numeros:
        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero
        soma += numero

    return menor, maior, soma


# Solicitar números ao usuário
n = int(input("Digite a quantidade de números: "))
numeros = []

for i in range(n):
    numero = float(input("Digite o {}° número: ".format(i+1)))
    numeros.append(numero)

# Calcular menor valor, maior valor e soma dos valores
menor_valor, maior_valor, soma_valores = obter_menor_maior_soma(numeros)

# Imprimir resultados
print("Menor valor:", menor_valor)
print("Maior valor:", maior_valor)
print("Soma dos valores:", soma_valores)
