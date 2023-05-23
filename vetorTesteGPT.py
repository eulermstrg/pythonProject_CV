# Função para organizar os valores e exibir em ordem numérica
def exibir_valores_ordenados(valores):
    valores_ordenados = sorted(valores)
    print("Valores organizados em ordem numérica:")
    for valor in valores_ordenados:
        print(valor)


# Função para ler os valores da entrada
def ler_valores():
    quantidade = int(input("Digite a quantidade de valores: "))
    valores = []
    for i in range(quantidade):
        valor = input(f"Digite o valor {i + 1}: ")
        # Verifica se o valor é inteiro ou booleano e converte para o tipo apropriado
        if valor.lower() == 'true':
            valor = True
        elif valor.lower() == 'false':
            valor = False
        else:
            valor = int(valor)
        valores.append(valor)
    return valores


# Chamada das funções
valores = ler_valores()
exibir_valores_ordenados(valores)
