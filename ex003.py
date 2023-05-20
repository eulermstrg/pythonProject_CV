quantidade = int(input("Informe a quantidade de números que você deseja inserir na lista: "))
numeros = []

for i in range(quantidade):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

print("Os números digitados foram:")
for i, numero in enumerate(numeros):
    print("Número", i + 1, ":", numero)
